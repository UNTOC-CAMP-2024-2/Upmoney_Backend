from pydantic import BaseModel

class Create(BaseModel):
    weekid: int
    content: str