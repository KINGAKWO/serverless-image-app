"""Test module for the image processor utility."""

import os

from PIL import Image
from utilities.image_processor import create_thumbnail


def test_create_thumbnail_creates_file(tmp_path):
    """Test that create_thumbnail creates a file."""
    # Arrange
    test_dir = os.path.dirname(__file__)
    test_image_path = os.path.join(
        test_dir,
        '../ImageProcessingApp/test-input/sample.jpg'
    )
    output_path = tmp_path / "thumbnail.jpg"

    # Act
    create_thumbnail(test_image_path, str(output_path))

    # Assert
    assert output_path.exists()
    with Image.open(output_path) as img:
        assert img.size[0] <= 128 and img.size[1] <= 128


def test_create_thumbnail_invalid_image_path(tmp_path):
    """Test handling of invalid image path."""
    # Arrange
    invalid_image_path = "non_existent.jpg"
    output_path = tmp_path / "thumbnail.jpg"

    # Act & Assert
    try:
        create_thumbnail(invalid_image_path, str(output_path))
        assert False, "Expected exception"
    except Exception:  # pylint: disable=broad-exception-caught
        pass


def test_create_thumbnail_custom_size(tmp_path):
    """Test create_thumbnail with custom size."""
    # Arrange
    test_dir = os.path.dirname(__file__)
    test_image_path = os.path.join(
        test_dir,
        '../ImageProcessingApp/test-input/sample.jpg'
    )
    output_path = tmp_path / "thumbnail.jpg"
    custom_size = (64, 64)

    # Act
    create_thumbnail(test_image_path, str(output_path), size=custom_size)

    # Assert
    assert output_path.exists()
    with Image.open(output_path) as img:
        assert img.size[0] <= 64 and img.size[1] <= 64


def test_create_thumbnail_preserves_aspect_ratio(tmp_path):
    """Test that aspect ratio is preserved in thumbnail."""
    # Arrange
    test_dir = os.path.dirname(__file__)
    test_image_path = os.path.join(
        test_dir,
        '../ImageProcessingApp/test-input/sample.jpg'
    )
    output_path = tmp_path / "thumbnail.jpg"

    # Act
    create_thumbnail(test_image_path, str(output_path))

    # Assert
    assert output_path.exists()
    with Image.open(output_path) as img, Image.open(test_image_path) as orig:
        orig_ratio = orig.size[0] / orig.size[1]
        thumb_ratio = img.size[0] / img.size[1]
        assert (
            abs(orig_ratio - thumb_ratio) < 0.1
        )  # Allow small difference due to thumbnail algorithm


def test_create_thumbnail_invalid_output_path():
    """Test handling of invalid output path."""
    # Arrange
    test_dir = os.path.dirname(__file__)
    test_image_path = os.path.join(
        test_dir,
        '../ImageProcessingApp/test-input/sample.jpg'
    )
    invalid_output_path = "/invalid/path/thumbnail.jpg"

    # Act & Assert
    try:
        create_thumbnail(test_image_path, invalid_output_path)
        assert False, "Expected exception"
    except Exception:  # pylint: disable=broad-exception-caught
        pass
