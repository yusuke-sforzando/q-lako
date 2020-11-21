import pytest

from main import app


@pytest.fixture
def test_client():
    app.config["TESTING"] = True
    return app.test_client()


def test_GET_index(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert "書籍・備品の登録", "キーワード、ISBNコード、ASINコードのいずれかを入力してください" in response.data.decode('utf-8')


def test_GET_search_result_correct_query(test_client):
    response = test_client.get("/search-result?input_keyword=kindle")
    assert b"kindle" in response.data


def test_GET_search_result_incorrect_query(test_client):
    response = test_client.get("/search-result?unexpected_query=kindle")
    print(response.data)
    assert b"kindle" not in response.data


def test_GET_search_result_query_not_inputted(test_client):
    response = test_client.get("/search-result?input_keyword=")
    print(response.data.decode('utf-8'))
    assert "TOPページに戻ってキーワードを入力してください" in response.data.decode('utf-8')


def test_GET_search_result_direct_access(test_client):
    response = test_client.get("/search-result")
    print(response.data.decode('utf-8'))
    assert "TOPページに戻ってキーワードを入力してください" in response.data.decode('utf-8')
