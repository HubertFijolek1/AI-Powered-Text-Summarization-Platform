import os
import jwt
from datetime import datetime, timedelta

JWT_SECRET = os.getenv("JWT_SECRET", "defaultsecret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRATION = int(os.getenv("JWT_EXPIRATION", "3600"))


def create_access_token(data: dict) -> str:
    """
    Create a JWT token containing the user's data.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(seconds=JWT_EXPIRATION)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> dict:
    """
    Decode a JWT token and return the payload if valid.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
