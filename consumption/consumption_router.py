from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_consumptiondb
from consumption.consumption_crud import create_consumption
from consumption.consumption_schema import ConsumptionCreate
from userinfo.userinfo_router import get_current_user
from models import Userinfo

router = APIRouter()

@router.post("/")
def save_consumption(
    data: ConsumptionCreate,
    db: Session = Depends(get_consumptiondb),
    current_user: Userinfo = Depends(get_current_user),
):
    
    # 소비/소득 데이터 저장
    consumption = create_consumption(
        db=db,
        user_id=current_user.id,
        amount=data.amount,
        category=data.category,
        description=data.description
    )
    return {"message": "Data saved successfully.", "data": consumption}
