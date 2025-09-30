"""Test module for the Azure Function app."""

import os
from unittest.mock import MagicMock

import azure.functions as func

from ImageProcessingApp import function_app


def test_main_success(monkeypatch):
    """Test successful image processing and thumbnail creation."""
    # Arrange
    test_dir = os.path.dirname(__file__)
    sample_path = '../ImageProcessingApp/test-input/sample.jpg'
    test_image_path = os.path.join(test_dir, sample_path)
    monkeypatch.setattr(function_app, "local_image_path", test_image_path)

    # Mock create_thumbnail to just copy the file
    def mock_create_thumbnail(input_path, output_path, size=(128, 128)):
        with open(input_path, "rb") as src, open(output_path, "wb") as dst:
            dst.write(src.read())
    monkeypatch.setattr(function_app, "create_thumbnail", mock_create_thumbnail)

    # Create a dummy HttpRequest
    req = MagicMock(spec=func.HttpRequest)

    # Act
    response = function_app.main(req)

    # Assert
    assert response.status_code == 200
    assert response.mimetype == "image/jpeg"
    assert response.get_body() is not None


def test_main_missing_image(monkeypatch):
    """Test handling when the test image is missing."""
    # Arrange
    monkeypatch.setattr(function_app, "local_image_path", "non_existent.jpg")
    req = MagicMock(spec=func.HttpRequest)

    # Act
    response = function_app.main(req)

    # Assert
    assert response.status_code == 400
    assert "Test image not found" in response.get_body().decode()


def test_main_exception(monkeypatch):
    """Test error handling when thumbnail creation fails."""
    # Arrange
    def raise_exception(*args, **kwargs):
        raise ValueError("Test exception")
    monkeypatch.setattr(function_app, "create_thumbnail", raise_exception)
    test_dir = os.path.dirname(__file__)
    sample_path = '../ImageProcessingApp/test-input/sample.jpg'
    test_image_path = os.path.join(test_dir, sample_path)
    monkeypatch.setattr(function_app, "local_image_path", test_image_path)
    req = MagicMock(spec=func.HttpRequest)

    # Act
    response = function_app.main(req)

    # Assert
    assert response.status_code == 500
    assert "Error processing image" in response.get_body().decode()
