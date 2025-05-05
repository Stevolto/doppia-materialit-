import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_phase1(client):
    rv = client.get('/phase1/')
    assert rv.status_code == 200
