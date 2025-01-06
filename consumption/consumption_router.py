from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from consumption.consumption_crud import create_consumption
from consumption.consumption_schema import ConsumptionCreate
from totalcategory.totalcategory_crud import update_totalcategory
from dateconsumption.dateconsumption_crud import update_dateconsumption_on_input
from userinfo.userinfo_router import get_current_user
from models import Userinfo
from datetime import datetime

router = APIRouter()

@router.post("/consumption")
def save_consumption(
    amount: int,
    category: int,
    description: str,
    db: Session = Depends(get_db),
    current_user: Userinfo = Depends(get_current_user)
):
    consumption = create_consumption(
        db=db,
        user_id=current_user.id,
        amount=amount,
        category=category,
        description=description,
    )
    
    update_totalcategory(
        db=db,
        user_id=current_user.id,
        category=category,
        amount=amount
    )
    
    today_date = datetime.now().date()
    update_dateconsumption_on_input(
        db=db,
        user_id=current_user.id,
        category=category,
        amount=amount,
        date=today_date,
    )
    
    
    return {"message": "Consumption saved successfully", "data": consumption}
