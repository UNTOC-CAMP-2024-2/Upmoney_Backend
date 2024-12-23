from fastapi import APIRouter, HTTPException, Depends, Response,Security

from sqlalchemy.orm import Session
from database import get_userinfodb

from .userinfo_schema import Create
from models import Userinfo as Userinfo_model

router = APIRouter(
    prefix="/userinfo"
)

def insert_data(db, table):
    db.add(table)
    db.commit()
    db.refresh(table)

@router.post("/signup", response_model=Create)
def signup(newuser: Create, 
                       userinfo_db: Session = Depends(get_userinfodb)):
    user =  get_userinfodb(newuser.userid, userinfo_db)
    if user:
        raise HTTPException(status_code=404, detail="User already exists")

    create = Userinfo_model(userid=newuser.userid,
                            password=newuser.password,
                            username=newuser.username,
                            age=newuser.age,
                            gender=newuser.gender)
    
    insert_data(userinfo_db, create)
    return HTTPException(status_code=200, detail="Signup Successful")