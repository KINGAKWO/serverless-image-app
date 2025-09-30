import os

import pytest
from PIL import Image
from utilities.image_processor import create_thumbnail


def test_create_thumbnail_creates_file(tmp_path):
    # Arrange
    test_dir = os.path.dirname(__file__)
    test_image_path = os.path.join(test_dir, '../ImageProcessingApp/test-input/sample.jpg')
    output_path = tmp_path / "thumbnail.jpg"

    # Act
    create_thumbnail(test_image_path, str(output_path))

    # Assert
    assert output_path.exists()
    with Image.open(output_path) as img:
        assert img.size[0] <= 128 and img.size[1] <= 128


def test_create_thumbnail_invalid_image_path(tmp_path):
    # Arrange
    invalid_image_path = "non_existent.jpg"
    output_path = tmp_path / "thumbnail.jpg"

    # Act & Assert
    with pytest.raises(Exception):
        create_thumbnail(invalid_image_path, str(output_path))
