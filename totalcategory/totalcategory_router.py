from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter()

@router.put("/update_from_consumption/{user_id}")
def update_from_consumption(user_id: int, db: Session = Depends(get_db)):
    pass
