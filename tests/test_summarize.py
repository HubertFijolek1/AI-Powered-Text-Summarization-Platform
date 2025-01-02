from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def mock_openai_summary():
    with patch("app.core.llm.summarize_with_openai", return_value="This is a mocked LLM summary"):
        yield

def test_summarize_endpoint(mock_openai_summary):
    response = client.post("/summaries/", json={"text": "This is a test string for summarization."})
    assert response.status_code == 200
    data = response.json()
    assert "original_text" in data
    assert "summary" in data
    assert data["summary"] == "This is a mocked LLM summary"

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
