from sqlalchemy.orm import Session
from models import Averageconsumption, Dateconsumption
from fastapi import HTTPException
from averageconsumption.averageconsumption_schema import AverageConsumptionCreate, AverageConsumptionUpdate
from datetime import datetime, timedelta

# POST - 새 데이터 생성
def create_record(db: Session, data: AverageConsumptionCreate):
    new_record = Averageconsumption(
        age=data.age,
        gender=data.gender,
        classify_id=data.classify_id,
        content=data.content
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

# PUT - 기존 데이터 수정
def update_record(db: Session, record_id: int, data: AverageConsumptionUpdate):
    record = db.query(Averageconsumption).filter(Averageconsumption.id == record_id).first()
    if not record:
        raise ValueError("Record not found")
    record.age = data.age
    record.gender = data.gender
    record.classify_id = data.classify_id
    record.content = data.content

    db.commit()
    db.refresh(record)
    return record

# GET - 현재 유저의 데이터를 기반으로 값을 계산
def get_average_consumption_by_user(
    db: Session,
    current_user,
    classify_id: int,
):
    # 나이대 계산 (20, 30, 40 등)
    age_group = (current_user.age // 10) * 10

    # Averageconsumption에서 조건에 맞는 데이터 조회
    avg_consumption = db.query(Averageconsumption).filter(
        Averageconsumption.gender == current_user.gender,
        Averageconsumption.age == age_group,
        Averageconsumption.classify_id == classify_id,
    ).first()

    if not avg_consumption:
        raise HTTPException(status_code=404, detail="No average consumption data found")

    # Dateconsumption에서 현재 유저의 최신 데이터 조회
    date_consumption = (
        db.query(Dateconsumption)
        .filter(Dateconsumption.user_id == current_user.id)
        .order_by(Dateconsumption.date.desc())
        .first()
    )

    if not date_consumption:
        raise HTTPException(status_code=404, detail="No date consumption data found for the user")

    # classify_id에 따른 값 계산
    if classify_id == 0:
        result = avg_consumption.content - date_consumption.total_income
    else:
        result = avg_consumption.content - date_consumption.total_consumption

    # 결과 반환
    return {
        "gender": current_user.gender,
        "age_group": age_group,
        "classify_id": classify_id,
        "difference": result,
    }