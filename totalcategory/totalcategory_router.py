from fastapi import APIRouter, HTTPException, Depends, Response,Security

from sqlalchemy.orm import Session
from database import get_db

from .totalcategory_schema import Create
from models import Totalcategory as Totalcategory_model

router = APIRouter(
    prefix="/totalcategory"
)

def insert_data(db, table):
    db.add(table)
    db.commit()
    db.refresh(table)
    

@router.put("/update_totalcategory", response_model=Create)
def create_monetaryluck(totalcategory:Create, 
                       totalcategory_db: Session = Depends(get_db)):
    
    create = Totalcategory_model(userid=totalcategory.userid,
        classifyid=totalcategory.classifyid,
        content=totalcategory.content)

    insert_data(totalcategory_db, create)

    return create