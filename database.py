from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
import os
load_dotenv()


# .env의 정보를 불러온다.
DB_HOST = os.environ.get("DB_HOST")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
INCOME_DB_NAME = os.environ.get("INCOME_DB_NAME")
CONSUMPTION_DB_NAME = os.environ.get("CONSUMPTION_DB_NAME")
TOTALCONSUMPTION_DB_NAME = os.environ.get("TOTALCONSUMPTION_DB_NAME")
SCHOLARSHIP_DB_NAME = os.environ.get("SCHOLARSHIP_DB_NAME")
AVERAGECONSUMPTION_DB_NAME = os.environ.get("AVERAGECONSUMPTION_DB_NAME")
USERINFO_DB_NAME = os.environ.get("USERINFO_DB_NAME")
MONETARYLUCK_DB_NAME = os.environ.get("MONETARYLUCK_DB_NAME")
DB_PORT = os.environ.get("DB_PORT", 3306)

# 어떤 DB와 연결할지 정의한다.
SQLALCHEMY_DATABASE_URL_INCOME = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{INCOME_DB_NAME}"
SQLALCHEMY_DATABASE_URL_CONSUMPTION = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{CONSUMPTION_DB_NAME}"
SQLALCHEMY_DATABASE_URL_TOTALCONSUMPTION = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{TOTALCONSUMPTION_DB_NAME}"
SQLALCHEMY_DATABASE_URL_SCHOLARSHIP = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{SCHOLARSHIP_DB_NAME}"
SQLALCHEMY_DATABASE_URL_AVERAGECONSUMPTION = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{AVERAGECONSUMPTION_DB_NAME}"
SQLALCHEMY_DATABASE_URL_USERINFO = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{USERINFO_DB_NAME}"
SQLALCHEMY_DATABASE_URL_MONETARYLUCK = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{MONETARYLUCK_DB_NAME}"

# create_engine 함수는 데이터베이스와 연결을 설정할 수 있는 엔진을 생성한다.
# 이 엔진을 통해 데이터베이스와 상호작용할 수 있다.
income_engine = create_engine(SQLALCHEMY_DATABASE_URL_INCOME)
consumption_engine = create_engine(SQLALCHEMY_DATABASE_URL_CONSUMPTION)
totalconsumption_engine = create_engine(SQLALCHEMY_DATABASE_URL_TOTALCONSUMPTION)
scholarship_engine = create_engine(SQLALCHEMY_DATABASE_URL_SCHOLARSHIP)
averageconsumption_engine = create_engine(SQLALCHEMY_DATABASE_URL_AVERAGECONSUMPTION)
userinfo_engine = create_engine(SQLALCHEMY_DATABASE_URL_USERINFO)
monetaryluck_engine = create_engine(SQLALCHEMY_DATABASE_URL_MONETARYLUCK)

# sessionmaker는 SQLAlchemy에서 세션을 관리하기 위한 함수이다.
# 세션은 데이터베이스에 대한 트랜잭션을 관리하는 객체로, 데이터베이스와의 통신을 효율적으로 처리한다.
income_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=income_engine)
consumption_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=consumption_engine)
totalconsumption_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=totalconsumption_engine)
scholarship_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=scholarship_engine)
averageconsumtion_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=averageconsumption_engine)
userinfo_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=userinfo_engine)
monetaryluck_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=monetaryluck_engine)

# declarative_base는 SQLAlchemy에서 데이터베이스의 테이블과 매핑될 클래스를 정의할 때 사용하는 기본 클래스이다. 
income_Base = declarative_base()
consumption_Base = declarative_base()
totalconsumption_Base = declarative_base()
scholarship_Base = declarative_base()
averageconsumption_Base = declarative_base()
userinfo_Base = declarative_base()
monetaryluck_Base = declarative_base()

def get_incomedb():
    db = income_SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_consumptiondb():
    db = consumption_SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_totalconsumptiondb():
    db = totalconsumption_SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_scholarshipdb():
    db = scholarship_SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_averageconsumptiondb():
    db = averageconsumtion_SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_userinfodb():
    db = userinfo_SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_monetaryluckdb():
    db = monetaryluck_SessionLocal()
    try:
        yield db
    finally:
        db.close()