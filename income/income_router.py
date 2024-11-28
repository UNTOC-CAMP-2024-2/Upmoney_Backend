from fastapi import APIRouter, HTTPException, Depends, Response,Security

from sqlalchemy.orm import Session
from database import get_incomedb

from .income_schema import Create
from models import Income as Income_model

router = APIRouter(
    prefix="/income"
)

def insert_data(db, table):
    db.add(table)
    db.commit()
    db.refresh(table)

@router.post("/create_income", response_model=Create)
def create_consumption(income:Create, 
                       income_db: Session = Depends(get_incomedb)):
    
    create = Income_model(
        income_userid=income.userid,
        income_content=income.content)

    insert_data(income_db, create)

    return create