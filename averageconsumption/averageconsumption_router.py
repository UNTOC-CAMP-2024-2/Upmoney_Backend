from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from averageconsumption.averageconsumption_crud import create_record, update_record
from averageconsumption.averageconsumption_schema import AverageConsumptionCreate, AverageConsumptionUpdate, AverageConsumptionResponse
from averageconsumption.averageconsumption_crud import get_average_consumption_by_user
from userinfo.userinfo_router import get_current_user


router = APIRouter(
    prefix="/averageconsumption",
    tags=["Average Consumption"],
)

# POST 엔드포인트
@router.post("/", response_model=AverageConsumptionResponse)
def create_average_consumption(data: AverageConsumptionCreate, db: Session = Depends(get_db)):
    try:
        return create_record(db, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# PUT 엔드포인트
@router.put("/{id}", response_model=AverageConsumptionResponse)
def update_average_consumption(id: int, data: AverageConsumptionUpdate, db: Session = Depends(get_db)):
    try:
        return update_record(db, id, data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# GET - 현재 유저 데이터 기반 필터
@router.get("/")
def get_average_consumption(
    classify_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    try:
        # 데이터 처리 함수 호출
        return get_average_consumption_by_user(
            db=db,
            current_user=current_user,
            classify_id=classify_id,
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))