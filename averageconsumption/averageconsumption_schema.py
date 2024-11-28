from pydantic import BaseModel

class Create(BaseModel):
    age: int
    gender: int
    classifyid: int
    content: int