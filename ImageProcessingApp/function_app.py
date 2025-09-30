import tempfile
import os
import azure.functions as func
from utilities.image_processor import create_thumbnail


def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        local_image_path = "test-input/sample.jpg"
        if not os.path.exists(local_image_path):
            msg = "Test image not found. Place 'sample.jpg' in /test-input."
            return func.HttpResponse(msg, status_code=400)
        # Create temp file for thumbnail
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
            temp_output_path = temp_file.name
            create_thumbnail(local_image_path, temp_output_path)
            # Read thumbnail and return in HTTP response
            with open(temp_output_path, "rb") as f:
                image_data = f.read()
            os.unlink(temp_output_path)  # Clean up temp file
            return func.HttpResponse(image_data, mimetype="image/jpeg", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Error processing image: {str(e)}",  status_code=500)
