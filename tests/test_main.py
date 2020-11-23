import pytest

from main import app


@pytest.fixture
def test_client():
    app.config["TESTING"] = True
    return app.test_client()


def test_GET_index(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert "備品・書籍の登録" in response.data.decode('utf-8')
    assert "キーワード、ISBNコード、ASINコードのいずれかを入力してください" in response.data.decode('utf-8')


def test_GET_search_with_correct_query(test_client):
    response = test_client.get("/search?query=kindle")
    assert b"kindle" in response.data


def test_GET_search_with_incorrect_query(test_client):
    response = test_client.get("/search?unexpected_query=kindle")
    assert "TOPページに戻ってキーワードを入力してください" in response.data.decode('utf-8')


def test_GET_search_with_not_inputted_query(test_client):
    response = test_client.get("search?query=")
    assert "TOPページに戻ってキーワードを入力してください" in response.data.decode('utf-8')


def test_GET_search_direct_access(test_client):
    response = test_client.get("/search")
    assert "TOPページに戻ってキーワードを入力してください" in response.data.decode('utf-8')
