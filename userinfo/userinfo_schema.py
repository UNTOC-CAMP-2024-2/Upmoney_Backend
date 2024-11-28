from pydantic import BaseModel

class Create(BaseModel):
    userid: str
    password: str
    username: str
    age: int
    gender: int