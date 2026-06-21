
from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, HTTPException, Query, Depends
from app.schemas.time_slots import TimeSlot, TimeSlotCreate
from app.core.database import get_db_session

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
    tslot: TimeSlotCreate
) -> TimeSlot:
    '''
    Create a new time slot
    '''

    # if end_time <= start_time:
    #     raise HTTPException(status_code=400, detail='End date must be strictly after start_date')
    slot_id = len(SLOTS_DB) + 1
    new_tslot = TimeSlot(
        id=slot_id,
        start_time = tslot.start_time,
        end_time = tslot.end_time,
        is_booked = False,
        booked_by = None 
    )
    SLOTS_DB[slot_id] = new_tslot

    return new_tslot

async def get_slot_or_404(id: int) -> TimeSlot:
    if not id in SLOTS_DB:
        raise HTTPException(status_code=404
            ,detail='No such time slot available')

    return SLOTS_DB[id]

@router.patch('/{id}', response_model=TimeSlot)
async def book_slot(
    booked_by: Annotated[str, Query(min_length=3)],
    slot: TimeSlot = Depends(get_slot_or_404)) -> TimeSlot:
    '''
    Book a time slot
    '''
    
    slot.booked_by = booked_by
    slot.is_booked = True

    return slot

@router.delete('/{id}', status_code=204)
async def remove_timeslot(
    slot: TimeSlot = Depends(get_slot_or_404)
):
    SLOTS_DB.pop(slot.id, None)