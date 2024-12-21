from fastapi import APIRouter, HTTPException, Depends, Response,Security

from sqlalchemy.orm import Session
from database import get_dateconsumptiondb

from .dateconsumption_schema import Create
from models import Dateconsumption as Dateconsumption
from zoneinfo import ZoneInfo

router = APIRouter(
    prefix="/dateconsumption"
)

def insert_data(db, table):
    db.add(table)
    db.commit()
    db.refresh(table)

