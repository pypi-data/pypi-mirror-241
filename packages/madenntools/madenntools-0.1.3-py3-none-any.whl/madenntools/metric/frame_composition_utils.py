import cv2
import numpy as np
import os
import colour
import matplotlib.pyplot as plt

BT_709_coordinates = np.array([[0.640, 0.330], [0.300, 0.600], [0.150, 0.060]])
BT_2020_coordinates = np.array([[0.708, 0.292], [0.170, 0.797], [0.131, 0.046]])

def image_info(image):
    # Read the image

    # Get the data type of the pixel, max value, and min value
    dtype = image.dtype
    max_val = image.max()
    min_val = image.min()

    # Print the information
    print(f"Data type: {dtype}")
    print(f"Max value: {max_val}")
    print(f"Min value: {min_val}")

def normalized(image):
    if image.dtype == np.uint8:
        return (image / 255.0).astype(np.float32)
    elif image.dtype == np.uint16:
        return (image / 65535.0).astype(np.float32)
    else:
        print('dtype of image is neither np.uint8 nor np.uint16, but: ', image.dtype)

def is_point_inside_triangle(p1, p2, p3, p4):
    # Calculate the area of the original triangle
    area = abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))/2.0)
    
    # Calculate the area of each of the three smaller triangles
    area1 = abs((p1[0]*(p2[1]-p4[1]) + p2[0]*(p4[1]-p1[1]) + p4[0]*(p1[1]-p2[1]))/2.0)
    area2 = abs((p2[0]*(p3[1]-p4[1]) + p3[0]*(p4[1]-p2[1]) + p4[0]*(p2[1]-p3[1]))/2.0)
    area3 = abs((p3[0]*(p1[1]-p4[1]) + p1[0]*(p4[1]-p3[1]) + p4[0]*(p3[1]-p1[1]))/2.0)
    
    # Check if the sum of the areas of the smaller triangles is equal to the area of the original triangle
    return area == area1 + area2 + area3

class ChromaticityDiagram:
    def __init__(self):
        # os.makedirs('./chroma_results', exist_ok=True)
        pass
    
    def init_image(self, image_path):
        self.image_name = os.path.basename(image_path)
        self.image_data, self.colourspace_name = self._load_image(image_path)
        self.colourspace = self._get_rgb_colourspace(self.colourspace_name)
        self._update_rgb()
        self._update_color_map()
        self._update_xyz()
        self._update_xy_coordinates()
        
    def init_image_from_data(self, image_data, image_name):
        self.image_name = image_name
        self.image_data = image_data
        self.colourspace_name, self.image_data = self._get_colourspace_name_from_data(image_data)
        self.colourspace = self._get_rgb_colourspace(self.colourspace_name)
        self._update_rgb()
        self._update_color_map()
        self._update_xyz()
        self._update_xy_coordinates()

    def _update_rgb(self):
        self.RGB = np.reshape(self.image_data, (-1, 3))
        self.RGB = self.RGB[self.RGB[:, 1].argsort()]

    def _update_color_map(self):
        self.color_map = self._convert_rgb_to_colormap(
            self.RGB,
            self.colourspace,
            colour.plotting.CONSTANTS_COLOUR_STYLE.colour.colourspace,
            apply_cctf_encoding=True,
        )

    def _update_xyz(self):
        self.XYZ = colour.RGB_to_XYZ(
            self.RGB,
            self.colourspace.whitepoint,
            self.colourspace.whitepoint,
            self.colourspace.matrix_RGB_to_XYZ,
        )

    def _update_xy_coordinates(self):
        self.xy_coordinates = colour.XYZ_to_xy(self.XYZ, self.colourspace.whitepoint)
     
    @staticmethod    
    def _get_colourspace_name_from_data(image_data):
        if image_data.dtype == np.uint8:
            image_data = (image_data.astype(np.float32) / 255.0).astype(np.float32)
            return 'ITU-R BT.709', image_data
        elif image_data.dtype == np.uint16:
            image_data = (image_data.astype(np.float32) / 65535.0).astype(np.float32)
            return 'ITU-R BT.2020', image_data
        else:
            raise ValueError("Image must be either 8-bit or 16-bit.")
    
    @staticmethod
    def _load_image(image_path):
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        # image to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if image.dtype == np.uint8:
            colourspace_name = 'ITU-R BT.709'
            image = (image.astype(np.float32) / 255.0).astype(np.float32)
        elif image.dtype == np.uint16:
            colourspace_name = 'ITU-R BT.2020'
            image = (image.astype(np.float32) / 65535.0).astype(np.float32)
        else:
            raise ValueError("Image must be either 8-bit or 16-bit.")
        return image, colourspace_name

    @staticmethod
    def _get_rgb_colourspace(colourspace_name):
        return colour.hints.cast(
            colour.RGB_COLOURSPACES,
            colour.utilities.first_item(
                colour.plotting.common.filter_RGB_colourspaces(colourspace_name).values()
            ),
        )

    def _convert_rgb_to_colormap(self, RGB, colourspace_src, colourspace_dst, apply_cctf_encoding=True):
        return np.clip(
            np.reshape(
                colour.RGB_to_RGB(
                    RGB,
                    colourspace_src,
                    colourspace_dst,
                    apply_cctf_encoding=apply_cctf_encoding,
                ),
                (-1, 3),
            ),
            0,
            1,
        )

    