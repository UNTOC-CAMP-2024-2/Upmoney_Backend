from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta
from database import get_userinfodb  # 데이터베이스 세션 가져오기
from .userinfo_schema import TokenResponse, UserCreate
from models import Userinfo
from .userinfo_crud import get_user_by_username, verify_password, create_user
from dotenv import load_dotenv
import os
load_dotenv()
router = APIRouter()

# JWT 설정
SECRET_KEY = os.environ.get("SECRET_KEY")  # .env에서 로드된 값
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_userinfodb)):
    user = get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_userinfodb)):
    # 사용자 이름 중복 확인
    existing_user = db.query(Userinfo).filter(Userinfo.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # 사용자 생성
    new_user = create_user(db, user.username, user.password, user.name, user.age, user.gender)
    return {"message": "User created successfully", "user_id": new_user.id}
