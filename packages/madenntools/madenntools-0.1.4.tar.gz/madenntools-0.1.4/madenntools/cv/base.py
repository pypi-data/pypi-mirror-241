import os
import cv2
import tqdm
import numpy as np

def _remove_prefix_number(input_string):

    if input_string and input_string[0].isdigit() and "_" in input_string:
        return input_string.split("_", 1)[1]
    return input_string

def blend(foreground_image, binary_mask, level=(128, 128, 128)):
    """
    Blend a foreground image with a background using the binary mask as the alpha channel.

    This function takes a foreground image, a binary mask, and an optional background color to create a blended image. The binary mask is used as the alpha channel to determine the transparency of the foreground image.

    Args:
        foreground_image (numpy.ndarray): The BGR image to be blended.
        binary_mask (numpy.ndarray): The binary mask in BGR format.
        level (tuple, optional): The BGR color of the background. Defaults to (128, 128, 128).

    Returns:
        numpy.ndarray: The blended image.
    """

    # Convert the binary mask to a single-channel grayscale image
    alpha_channel = cv2.cvtColor(binary_mask, cv2.COLOR_BGR2GRAY)

    # Convert the alpha channel to a range of 0 to 1 (float)
    alpha_channel = alpha_channel.astype(float) / 255.0

    # Create a solid color background image with the same shape as the foreground
    background = np.ones_like(foreground_image)
    background[:, :] = level

    blended_image = np.zeros_like(foreground_image)

    blended_image[:,:, 0] = foreground_image[:,:, 0] * alpha_channel + background[:,:, 0] * (1 - alpha_channel)
    blended_image[:,:, 1] = foreground_image[:,:, 1] * alpha_channel + background[:,:, 1] * (1 - alpha_channel)
    blended_image[:,:, 2] = foreground_image[:,:, 2] * alpha_channel + background[:,:, 2] * (1 - alpha_channel)

    return blended_image

def collage_images(image_and_caption_list, output_path, max_columns=3, caption_height=30):
    """
    Creates a horizontal collage from the list of images and captions provided
    using OpenCV and saves it to the specified output path.

    Args:
    - image_and_caption_list (list): A list of tuples, each containing an image
      path and its corresponding caption. The image path should be a string,
      and the caption should be a string.
    - output_path (str): The path where the output image should be saved.
    - max_columns (int): The maximum number of columns in the collage.
    - caption_height (int): The height of the caption area in pixels.

    Returns:
    - None
    """
    images = []

    for i, (image_path, caption) in enumerate(image_and_caption_list):
        image = cv2.imread(image_path)
        caption = _remove_prefix_number(caption)
        bbox = np.zeros([caption_height, image.shape[1], 3], dtype=image.dtype)
        cv2.putText(bbox, caption, (bbox.shape[1] // 2, caption_height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        image = cv2.vconcat([bbox, image])
        images.append(image)

    num_images = len(image_and_caption_list)
    num_rows = (num_images + max_columns - 1) // max_columns

    image_height, image_width, _ = images[0].shape
    collage_width = image_width * min(num_images, max_columns)
    collage_height = image_height * num_rows

    # Create a blank collage canvas
    collage = np.zeros((collage_height, collage_width, 3), dtype=np.uint8)

    # Loop over each image and caption and add them to the collage
    for i, image in enumerate(images):

        row_index = i // max_columns
        col_index = i % max_columns

        # Calculate the position to place the image in the collage
        start_x = col_index * image_width
        end_x = start_x + image_width
        start_y = row_index * image_height
        end_y = start_y + image_height

        # Place the image in the collage
        collage[start_y:end_y, start_x:end_x] = image

    # Save the collage to the specified output path
    cv2.imwrite(output_path, collage)

def collage_directories(root_dir, output_dir, max_columns=3, caption_height=30):
    """
    Create a collage for each image in all the directories within the root directory and save them to the output directory.
    If the output_dir is already in the root dir, it ignores it.

    This function assumes that the root directory contains multiple subdirectories, and each subdirectory contains one or more images with the same names.

    Args:
        root_dir (str): The root directory containing subdirectories with images.
        output_dir (str): The directory where the collage images will be saved.
        max_columns (int, optional): The maximum number of columns in the collage. Defaults to 3.
        caption_height (int, optional): The height of the caption area in pixels. Defaults to 30.

    Returns:
        None
    """

    os.makedirs(output_dir, exist_ok=True)

    subdirectories = os.listdir(root_dir)
    if os.path.basename(output_dir) in subdirectories:
        subdirectories.pop(subdirectories.index(os.path.basename(output_dir)))

    image_paths = [[] for _ in range(len(os.listdir(os.path.join(root_dir, subdirectories[0]))))]

    for subdir in subdirectories:

        if os.path.join(root_dir, subdir) == output_dir:
            continue
        
        image_names = sorted(os.listdir(os.path.join(root_dir, subdir)))

        for i, name in enumerate(image_names):
            image_paths[i].append(os.path.join(root_dir, subdir, name))

    for paths in tqdm.tqdm(image_paths, desc='Collaging images...'):
        image_and_caption_list = []
        for path in paths:
            caption = os.path.basename(os.path.dirname(path))
            image_and_caption_list.append((path, caption))
        output_path = os.path.join(output_dir, path.split(os.sep)[-1])
        collage_images(image_and_caption_list, output_path, max_columns, caption_height)
