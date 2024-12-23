from pydantic import BaseModel

class Create(BaseModel):
    userid: str
    category: int
    sumconsumption: int