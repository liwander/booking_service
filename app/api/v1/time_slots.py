
from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, HTTPException, Query
from app.schemas.time_slots import TimeSlot

router = APIRouter(
    prefix='/slots',
    tags=['Slots']
)

SLOTS_DB: dict[int, TimeSlot] = dict()

@router.get('', response_model=list[TimeSlot])
async def get_slots():
    '''
    Get all time slots.
    '''

    return SLOTS_DB.values()

@router.post('', response_model=TimeSlot, status_code=201)
async def create_slot(
    start_time: datetime,
    end_time: datetime
) -> TimeSlot:
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
    SLOTS_DB[slot_id] = new_tslot

    return new_tslot

@router.patch('', response_model=TimeSlot)
async def book_slot(
    id: int,
    booked_by: Annotated[str, Query(min_length=3)]) -> TimeSlot:
    '''
    Book a time slot
    '''

    check_if_slots_exists(id, SLOTS_DB)
    
    SLOTS_DB[id].booked_by = booked_by
    SLOTS_DB[id].is_booked = True

    return SLOTS_DB[id]

@router.delete('', status_code=204)
async def remove_timeslot(id: int):
    check_if_slots_exists(id, SLOTS_DB)

    SLOTS_DB.pop(id, None)

def check_if_slots_exists(id: int, db: dict[int, TimeSlot]):
    if not id in db:
        raise HTTPException(status_code=404
            ,detail='No such time slot available')