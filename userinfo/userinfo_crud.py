from sqlalchemy.orm import Session
from models import Userinfo  # User는 DB 모델이어야 합니다.
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_user(db: Session, username: str, password: str, name: str, age: int, gender: str):
    hashed_password = hash_password(password)
    new_user = Userinfo(
        username=username,
        hashed_password=hashed_password,
        name=name,
        age=age,
        gender=gender,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db: Session, username: str):
    return db.query(Userinfo).filter(Userinfo.username == username).first()

def verify_password(plain_password: str, hashed_password: str):
    # 실제로는 bcrypt 또는 다른 해시 함수를 사용해야 합니다.
    return plain_password == hashed_password