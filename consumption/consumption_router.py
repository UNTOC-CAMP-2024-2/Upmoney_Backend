from fastapi import APIRouter, HTTPException, Depends, Response,Security

from sqlalchemy.orm import Session
from database import get_consumptiondb

from .consumption_schema import Create
from models import Consumption as Consumption_model
from zoneinfo import ZoneInfo

router = APIRouter(
    prefix="/consumption"
)

def insert_data(db, table):
    db.add(table)
    db.commit()
    db.refresh(table)

@router.post("/create_consumption", response_model=Create)
def create_consumption(consumption:Create, 
                       consumption_db: Session = Depends(get_consumptiondb)):
    
    create = Consumption_model(userid=consumption.userid,
        classifyid=consumption.classifyid,
        content=consumption.content,
        title=consumption.title,
        date=consumption.date.replace(tzinfo=ZoneInfo("UTC")).astimezone(ZoneInfo("Asia/Seoul")))

    insert_data(consumption_db, create)

    return create