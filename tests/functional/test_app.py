"""
This file (test_app.py) contains the functional tests for the `app.y` file.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `app`.
"""

def test_home_page(app, test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    del app
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Prediction of the fuel efficiency of late -1970s and early 1980s automobiles." in response.data
    assert b"Predicted MPG:" not in response.data


def test_home_page_post(app,test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned
    """
    del app
    data = {"Cylinders":"8","Displacement":"390","Horsepower":"190","Weight":"3850","Acceleration":"14.0","Model Year":"76","Origin":"USA"}
    response = test_client.post('/',data=data)
    assert response.status_code == 405
    assert b"Prediction of the fuel efficiency of late -1970s and early 1980s automobiles." in response.data
    assert b"Predicted MPG:" in response.data
