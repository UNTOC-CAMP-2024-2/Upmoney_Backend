from pydantic import BaseModel

class Create(BaseModel):
    userid: str
    classifyid: int
    content: int