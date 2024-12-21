from pydantic import BaseModel
from datetime import datetime

class Create(BaseModel):
    userid: str
    classifyid: int
    content: int
    title: str
    date: datetime