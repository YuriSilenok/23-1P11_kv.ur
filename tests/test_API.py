from fastapi.testclient import TestClient
import unittest

from .main import app

client = TestClient(app)


class TestAPI(unittest.TestCase):
    """Класс тестирования API"""
    response = client.get("/solve?a=0&b=0&c=5")
    assert response.status_code == 400
    assert response.json() == {"detail": "Уравнение не имеет решений"}
