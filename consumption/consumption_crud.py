from sqlalchemy.orm import Session
from models import Consumption
from datetime import datetime, timedelta
from totalcategory.totalcategory_crud import update_totalcategory

def create_consumption(db: Session, user_id: int, amount: float, category: int, description: str):
    """
    소비 내역을 추가하고 totalcategory를 업데이트합니다.
    """
    new_consumption = Consumption(
        user_id=user_id,
        amount=amount,
        category=category,
        description=description,
        created_at=datetime.utcnow()
    )
    db.add(new_consumption)
    db.commit()
    db.refresh(new_consumption)



    return new_consumption