import cv2
import numpy as np
import colour
from frame_composition_utils import is_point_inside_triangle, BT_709_coordinates, BT_2020_coordinates, ChromaticityDiagram, normalized

def luminance(image_rgb, sdr):
    """
    Compute luminance values from an RGB image.

    Args:
        image_rgb (numpy.ndarray): The input RGB image.
        sdr (bool): Set to True for SDR, False for HDR.

    Returns:
        numpy.ndarray: The calculated luminance values.
    """    
    r, g, b = np.split(image_rgb, 3, axis=-1)
    
    if sdr:
        # REC.709 (SDR)
        luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    else:
        # BT.2020 (HDR)
        luminance = 0.2627 * r + 0.6780 * g + 0.0593 * b
        
    return luminance

def fhlp(image, sdr=False):
    """
    Compute the Fraction of HighLight Pixel (FHLP) metric.

    Args:
        image (numpy.ndarray): The input image.
        sdr (bool, optional): Set to True for SDR, False for HDR (default is False).

    Returns:
        float: The FHLP value.

    Details:
        FHLP evaluates image quality in SDR and HDR contexts by quantifying the spatial ratio of 'highlight' pixels.
        A highlight pixel has a normalized luminance value (Y) greater than 0.1.
    """
    image = normalized(image)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate the luminance values
    luminance = compute_luminance(image_rgb, sdr)

    # Count the highlight pixels
    highlight_pixels = np.sum(luminance > 0.1)

    # Calculate the fraction of highlight pixels
    total_pixels = image.shape[0] * image.shape[1]
    fhlp = highlight_pixels / total_pixels

    return fhlp

def ehl(image, sdr=False):
    """
    Calculate the Extent of HighLight (EHL) metric.
   
    Args:
        image (numpy.ndarray): The input image.
        sdr (bool, optional): Set to True for SDR, False for HDR (default is False).

    Returns:
        float: The EHL metric value.

    Details:
      EHL evaluates image quality in SDR and HDR contexts by quantifying the extent of 'highlight' pixels.
    """
    image = normalized(image)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate the luminance values
    luminance = compute_luminance(image_rgb, sdr)

    # Clip the luminance values to 0.1
    clipped_luminance = np.clip(luminance, 0, 0.1)

    # Calculate the squared differences between the original and clipped luminance values
    squared_diff = (luminance - clipped_luminance) ** 2

    # Calculate the sum of squared differences
    sum_squared_diff = np.sum(squared_diff)

    # Calculate the average of squared differences and take the square root
    total_pixels = image.shape[0] * image.shape[1]
    ehl = np.sqrt(sum_squared_diff / total_pixels)

    return ehl

def all(image, sdr=False):
    """
    The ALL (Average Luminance Level) metric evaluates the average luminance level in SDR and HDR contexts by calculating the pixel-average of Y in FHLP.
    Useful for assessing brightness, visual quality, dynamic range, and comparing image processing algorithms or display technologies.
    
    Args:
        image (numpy.ndarray): The input image.
        sdr (bool, optional): Set to True for SDR, False for HDR (default is False).

    Returns:
        float: The ALL metric value.
    """

    image = normalized(image)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate the luminance values
    luminance = compute_luminance(image_rgb, sdr)

    # Filter the highlight pixels
    highlight_pixels = luminance[luminance > 0.1]

    # Calculate the average luminance level of highlight pixels
    all_value = np.mean(highlight_pixels)

    return all_value

def si(image, sdr=False):
    """
    Spatial Information (SI) is a metric that indicates the amount of spatial detail or complexity in an image. 

    Args:
        image (numpy.ndarray): The input image.
        sdr (bool, optional): Set to True for SDR, False for HDR (default is False).

    Returns:
        float: The SI metric value.

    Details:
        It is generally higher for images with more intricate textures and details.
        from https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.500-14-201910-I!!PDF-E.pdf,
        The spatial perceptual information, SI, is based on the Sobel filter. 
        Each video frame (luminance plane) at time n (Fn) is first filtered with the Sobel filter [Sobel (Fn)]. 
        The standard deviation over the pixels (stdspace) in each Sobel-filtered frame is then computed

    """
    image = normalized(image)
    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate the luminance values
    r, g, b = np.split(image_rgb, 3, axis=-1)
    luminance = compute_luminance(image_rgb, sdr)

    # Apply the Sobel filter in both the x and y directions
    sobel_x = cv2.Sobel(luminance, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(luminance, cv2.CV_64F, 0, 1, ksize=3)

    # Compute the magnitude of the gradient
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Calculate the standard deviation of pixels in the Sobel-filtered frame
    si = np.std(sobel_magnitude)

    return si

def cf(image, sdr=False):
    """
    Calculate the Opponent Color Metric - Colorfulness (CF) metric.
       Args:
        image (numpy.ndarray): The input image.
        sdr (bool, optional): Set to True for SDR, False for HDR (default is False).

    Returns:
        float: The CF metric value. 

    Details:    
        CF evaluates image quality using a computationally more efficient approach based on a simple opponent color space.
        This metric evaluates image quality using a computationally more efficient approach based on a simple opponent color space.
        Useful for assessing visual quality, dynamic range, and comparing image processing algorithms or display technologies.
    """
    image = normalized(image)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate the luminance values
    r, g, b = np.split(image_rgb, 3, axis=-1)

    # Compute the simple opponent color space
    rg = r - g
    yb = (0.5 * (r + g)) - b

    # Calculate standard deviation and mean value of rg and yb
    s_rg, s_yb = np.std(rg), np.std(yb)
    u_rg, u_yb = np.mean(rg), np.mean(yb)

    # Compute Srgyb and Urgyb
    s_rgyb = np.sqrt(s_rg ** 2 + s_yb ** 2)
    u_rgyb = np.sqrt(u_rg ** 2 + u_yb ** 2)

    # Calculate the M value
    m = s_rgyb + 0.3 * u_rgyb

    return m

def stdL(image, sdr=False):
    """
    Calculate the standard deviation of luminance (stdL) metric.

    Args:
        image (numpy.ndarray): The input image.
        sdr (bool, optional): Set to True for SDR, False for HDR (default is False).

    Returns:
        float: The stdL metric value.

    Details:
        The stdL metric, also known as the standard deviation of luminance, is a measure of the variation in brightness values across an image or a frame. 
        It is calculated as the standard deviation of the luminance values of all pixels in the image or frame.
    """
    image = normalized(image)

    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate the luminance values
    luminance = luminance(image_rgb, sdr)

    # Calculate the standard deviation of the luminance values
    stdL = np.std(luminance)

    return stdL

def fwgp(image_RGB, sdr=False, image_name='doesnt_matter.png'):
    """
    Calculate the Fraction of Pixels Outside of BT 709 and Inside of BT 2020 (FWGP) metric.

    FWGP measures how many pixels are outside of BT 709 and inside of BT 2020. A higher value is better.

    Args:
        image_RGB (numpy.ndarray): The input image in RGB format.
        sdr (bool, optional): Set to True for SDR, False for HDR (default is False).
        image_name (str, optional): The name of the image (default is 'doesnt_matter.png').

    Returns:
        float: The FWGP metric value.
    """

    image_RGB = cv2.cvtColor(image_RGB, cv2.COLOR_BGR2RGB)

    h, w, _ = image_RGB.shape
    no_pixels = float(h * w)
    no_pixels_inside_709 = 0.0
    no_pixels_inside_2020 = 0.0

    chromaticity_diagram = ChromaticityDiagram()
    chromaticity_diagram.init_image_from_data(image_RGB, image_name)
    xy_coordinates = chromaticity_diagram.xy_coordinates

    for i in range(len(xy_coordinates)):
            if is_point_inside_triangle (BT_709_coordinates[0], BT_709_coordinates[1], BT_709_coordinates[2], xy_coordinates[i]):
                no_pixels_inside_709 += 1
            elif is_point_inside_triangle(BT_2020_coordinates[0], BT_2020_coordinates[1], BT_2020_coordinates[2], xy_coordinates[i]) and not is_point_inside_triangle(BT_709_coordinates[0], BT_709_coordinates[1], BT_709_coordinates[2], xy_coordinates[i]):
                no_pixels_inside_2020 += 1
    
    return no_pixels_inside_2020 / no_pixels

def asl(image, sdr=False):
    """
    Calculate the ASL metric.
  
    Args:
        image_RGB (numpy.ndarray): The input image in RGB format.
        sdr (bool, optional): Set to True for SDR, False for HDR (default is False).

    Returns:
        float: The ASL metric value.
    """
    image = normalized(image)
    
    # image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # image_rgb_linear = colour.models.eotf_ST2084(image_rgb, L_p= 1000)/1000
    # image_rgb_linear = colour.models.eotf_BT1886(image_rgb)

    r, g, b = np.split(image, 3, axis=-1)

    # 1. calculate LMS
    # L = (1688*r + 2146*g + 262*b)/4096
    # M = (683*r + 2951*g + 462*b)/4096
    # S = (99*r + 309*g + 3688*b)/4096
    # LMS = np.dstack((L,M,S))


    L = 0.4002*r + 0.7076*g - 0.0808*b
    M = -0.2263*r + 1.1653*g + 0.0457*b
    S = 0.0000*r + 0.0000*g + 0.9182*b
    LMS = np.dstack((L,M,S))

    if np.min(LMS) < 0:
        raise ValueError("LMS values should be positive")
    if np.max(LMS) > 1:
        raise ValueError("LMS values should be less than 1")
    
    #2. Apply the ST 2084 non-linearity
    lms_non_linear = colour.models.eotf_inverse_ST2084(LMS)

    l,m,s = np.split(lms_non_linear, 3, axis=-1)

    #3. Calculate the ICtCp values

    I = (l + m)/2
    Ct = (6610*l - 13613*m + 7003*s)/4096
    Cp = (17933*s - 17390*l - 543*s)/4096

    C = np.dstack((Ct,Cp))
    l2_norm = np.sqrt(Ct**2 + Cp**2)

    ASL = np.sqrt(2) / (Ct.shape[0] * Ct.shape[1]) * np.sum(l2_norm)

    if np.max(C) >0.5:
        raise ValueError("C values should be less than 0.5")
    
    if np.min(C) < -0.5:
        raise ValueError("C values should be greater than -0.5")

    return ASL

    