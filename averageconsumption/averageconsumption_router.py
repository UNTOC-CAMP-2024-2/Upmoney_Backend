from fastapi import APIRouter, HTTPException, Depends, Response,Security

from sqlalchemy.orm import Session
from database import get_averageconsumptiondb

from .averageconsumption_schema import Create
from models import Averageconsumption as Averageconsumption_model

router = APIRouter(
    prefix="/averageconsumption"
)

def insert_data(db, table):
    db.add(table)
    db.commit()
    db.refresh(table)

@router.post("/create_averageconsumption", response_model=Create)
def create_averageconsumption(averageconsumption:Create, 
                averageconsumption_db: Session = Depends(get_averageconsumptiondb)):
    
    create = Averageconsumption_model(age=averageconsumption.age,
        gender=averageconsumption.gender,
        classifyid=averageconsumption.classifyid,
        content=averageconsumption.content)

    insert_data(averageconsumption_db, create)

    return create