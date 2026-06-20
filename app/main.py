from fastapi import FastAPI
from app.api.v1.time_slots import router as tslots_router
from datetime import datetime

app=FastAPI(
    title='Booking Service API',
    version='1.0.0'
)

@app.get("/healthcheck")
async def root():
    return {"status" : "ok"}

app.include_router(tslots_router, prefix='/api/v1')