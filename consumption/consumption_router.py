from fastapi import APIRouter, Depends, HTTPException, status, Body, Header
from sqlalchemy.orm import Session
from database import get_db
from consumption.consumption_crud import create_consumption, update_consumption, delete_consumption
from consumption.consumption_schema import ConsumptionCreate
from totalcategory.totalcategory_crud import update_totalcategory
from dateconsumption.dateconsumption_crud import update_dateconsumption_on_input
from userinfo.userinfo_router import get_current_user
from models import Userinfo, Consumption
from datetime import datetime
from zoneinfo import ZoneInfo

router = APIRouter()

@router.post("/consumption")
def save_consumption(
    amount: int = Body(...),
    category: int = Body(...),
    description: str = Body(...),
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
    
    today_date = datetime.now(ZoneInfo("Asia/Seoul")).date()
    update_dateconsumption_on_input(
        db=db,
        user_id=current_user.id,
        category=category,
        amount=amount,
        date=today_date,
    )
    
    
    return {"message": "Consumption saved successfully", "data": consumption}


@router.get("/consumption/recent")
def get_recent_consumptions(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    consumptions = (
        db.query(Consumption)
        .filter(Consumption.user_id == current_user.id)
        .order_by(Consumption.created_at.desc())
        .limit(5)
        .all()
    )
    return [
        {
            "id": c.id,
            "amount": c.amount,
            "category": c.category,
            "description": c.description,
            "created_at": c.created_at.astimezone(ZoneInfo("Asia/Seoul"))
        } for c in consumptions
    ]

@router.get("/consumption/recentone")
def get_recent_consumptions(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    consumptions = (
        db.query(Consumption)
        .filter(Consumption.user_id == current_user.id)
        .order_by(Consumption.created_at.desc())
        .limit(1)
        .all()
    )
    return [
        {
            "id": c.id,
            "amount": c.amount,
            "category": c.category,
            "description": c.description,
            "created_at": c.created_at.astimezone(ZoneInfo("Asia/Seoul"))
        } for c in consumptions
    ]


@router.put("/consumption/{consumption_id}")
def update_consumption_entry(
    consumption_id: int,
    amount: int = Body(...),
    category: int = Body(...),
    description: str = Body(...),
    db: Session = Depends(get_db),
    current_user: Userinfo = Depends(get_current_user)
):
    """
    소비/소득 내역을 업데이트합니다.
    """
    try:
        updated_consumption = update_consumption(
            db=db,
            consumption_id=consumption_id,
            user_id=current_user.id,
            amount=amount,
            category=category,
            description=description
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    return {
        "message": "Consumption updated successfully",
        "data": {
            "id": updated_consumption.id,
            "amount": updated_consumption.amount,
            "category": updated_consumption.category,
            "description": updated_consumption.description,
            "created_at": updated_consumption.created_at.astimezone(ZoneInfo("Asia/Seoul")),
        }
    }

@router.get("/consumption/most_recent_consumption")
def get_most_recent_consumption(
    db: Session = Depends(get_db),
    current_user: Userinfo = Depends(get_current_user)
):
    """
    가장 최근 소비 내역을 반환합니다.
    """
    # 최신 순으로 데이터를 가져오며, 카테고리가 0(소득)이 아닌 데이터 필터링
    consumptions = (
        db.query(Consumption)
        .filter(
            Consumption.user_id == current_user.id, 
            Consumption.category != 0  # 소득 제외
        )
        .order_by(Consumption.created_at.desc())  # 최신순 정렬
        .limit(1)  # 가장 최근 데이터 하나만 가져오기
        .all()
    )

    if not consumptions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No recent consumption found"
        )

    # 반환 데이터
    most_recent = consumptions[0]
    return {
        "id": most_recent.id,
        "amount": most_recent.amount,
        "category": most_recent.category,
        "description": most_recent.description,
        "created_at": most_recent.created_at.astimezone(ZoneInfo("Asia/Seoul")),
    }
    
@router.delete("/consumption/{consumption_id}")
def delete_consumption_entry(
    consumption_id: int,
    db: Session = Depends(get_db),
    current_user: Userinfo = Depends(get_current_user)
):
    """
    소비/소득 내역을 삭제합니다.
    """
    try:
        delete_consumption(
            db=db,
            consumption_id=consumption_id,
            user_id=current_user.id
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    return {"message": "Consumption deleted successfully"}
