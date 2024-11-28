from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from averageconsumption.averageconsumption_router import router as averageconsumption_router
from consumption.consumption_router import router as consumption_router
from income.income_router import router as income_router
from scholarship.scholarship_router import router as scholarship_router
from totalconsumption.totalconsumption_router import router as totalconsumption_router
from monetaryluck.monetaryluck_router import router as monetaryluck_router
from userinfo.userinfo_router import router as userinfo_router


from database import income_Base, income_engine, consumption_Base, consumption_engine, totalconsumption_Base, totalconsumption_engine, scholarship_Base, scholarship_engine, averageconsumption_Base, averageconsumption_engine, userinfo_Base, userinfo_engine, monetaryluck_Base, monetaryluck_engine
app = FastAPI()

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
totalconsumption_Base.metadata.create_all(bind=totalconsumption_engine)
scholarship_Base.metadata.create_all(bind=scholarship_engine)
averageconsumption_Base.metadata.create_all(bind=averageconsumption_engine)
userinfo_Base.metadata.create_all(bind=userinfo_engine)
monetaryluck_Base.metadata.create_all(bind=monetaryluck_engine)

app.include_router(averageconsumption_router, tags=["averageconsumption"])
app.include_router(consumption_router, tags=["consumption"])
app.include_router(income_router, tags=["income"])
app.include_router(scholarship_router, tags=["scholarship"])
app.include_router(totalconsumption_router, tags=["totalconsumption"])
app.include_router(monetaryluck_router, tags=["monetaryluck"])
app.include_router(userinfo_router, tags=["userinfo"])



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)