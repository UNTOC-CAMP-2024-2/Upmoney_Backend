from sqlalchemy.orm import Session
from models import Consumption
from datetime import datetime, timedelta
from totalcategory.totalcategory_crud import update_totalcategory
from zoneinfo import ZoneInfo

def create_consumption(db: Session, user_id: int, amount: float, category: int, description: str):
    """
    소비 내역을 추가하고 totalcategory를 업데이트합니다.
    """
    current_time_kst = datetime.now(ZoneInfo("Asia/Seoul"))
    
    new_consumption = Consumption(
        user_id=user_id,
        amount=amount,
        category=category,
        description=description,
        created_at=current_time_kst
    )
    db.add(new_consumption)
    db.commit()
    db.refresh(new_consumption)



    return new_consumption

def update_consumption(db: Session, consumption_id: int, user_id: int, amount: int, category: int, description: str):
    """
    특정 소비/소득 내역을 업데이트합니다.
    """
    consumption = db.query(Consumption).filter(
        Consumption.id == consumption_id,
        Consumption.user_id == user_id
    ).first()

    if not consumption:
        raise ValueError("해당 소비/소득 내역이 존재하지 않습니다.")

    # 기존 값 업데이트
    consumption.amount = amount
    consumption.category = category
    consumption.description = description

    db.commit()
    db.refresh(consumption)

    return consumption
