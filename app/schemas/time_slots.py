from pydantic import BaseModel, model_validator, Field
from datetime import datetime
from typing import Optional

class TimeSlot(BaseModel):
    id: int
    start_time: datetime
    end_time: datetime
    is_booked : bool = False
    booked_by : str | None = Field(min_length=3, default=None)    

class TimeSlotCreate(BaseModel):
    start_time: datetime
    end_time: datetime

    @model_validator(mode='after')
    def validate_range(self) -> "TimeSlotCreate":
        if self.end_time <= self.start_time:
            raise ValueError('The start_date must precede the end_date')
        return self