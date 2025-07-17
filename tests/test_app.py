import pytest
import app  # assuming app.py is the main app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as c:
        yield c

def test_add_function_exists():
    assert app.add.__name__ == 'add'

def test_add_endpoint(client):
    response = client.get('/add?a=2&b=3')
    assert response.status_code == 200
    assert response.get_json() == {'result': 5.0}
