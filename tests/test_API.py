from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_с_not_equal_zero():
    """Тест: a=0, b=0, c≠0 Уравнение не имеет решений"""
    response = client.get("/solve?a=0&b=0&c=5")
    assert response.status_code == 400
    assert response.json() == {"detail": "Уравнение не имеет решений"}
