"""
This file (test_model.py) contains the unit tests for the model.py file.
"""
from model import Model


def test_new_model():
    """
    GIVEN a model with the input features
    WHEN the model is instantiated 
    THEN check that the features are correctly identified and properly converted into a float list 
    """
    new_model = Model('8', '390', '190', '3850', '14.0', '76','Europe')
    assert new_model.cylinders == '8'
    assert new_model.displacement == '390'
    assert new_model.horsepower =='190'
    assert new_model.weight == '3850'
    assert new_model.acceleration == '14.0'
    assert new_model.model_year == '76'
    assert new_model.origin == 'Europe'
    assert new_model.generate_numeric_features()
    assert new_model.origin_mapping() != None
    
def test_new_model_with_fixture(new_model):
    """
    GIVEN a model with the input features
    WHEN the model is instantiated 
    THEN check that the features are correctly identified and properly converted into a float list 
    """
    assert new_model.cylinders == '8'
    assert new_model.displacement == '390'
    assert new_model.horsepower =='190'
    assert new_model.weight == '3850'
    assert new_model.acceleration == '14.0'
    assert new_model.model_year == '76'
    assert new_model.origin == 'Europe'
    assert new_model.generate_numeric_features()
    assert new_model.origin_mapping() != None

