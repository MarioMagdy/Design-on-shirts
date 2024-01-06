# import modules
# from rembg import remove
# from PIL import Image


# def remove_background(input_path,output_path):
#     # read input image as byte array
#     with open(input_path, 'rb') as i:
#         input = i.read()

#     # remove background using rembg
#     output = remove(input)

#     # write output image as png file
#     with open(output_path, 'wb') as o:
#         o.write(output)


# # remove_background(input_path,output_path)


from PIL import Image
import numpy as np


def remove_background2(input_path, output_path, tolerance=30, bing=True):
    "removes background from image in the path and saves it to the output path"

    # Open the image
    image = Image.open(input_path)

    # Convert the image to a NumPy array
    img_array = np.array(image)

    # Find the most common color
    background_color = tuple(np.median(img_array, axis=(0, 1)).astype(int))

    # Create a mask for pixels within the tolerance range
    mask = np.all(np.abs(img_array - background_color) <= tolerance, axis=-1)

    alpha_channel = np.ones_like(img_array[..., 0], dtype=np.uint8) * 255

    # Set the alpha channel to 0 for transparent pixels
    alpha_channel[mask] = 0

    # Add the alpha channel to the image array
    img_array = np.dstack((img_array, alpha_channel))

    # Convert the NumPy array back to an image with an alpha channel
    result_image = Image.fromarray(img_array, 'RGBA')

    # Save the image with no background
    result_image.save(output_path, "PNG")






def remove_watermark(input_path, output_path):
    """removes the bing watermark, 
    run it after the background remover"""
    # Open the image
    image = Image.open(input_path)
    
    # Convert the image to a NumPy array
    img_array = np.array(image)

    # Check if the image already has an alpha channel
    if img_array.shape[2] == 3:
        # If no alpha channel exists, create one
        alpha_channel = np.ones_like(img_array[..., 0], dtype=np.uint8) * 255
        img_array = np.dstack((img_array, alpha_channel))

    
    elif img_array.shape[2] == 4:
        # If the array already has an alpha channel, use it
        pass
    else:
        raise ValueError("Unsupported array shape. The array should have either 3 or 4 channels.")
    
    # Create a mask for the region of the watermark
    watermark_mask = np.zeros_like(img_array[..., 0], dtype=bool)
    watermark_mask[970:1024, 0:45] = True

    # Set the pixels in the watermark region to be transparent
    img_array[watermark_mask, 3] = 0  # Set alpha channel to 0 for transparent pixels
    

    # Save the image with alpha channel
    result_image = Image.fromarray(img_array, 'RGBA')
    result_image.save(output_path, "PNG")


