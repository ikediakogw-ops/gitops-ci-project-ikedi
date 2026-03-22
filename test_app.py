import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json() == {"status": "UP"}
