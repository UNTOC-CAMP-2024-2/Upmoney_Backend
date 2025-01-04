from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship
from database import income_Base, consumption_Base, totalcategory_Base, dateconsumption_Base, scholarship_Base, averageconsumption_Base, userinfo_Base, monetaryluck_Base


# User �� ����
class Income(income_Base):
    __tablename__ = "income"

    id = Column(Integer, primary_key=True, index=True)
    userid = Column(String(255), nullable=False)
    content = Column(Integer, nullable=False)

class Consumption(consumption_Base):
    __tablename__ = "consumption"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("userinfo.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    category = Column(Integer, nullable=False)  # 0: 소득, 1~5: 소비 카테고리
    description = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship("Userinfo", back_populates="consumptions")

class Totalcategory(totalcategory_Base):
    __tablename__ = "totalcategory"
    
    id = Column(Integer, primary_key=True, index=True)
    userid = Column(String(255), nullable=False)
    category = Column(Integer, nullable=False)
    consumption = Column(Integer, nullable=False)

class Dateconsumption(dateconsumption_Base):
    __tablename__ = "dateconsumption"

    id = Column(Integer, primary_key=True, index=True)
    userid = Column(String(255), nullable=False)
    classifyid = Column(Integer, nullable=False)
    content = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    date = Column(DateTime, nullable = False)

class Scholarship(scholarship_Base):
    __tablename__ = "scholarship"

    id = Column(Integer, primary_key=True, index=True)
    period = Column(String(32), nullable=False)
    recipients = Column(String(256), nullable=False)
    money = Column(String(256), nullable=False)
    HowToAccept = Column(String(256), nullable=False)    
    subject = Column(String(256), nullable=False)
    qualification = Column(String(256), nullable=False)
    inquiry = Column(String(256), nullable=False)

class Averageconsumption(averageconsumption_Base):
    __tablename__ = "averageconsumption"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(Integer, nullable=False)
    classifyid = Column(Integer, nullable=False)
    content = Column(Integer, nullable=False)

class Userinfo(userinfo_Base):
    __tablename__ = "userinfo"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), unique=True, index=True, nullable=False)
    hashed_password = Column(String(256), nullable=False) 
    name = Column(String(256), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(256), nullable=False)
    
    consumptions = relationship("Consumption", back_populates="user")


class Monetaryluck(monetaryluck_Base):
    __tablename__ = "monetaryluck"

    id = Column(Integer, primary_key=True, index=True)
    weekid = Column(Integer, nullable=False)
    content = Column(String(256), nullable=False)