from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Userinfo(Base):
    __tablename__ = "userinfo"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), unique=True, index=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)
    name = Column(String(256), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(256), nullable=False)

    consumptions = relationship("Consumption", back_populates="user")


class Consumption(Base):
    __tablename__ = "consumption"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("userinfo.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    category = Column(Integer, nullable=False)  # 0: ?Üå?ìù, 1~5: ?ÜåÎπ? Ïπ¥ÌÖåÍ≥†Î¶¨
    description = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    user = relationship("Userinfo", back_populates="consumptions")


class Totalcategory(Base):
    __tablename__ = "totalcategory"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("userinfo.id"), nullable=False)
    category = Column(Integer, nullable=False)
    consumption = Column(Integer, nullable=False)


class Dateconsumption(Base):
    __tablename__ = "dateconsumption"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("userinfo.id"), nullable=False)
    classify_id = Column(Integer, nullable=False)
    content = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)


class Scholarship(Base):
    __tablename__ = "scholarship"

    id = Column(Integer, primary_key=True, index=True)
    page_id = Column(Integer, nullable=False) # 0~1
    name = Column(String(255), nullable=False)
    link = Column(String(255), unique=True, nullable=False)


class Averageconsumption(Base):
    __tablename__ = "averageconsumption"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(Integer, nullable=False)
    classify_id = Column(Integer, nullable=False)
    content = Column(Integer, nullable=False)


class Monetaryluck(Base):
    __tablename__ = "monetaryluck"

    id = Column(Integer, primary_key=True, index=True)
    week_id = Column(Integer, nullable=False)
    content = Column(String(256), nullable=False)
