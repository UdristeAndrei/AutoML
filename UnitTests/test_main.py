import os
import pytest
import pandas as pd
from app.main import automML

def test_autoML_init_empty():
    # Test that the class initializes with no arguments
    test_autoML_init_empty = automML()
    assert isinstance(test_autoML_init_empty, automML)

def test_autoML_init_DF():
    # Test that the class raises a ValueError if the data is not a DataFrame
    with pytest.raises(ValueError):
        automML(data='not a dataframe')

    # Test that the class initializes
    test_autoML_init = automML(data=pd.DataFrame())
    assert isinstance(test_autoML_init, automML)
    assert isinstance(test_autoML_init.data, pd.DataFrame)


def test_autoML_load_data():
    # Test that the method raises a ValueError if the path is not a string
    test_autoML_load_data = automML(data=pd.DataFrame())
    with pytest.raises(ValueError):
        test_autoML_load_data.load_data(path=123)

    # Test that the method loads the data
    test_autoML_load_data.load_data(path = os.getcwd() + '/UnitTests/data/movies.csv')
    assert isinstance(test_autoML_load_data.data, pd.DataFrame)

