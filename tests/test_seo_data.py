import pytest
from fastapi.testclient import TestClient
from src.tensor-pilot-145.api.seo_data import app

@pytest.fixture
def client():
    return TestClient(app)

def test_health_check(client):
    response = client.get("/api/seo/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
