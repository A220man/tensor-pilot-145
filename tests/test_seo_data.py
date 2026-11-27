import pytest
from fastapi.testclient import TestClient
from src.tensor_pilot_145.api.seo_data import app

@pytest.fixture
def client():
    return TestClient(app)

def test_health_check(client):
    response = client.get("/api/seo/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_keyword_analysis_limit(client):
    """Test that limit parameter is respected in keyword analysis."""
    # Test with limit: 5
    response = client.post('/api/seo/keyword/analyze', json={"keyword": "test", "limit": 5})
    assert response.status_code == 200
    assert len(response.json()['serp_results']) == 5

    # Test with limit: 1
    response = client.post('/api/seo/keyword/analyze', json={"keyword": "test", "limit": 1})
    assert response.status_code == 200
    assert len(response.json()['serp_results']) == 1

    # Test default limit (no limit specified, should default to 10)
    response = client.post('/api/seo/keyword/analyze', json={"keyword": "test"})
    assert response.status_code == 200
    assert len(response.json()['serp_results']) == 10


def test_keyword_analysis_no_keyword(client):
    """Test that missing keyword returns 400."""
    response = client.post('/api/seo/keyword/analyze', json={"other": "value"})
    assert response.status_code == 400
