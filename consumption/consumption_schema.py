from pydantic import BaseModel, Field

class ConsumptionCreate(BaseModel):
    amount: int
    category: int = Field(..., ge=0, le=5)  # 0에서 5 사이의 값만 허용
    description: str
