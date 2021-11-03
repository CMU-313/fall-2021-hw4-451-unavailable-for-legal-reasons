import os
import tempfile
import requests

import pytest

from apps.app import app

url = "http://localhost:5000/predict"

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_client(client):
    r = client.get('/')
    print("Testing client initialization...", end=" ")
    assert (b'try the predict route it is great!' == r.data)
    print("Test passed!")

def test_predict(client):
    r = client.get('/predict?age=5&absences=5&health=20')
    print("Testing prediction...", end=" ")
    assert "Internal Server Error" not in str(r.data)
    assert int(r.prediction) == 1
    print("Test passed!")

def test_empty(client):
    r = client.get('/predict?')
    print("Testing empty prediction...", end=" ")
    assert "500 Internal Server Error" in str(r.data)
    print("Test passed!")

def test_missing_one(client):
    r = client.get('/predict?&&absences=5&health=20')
    print("Testing incomplete prediction, missing one argument...", end=" ")
    assert "500 Internal Server Error" in str(r.data)
    print("Test passed!")

def test_missing_multiple(client):
    r = client.get('/predict?&&absences=5&')
    print("Testing incomplete prediction, missing multiple arguments...", end=" ")
    assert "500 Internal Server Error" in str(r.data)
    print("Test passed!")

def test_extra_one(client):
    r = client.get('/predict?age=5&absences=5&health=20&test=32')
    print("Testing addition prediction features, extra one argument...", end=" ")
    assert "500 Internal Server Error" in str(r.data)
    print("Test passed!")
