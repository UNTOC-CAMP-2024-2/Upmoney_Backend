from pydantic import BaseModel

class Create(BaseModel):
    userid: str
    content: int