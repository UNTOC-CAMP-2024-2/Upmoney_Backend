from fastapi import APIRouter, HTTPException, Depends, Response,Security

from sqlalchemy.orm import Session
from database import get_scholarshipdb

from .scholarship_schema import Create
from models import Scholarship as Scholarship_model

router = APIRouter(
    prefix="/scholarship"
)

def insert_data(db, table):
    db.add(table)
    db.commit()
    db.refresh(table)

@router.post("/create_scholarship", response_model=Create)
def create_monetaryluck(scholarship:Create, 
                       scholarship_db: Session = Depends(get_scholarshipdb)):
    
    create = Scholarship_model(period=scholarship.period,
        recipients=scholarship.recipients,
        money=scholarship.money,
        HowToAccept=scholarship.HowToAccept,
        subject=scholarship.subject,
        qualification=scholarship.qualification,
        inquiry=scholarship.inquiry)

    insert_data(scholarship_db, create)

    return create