# utilities/image_processor.py
from PIL import Image
import os

def create_thumbnail(image_path, output_path, size=(128,128)):
    """Creates a thumbnail of the provided image

    Args:
        image_path (str): path to the source image file
        output_path (str): path where the thumbnail will be saved
        size (tuple, optional): thumbnail size. Defaults to (128, 128).
    """
    try:
        with Image.open(image_path) as img:
            img.thumbnail(size)
            img.save(output_path)
            print(f"Thumbnail created successfully at: {output_path}")
    except Exception as e:
        print(f"Error processing image: {e}")
        raise
