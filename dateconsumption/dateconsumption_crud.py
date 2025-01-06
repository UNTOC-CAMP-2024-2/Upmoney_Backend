from sqlalchemy.orm import Session
from models import Dateconsumption, Consumption
from sqlalchemy.sql import func

def update_dateconsumption_on_input(db: Session, user_id: int, category: int, amount: int, date: str):
    """
    소비/소득 입력 시 자동으로 dateconsumption 테이블 업데이트.
    """
    existing_entry = (
        db.query(Dateconsumption)
        .filter(
            Dateconsumption.user_id == user_id,
            Dateconsumption.date == date,
        )
        .first()
    )

    if not existing_entry:
        # 새로운 날짜에 대한 데이터 추가
        new_entry = Dateconsumption(
            user_id=user_id,
            date=date,
            total_income=amount if category == 0 else 0,
            total_consumption=amount if category != 0 else 0,
        )
        db.add(new_entry)
    else:
        # 기존 데이터 업데이트
        if category == 0:
            existing_entry.total_income += amount
        else:
            existing_entry.total_consumption += amount

    db.commit()
