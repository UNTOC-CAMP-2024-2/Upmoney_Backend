from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
import os
load_dotenv()


# .env�� ������ �ҷ��´�.
DB_HOST = os.environ.get("DB_HOST")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
INCOME_DB_NAME = os.environ.get("INCOME_DB_NAME")
CONSUMPTION_DB_NAME = os.environ.get("CONSUMPTION_DB_NAME")
TOTALCATEGORY_DB_NAME = os.environ.get("TOTALCATEGORY_DB_NAME")
DATECONSUMPTION_DB_NAME = os.environ.get("DATECONSUMPTION_DB_NAME")
SCHOLARSHIP_DB_NAME = os.environ.get("SCHOLARSHIP_DB_NAME")
AVERAGECONSUMPTION_DB_NAME = os.environ.get("AVERAGECONSUMPTION_DB_NAME")
USERINFO_DB_NAME = os.environ.get("USERINFO_DB_NAME")
MONETARYLUCK_DB_NAME = os.environ.get("MONETARYLUCK_DB_NAME")
DB_PORT = os.environ.get("DB_PORT", 3306)

# � DB�� �������� �����Ѵ�.
SQLALCHEMY_DATABASE_URL_INCOME = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{INCOME_DB_NAME}"
SQLALCHEMY_DATABASE_URL_CONSUMPTION = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{CONSUMPTION_DB_NAME}"
SQLALCHEMY_DATABASE_URL_TOTALCATEGORY = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{TOTALCATEGORY_DB_NAME}"
SQLALCHEMY_DATABASE_URL_DATECONSUMPTION = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATECONSUMPTION_DB_NAME}"
SQLALCHEMY_DATABASE_URL_SCHOLARSHIP = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{SCHOLARSHIP_DB_NAME}"
SQLALCHEMY_DATABASE_URL_AVERAGECONSUMPTION = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{AVERAGECONSUMPTION_DB_NAME}"
SQLALCHEMY_DATABASE_URL_USERINFO = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{USERINFO_DB_NAME}"
SQLALCHEMY_DATABASE_URL_MONETARYLUCK = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{MONETARYLUCK_DB_NAME}"

# create_engine �Լ��� �����ͺ��̽��� ������ ������ �� �ִ� ������ �����Ѵ�.
# �� ������ ���� �����ͺ��̽��� ��ȣ�ۿ��� �� �ִ�.
income_engine = create_engine(SQLALCHEMY_DATABASE_URL_INCOME)
consumption_engine = create_engine(SQLALCHEMY_DATABASE_URL_CONSUMPTION)
totalcategory_engine = create_engine(SQLALCHEMY_DATABASE_URL_TOTALCATEGORY)
dateconsumption_engine = create_engine(SQLALCHEMY_DATABASE_URL_DATECONSUMPTION)
scholarship_engine = create_engine(SQLALCHEMY_DATABASE_URL_SCHOLARSHIP)
averageconsumption_engine = create_engine(SQLALCHEMY_DATABASE_URL_AVERAGECONSUMPTION)
userinfo_engine = create_engine(SQLALCHEMY_DATABASE_URL_USERINFO)
monetaryluck_engine = create_engine(SQLALCHEMY_DATABASE_URL_MONETARYLUCK)

# sessionmaker�� SQLAlchemy���� ������ �����ϱ� ���� �Լ��̴�.  ����
# ������ �����ͺ��̽��� ���� Ʈ������� �����ϴ� ��ü��, �����ͺ��̽����� ����� ȿ�������� ó���Ѵ�.
income_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=income_engine)
consumption_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=consumption_engine)
totalcategory_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=totalcategory_engine)
dateconsumption_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=dateconsumption_engine)
scholarship_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=scholarship_engine)
averageconsumtion_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=averageconsumption_engine)
userinfo_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=userinfo_engine)
monetaryluck_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=monetaryluck_engine)

# declarative_base�� SQLAlchemy���� �����ͺ��̽��� ���̺��� ���ε� Ŭ������ ������ �� ����ϴ� �⺻ Ŭ�����̴�. 
income_Base = declarative_base()
consumption_Base = declarative_base()
totalcategory_Base = declarative_base()
dateconsumption_Base = declarative_base()
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

def get_totalcategorydb():
    db = totalcategory_SessionLocal()
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
        
def get_dateconsumptiondb():
    db = dateconsumption_SessionLocal()
    try:
        yield db
    finally:
        db.close()