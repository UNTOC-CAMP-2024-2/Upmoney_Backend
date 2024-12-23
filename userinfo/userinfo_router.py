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

