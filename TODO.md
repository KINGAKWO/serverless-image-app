# TODO: Fix Linter Errors

## tests/test_function_app.py
- [x] Remove unused import pytest
- [x] Break long lines to under 80 characters
- [x] Remove unused parameter tmp_path from test_main_success
- [x] Change broad Exception to ValueError in test_main_exception
- [x] Add module docstring
- [x] Add docstrings to all test functions

## tests/test_image_processor.py
- [x] Remove unused import pytest
- [x] Break long lines
- [x] Remove unused parameter tmp_path from test_create_thumbnail_invalid_output_path
- [x] Add module docstring
- [x] Add docstrings to all test functions

## utilities/image_processor.py
- [x] Remove unused import os
- [x] Reorder imports to standard before third party
- [x] Change logging f-strings to lazy % formatting
- [x] Add module docstring

## Final Steps
- [x] Verify all changes by running linter
