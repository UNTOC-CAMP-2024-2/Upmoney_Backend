from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from averageconsumption.averageconsumption_router import router as averageconsumption_router
from consumption.consumption_router import router as consumption_router
from income.income_router import router as income_router
from scholarship.scholarship_router import router as scholarship_router
from totalcategory.totalcategory_router import router as totalcategory_router
from dateconsumption.dateconsumption_router import router as dateconsumption_router
from monetaryluck.monetaryluck_router import router as monetaryluck_router
from userinfo.userinfo_router import router as userinfo_router
import sys
import os
from database import income_Base, income_engine, consumption_Base, consumption_engine, totalcategory_Base, totalcategory_engine, dateconsumption_Base, dateconsumption_engine, scholarship_Base, scholarship_engine, averageconsumption_Base, averageconsumption_engine, userinfo_Base, userinfo_engine, monetaryluck_Base, monetaryluck_engine
app = FastAPI()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

income_Base.metadata.create_all(bind=income_engine)
consumption_Base.metadata.create_all(bind=consumption_engine)
totalcategory_Base.metadata.create_all(bind=totalcategory_engine)
dateconsumption_Base.metadata.create_all(bind=dateconsumption_engine)
scholarship_Base.metadata.create_all(bind=scholarship_engine)
averageconsumption_Base.metadata.create_all(bind=averageconsumption_engine)
userinfo_Base.metadata.create_all(bind=userinfo_engine)
monetaryluck_Base.metadata.create_all(bind=monetaryluck_engine)

app.include_router(averageconsumption_router, tags=["averageconsumption"])
app.include_router(consumption_router, tags=["consumption"])
app.include_router(income_router, tags=["income"])
app.include_router(scholarship_router, tags=["scholarship"])
app.include_router(totalcategory_router, tags=["totalcategory"])
app.include_router(dateconsumption_router, tags=["dateconsumption"])
app.include_router(monetaryluck_router, tags=["monetaryluck"])
app.include_router(userinfo_router, prefix="/auth", tags=["userinfo"])



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)