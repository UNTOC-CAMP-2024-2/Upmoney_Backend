from fastapi import APIRouter, HTTPException, Depends, Response,Security

from sqlalchemy.orm import Session
from database import get_totalconsumptiondb

from .totalconsumption_schema import Create
from models import Totalconsumption as Totalconsumption_model

router = APIRouter(
    prefix="/totalconsumption"
)

def insert_data(db, table):
    db.add(table)
    db.commit()
    db.refresh(table)

@router.post("/create_totalconsumption", response_model=Create)
def create_monetaryluck(totalconsumption:Create, 
                       totalconsumption_db: Session = Depends(get_totalconsumptiondb)):
    
    create = Totalconsumption_model(userid=totalconsumption.userid,
        classifyid=totalconsumption.classifyid,
        content=totalconsumption.content)

    insert_data(totalconsumption_db, create)

    return create