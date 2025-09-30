"""
Azure Function app for image processing.
"""

import tempfile
import os
import logging
import azure.functions as func
from utilities.image_processor import create_thumbnail

logger = logging.getLogger(__name__)


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Main function for the Azure Function to process images.
    """
    logger.info("Received request: %s %s", req.method, req.url)

    # Input validation
    if req.method != 'GET':
        logger.warning("Unsupported method: %s", req.method)
        return func.HttpResponse("Method not allowed", status_code=405)

    try:
        local_image_path = "test-input/sample.jpg"
        if not os.path.exists(local_image_path):
            msg = (
                "Test image not found. "
                "Place 'sample.jpg' in /test-input."
            )
            logger.warning(msg)
            return func.HttpResponse(msg, status_code=400)
        # Create temp file for thumbnail
        with tempfile.NamedTemporaryFile(
            suffix='.jpg', delete=False
        ) as temp_file:
            temp_output_path = temp_file.name
            create_thumbnail(local_image_path, temp_output_path)
            # Read thumbnail and return in HTTP response
            with open(temp_output_path, "rb") as f:
                image_data = f.read()
            os.unlink(temp_output_path)  # Clean up temp file
            logger.info("Thumbnail created and returned successfully")
            return func.HttpResponse(
                image_data, mimetype="image/jpeg", status_code=200
            )
    except (OSError, ValueError) as e:
        logger.error("Error processing image: %s", str(e))
        error_msg = f"Error processing image: {str(e)}"
        return func.HttpResponse(error_msg, status_code=500)
