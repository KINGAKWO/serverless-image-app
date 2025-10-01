# serverless-image-app

## Project Overview
This project is a serverless image processing application built using Azure Functions. It processes images by creating thumbnails and serves them via HTTP endpoints. The project includes utility functions for image processing and comprehensive tests to ensure functionality.

## Local Setup

### Prerequisites
- Python 3.9+
- Azure Functions Core Tools
- Virtual environment tool (e.g., `venv`)

### Installation Steps
1. Clone the repository:
   ```
   git clone <repository-url>
   cd serverless-image-app
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run tests to verify setup:
   ```
   python -m pytest
   ```
5. Run the Azure Function locally:
   ```
   func start
   ```

## Deployment

### Azure
- The project is designed to be deployed as an Azure Function App.
- Use Azure CLI or Azure Portal to deploy the function.
- Ensure the `local.settings.json` is configured with necessary environment variables.

### Google Cloud Platform (GCP)
- To deploy on GCP, you can containerize the function using Cloud Functions or Cloud Run.
- Create a Dockerfile that installs dependencies and runs the function.
- Deploy using `gcloud` CLI:
  ```
  gcloud functions deploy <function-name> --runtime python39 --trigger-http --allow-unauthenticated
  ```
- Adjust the function entry point and environment variables as needed.

## Testing
- Tests are located in the `tests/` directory.
- Use `pytest` to run all tests.
- Tests cover image processing utilities and the Azure Function app endpoints.

## Project Structure
- `ImageProcessingApp/`: Azure Function app code and configuration.
- `utilities/`: Image processing utility functions.
- `tests/`: Unit tests for the application.

## Notes
- Ensure the sample image `sample.jpg` is placed in `ImageProcessingApp/test-input/` for tests and local runs.
- The project uses Pillow for image processing.
