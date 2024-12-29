import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.security import create_access_token

client = TestClient(app)


@pytest.fixture
def token_factory():
    def _make_token(user_id, user_email):
        data = {"sub": user_email, "user_id": user_id}
        return create_access_token(data)
    return _make_token


def test_get_current_user_no_header():
    response = client.get("/auth/me")
    assert response.status_code == 401
    assert response.json()["detail"] == "Authorization header missing"


def test_get_current_user_invalid_format():
    response = client.get("/auth/me", headers={"Authorization": "InvalidToken"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid authorization format"


def test_get_current_user_expired_or_invalid_token():
    response = client.get("/auth/me", headers={"Authorization": "Bearer abcdef"})
    assert response.status_code == 401


def test_get_current_user_valid(token_factory):
    # This test will fail to find the user in the DB by default
    token = token_factory(user_id=1, user_email="user@example.com")
    response = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    # Expect user not found if user ID 1 doesn't exist
    assert response.status_code == 401
    assert response.json()["detail"] in ["User not found", "Invalid or expired token"]

def test_put_current_user_no_header():
    response = client.put("/auth/me", json={"name": "NewName"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Authorization header missing"


def test_put_current_user_valid(token_factory):
    token = token_factory(user_id=999, user_email="old@example.com")
    response = client.put(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "NewName"}
    )
    # Expect 401 if user 999 is not in DB
    assert response.status_code == 401
    assert response.json()["detail"] == "User not found"