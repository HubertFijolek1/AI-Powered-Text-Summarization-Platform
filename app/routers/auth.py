from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserLogin,
    UserMeResponse
)
from app.models import User
from app.database import SessionLocal
from app.core.security import create_access_token, decode_access_token

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    hashed_password = pwd_context.hash(user.password)
    new_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login")
def login(user_login: UserLogin, db: Session = Depends(get_db)) -> dict:
    user = db.query(User).filter(User.email == user_login.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not pwd_context.verify(user_login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token_data = {
        "sub": user.email,
        "user_id": user.id
    }
    access_token = create_access_token(token_data)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me", response_model=UserMeResponse)
def get_current_user(authorization: str = Header(None), db: Session = Depends(get_db)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(status_code=401, detail="Invalid authorization format")

    payload = decode_access_token(token)
    if not payload or "user_id" not in payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user_id = payload["user_id"]
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return UserMeResponse.from_orm(user)
