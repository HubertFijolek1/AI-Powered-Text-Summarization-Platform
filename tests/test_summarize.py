from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_summarize_endpoint():
    response = client.post("/summaries/",
                           json={"text": "This is a test string for summarization."})
    assert response.status_code == 200
    data = response.json()
    assert "original_text" in data
    assert "summary" in data
    assert "mock summary" in data["summary"]
