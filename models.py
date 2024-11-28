from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from database import income_Base, consumption_Base, totalconsumption_Base, scholarship_Base, averageconsumption_Base, userinfo_Base, monetaryluck_Base


# User ¸ðµ¨ Á¤ÀÇ
class Income(income_Base):
    __tablename__ = "income"

    id = Column(Integer, primary_key=True, index=True)
    userid = Column(String(255), nullable=False)
    content = Column(Integer, nullable=False)

class Consumption(consumption_Base):
    __tablename__ = "consumption"

    id = Column(Integer, primary_key=True, index=True)
    userid = Column(String(255), nullable=False)
    classifyid = Column(Integer, nullable=False)
    content = Column(Integer, nullable=False)

class Totalconsumption(totalconsumption_Base):
    __tablename__ = "totalconsumption"

    id = Column(Integer, primary_key=True, index=True)
    userid = Column(String(255), nullable=False)
    classifyid = Column(Integer, nullable=False)
    content = Column(Integer, nullable=False)

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

class Averageconsumption(consumption_Base):
    __tablename__ = "averageconsumption"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(Integer, nullable=False)
    classifyid = Column(Integer, nullable=False)
    content = Column(Integer, nullable=False)

class Userinfo(userinfo_Base):
    __tablename__ = "userinfo"

    id = Column(Integer, primary_key=True, index=True)
    userid = Column(String(256), nullable=False)
    password = Column(String(32), nullable=False)
    username = Column(String(32), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Integer, nullable=False)

class Monetaryluck(monetaryluck_Base):
    __tablename__ = "monetaryluck"

    id = Column(Integer, primary_key=True, index=True)
    weekid = Column(Integer, nullable=False)
    content = Column(String(256), nullable=False)