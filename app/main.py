from fastapi import FastAPI
from app.api.v1.time_slots import router as tslots_router
from datetime import datetime
from app.models.timeslots import TimeSlot, Base
from app.core.database import engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield

    await engine.dispose()
    

app=FastAPI(
    title='Booking Service API',
    version='1.0.0',
    lifespan=lifespan
)

@app.get("/healthcheck")
async def root():
    return {"status" : "ok"}

app.include_router(tslots_router, prefix='/api/v1')