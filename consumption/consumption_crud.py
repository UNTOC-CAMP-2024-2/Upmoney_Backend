from sqlalchemy.orm import Session
from models import Consumption
from datetime import datetime, timedelta

def create_consumption(db: Session, user_id: int, amount: float, category: int, description: str):
    # 현재 UTC 시간에 +9시간을 더해 KST로 설정
    current_time_kst = datetime.utcnow() + timedelta(hours=9)

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
