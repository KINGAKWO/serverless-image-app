import tempfile
import os
import logging
import azure.functions as func
from utilities.image_processor import create_thumbnail

logger = logging.getLogger(__name__)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logger.info(f"Received request: {req.method} {req.url}")

    # Input validation
    if req.method != 'GET':
        logger.warning(f"Unsupported method: {req.method}")
        return func.HttpResponse("Method not allowed", status_code=405)

    try:
        local_image_path = "test-input/sample.jpg"
        if not os.path.exists(local_image_path):
            msg = "Test image not found. Place 'sample.jpg' in /test-input."
            logger.warning(msg)
            return func.HttpResponse(msg, status_code=400)
        # Create temp file for thumbnail
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
            temp_output_path = temp_file.name
            create_thumbnail(local_image_path, temp_output_path)
            # Read thumbnail and return in HTTP response
            with open(temp_output_path, "rb") as f:
                image_data = f.read()
            os.unlink(temp_output_path)  # Clean up temp file
            logger.info("Thumbnail created and returned successfully")
            return func.HttpResponse(image_data, mimetype="image/jpeg", status_code=200)
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        return func.HttpResponse(f"Error processing image: {str(e)}", status_code=500)
