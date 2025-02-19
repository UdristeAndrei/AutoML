import pytest
from app.main import automML

def test_main():
    test_AutoML = automML(123)
    assert test_AutoML.data == 123

