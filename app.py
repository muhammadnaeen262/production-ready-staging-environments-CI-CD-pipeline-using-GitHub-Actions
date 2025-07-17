import app
import pytest

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_add(client):
    res = client.get('/add?a=2&b=3')
    assert res.status_code == 200
    assert res.get_json() == {'result': 5.0}

def test_subtract(client):
    res = client.get('/subtract?a=10&b=4')
    assert res.status_code == 200
    assert res.get_json() == {'result': 6.0}

def test_multiply(client):
    res = client.get('/multiply?a=6&b=7')
    assert res.status_code == 200
    assert res.get_json() == {'result': 42.0}

def test_divide(client):
    res = client.get('/divide?a=8&b=2')
    assert res.status_code == 200
    assert res.get_json() == {'result': 4.0}

def test_divide_by_zero(client):
    res = client.get('/divide?a=5&b=0')
    assert res.status_code == 400
    assert res.get_json() == {'error': 'Division by zero!'}
