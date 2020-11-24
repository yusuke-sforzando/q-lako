import pytest

from main import app


@pytest.fixture
def test_client():
    app.config["TESTING"] = True
    return app.test_client()


def test_GET_index(test_client):
    response = test_client.get("/")
    assert b"index.html" in response.data
    assert response.status_code == 200


def test_GET_search(test_client):
    response = test_client.get("/search?query=サーカスTC")
    assert b"search.html" in response.data
    assert response.status_code == 200


def test_POST_registration(test_client):
    response = test_client.post('/registration', data={"asin": "B07B7HG86W"})
    assert b"registration details" in response.data
    assert response.status_code == 200


def test_GET_registration_direct_access(test_client):
    response = test_client.get("/registration")
    assert "TOPページに戻ってキーワードを入力してください" in response.data.decode('utf-8')
    assert response.status_code == 200
