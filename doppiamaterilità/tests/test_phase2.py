import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_phase2_canvas(client):
    rv = client.get('/phase2/canvas')
    assert rv.status_code == 200
