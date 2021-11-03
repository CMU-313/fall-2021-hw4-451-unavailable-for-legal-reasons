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

def test_predict1(client):
    r = client.get('/predict?age=15&absences=5&health=2&G1=10&G2=10&Studytime=2')
    print("Testing prediction...", end=" ")
    assert "Internal Server Error" not in str(r.data)
    print("Test passed!")
    print(f"[MID] Prediction received on age=18, absences=93, health=2, G1=10, G2=10, Studytime=2: {r.data}")

def test_predict2(client):
    r = client.get('/predict?age=18&absences=93&health=2&G1=1&G2=1&Studytime=1')
    print("Testing prediction...", end=" ")
    assert "Internal Server Error" not in str(r.data)
    print("Test passed!")
    print(f"[LOW] Prediction received on age=18, absences=93, health=2, G1=1, G2=1, Studytime=1: {r.data}")

def test_predict3(client):
    r = client.get('/predict?age=22&absences=1&health=5&G1=20&G2=20&Studytime=4')
    print("Testing prediction...", end=" ")
    assert "Internal Server Error" not in str(r.data)
    print("Test passed!")
    print(f"[HIGH] Prediction received on age=22, absences=1, health=5, G1=20, G2=20, Studytime=4: {r.data}")

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
