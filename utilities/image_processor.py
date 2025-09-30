"""
Module for image processing utilities.
"""

import logging

from PIL import Image

logger = logging.getLogger(__name__)


def create_thumbnail(image_path, output_path, size=(128, 128)):
    """Creates a thumbnail of the provided image

    Args:
        image_path (str): path to the source image file
        output_path (str): path where the thumbnail will be saved
        size (tuple, optional): thumbnail size. Defaults to (128, 128).
    """
    try:
        logger.info("Creating thumbnail for %s with size %s", image_path, size)
        with Image.open(image_path) as img:
            img.thumbnail(size)
            img.save(output_path)
            logger.info("Thumbnail created successfully at: %s", output_path)
    except Exception as e:
        logger.error("Error processing image: %s", e)
        raise
