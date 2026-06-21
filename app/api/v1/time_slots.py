
from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.schemas.time_slots import TimeSlot

router = APIRouter(
    prefix='/slots',
    tags=['Slots']
)

SLOTS_DB: set[TimeSlot] = set()

@router.get('', response_model=list[TimeSlot])
async def get_slots():
    '''
    Get all time slots.
    '''

    return SLOTS_DB

@router.post('', response_model=TimeSlot, status_code=201)
async def create_slot(
    start_time: datetime,
    end_time: datetime
):
    '''
    Create a new time slot
    '''

    if end_time <= start_time:
        raise HTTPException(status_code=400, detail='End date must be strictly after start_date')
    slot_id = len(SLOTS_DB) + 1
    new_tslot = TimeSlot(
        id=slot_id,
        start_time = start_time,
        end_time = end_time,
        is_booked = False,
        booked_by = None 
    )
    SLOTS_DB.add(new_tslot)

    return new_tslot