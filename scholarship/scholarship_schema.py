from pydantic import BaseModel

class Create(BaseModel):
    period: str
    recipients :str
    money: str
    HowToAccept: str  
    subject: str
    qualification: str
    inquiry: str