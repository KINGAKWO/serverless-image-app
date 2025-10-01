# tests/test_basic.py
def test_environment():
    """Basic environment test"""
    assert True

def test_imports():
    """Test that basic imports work"""
    try:
        import azure.functions
        from PIL import Image
        assert True
    except ImportError:
        assert False, "Required packages not installed"