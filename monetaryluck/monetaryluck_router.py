from fastapi import APIRouter, HTTPException, Depends, Response,Security

from sqlalchemy.orm import Session
from database import get_monetaryluckdb

from .monetaryluck_schema import Create
from models import Monetaryluck as Monetaryluck_model

router = APIRouter(
    prefix="/monetaryluck"
)

def insert_data(db, table):
    db.add(table)
    db.commit()
    db.refresh(table)

@router.post("/create_monetaryluck", response_model=Create)
def create_monetaryluck(monetaryluck:Create, 
                       monetaryluck_db: Session = Depends(get_monetaryluckdb)):
    
    create = Monetaryluck_model(
        monetaryluck_weekid=monetaryluck.weekid,
        monetaryluck_content=monetaryluck.content)

    insert_data(monetaryluck_db, create)

    return create