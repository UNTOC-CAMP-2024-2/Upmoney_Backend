from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from consumption.consumption_crud import create_consumption
from consumption.consumption_schema import ConsumptionCreate
from totalcategory.totalcategory_crud import update_totalcategory
from userinfo.userinfo_router import get_current_user
from models import Userinfo

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
    
    
    return {"message": "Consumption saved successfully", "data": consumption}
