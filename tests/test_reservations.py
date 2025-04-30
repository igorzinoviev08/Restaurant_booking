import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_reservation():
    response = client.post("/reservations/", json={
        "customer_name": "Igor Ivanon",
        "table_id": 1,
        "reservation_time": "2023-10-20T19:00:00",
        "duration_minutes": 90
    })
    assert response.status_code == 200
    assert response.json()["customer_name"] == "Igor Ivanov"