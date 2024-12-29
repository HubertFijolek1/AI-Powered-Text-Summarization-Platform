from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_summarize_endpoint():
    response = client.post(
        "/summaries/",
        json={"text": "This is a test string for summarization."}
    )
    assert response.status_code == 200
    data = response.json()
    assert "original_text" in data
    assert "summary" in data
    assert "mock summary" in data["summary"]


def test_summarize_short_input():
    # Input less than 5 chars
    response = client.post("/summaries/", json={"text": "Hi"})
    assert response.status_code == 422
    assert "detail" in response.json()
    assert "at least 5 characters" in str(response.json()["detail"])

    # Input that is 5 chars with whitespace
    response2 = client.post("/summaries/", json={"text": "  abc "})
    # "  abc " => "abc" after strip => length 3 => also fails
    assert response2.status_code == 422
