from fastapi import FastAPI
from time_slots import TimeSlot
from datetime import datetime

app=FastAPI()

slots = []

@app.get("/healthcheck")
async def root():
    return {"status" : "ok"}

@app.get('/slots')
async def get_slots():
    return slots

@app.post('/slots/')
async def create_slot(
    start_time: datetime,
    end_time: datetime
):
    slot_id = len(slots) + 1
    new_tslot = TimeSlot(
        id=slot_id,
        start_time = start_time,
        end_time = end_time,
        is_booked = False,
        booked_by = None 
    )
    slots.append(new_tslot)

    return new_tslot