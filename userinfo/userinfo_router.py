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

@router.post("/create_userinfo", response_model=Create)
def create_monetaryluck(userinfo:Create, 
                       userinfo_db: Session = Depends(get_userinfodb)):
    
    create = Userinfo_model(userid=userinfo.userid,
        password=userinfo.password,
        username=userinfo.username,
        age=userinfo.age,
        gender=userinfo.gender)

    insert_data(userinfo_db, create)

    return create