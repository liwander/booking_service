from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Optional

class TimeSlot(BaseModel):
    id: int
    start_time: datetime
    end_time: datetime
    is_booked : bool = False
    booked_by : Optional[datetime] = None

    @model_validator(mode='after')
    def validate_range(self) -> "TimeSlot":
        if self.end_time < self.start_time:
            raise ValueError('The start_date must precede the end_date')
        return self

    def __hash__(self):
        return hash((self.id, self.booked_by))

    def __eq__(self, other):
        if not isinstance(other, TimeSlot):
            return NotImplemented
        return self.id == other.id and self.id == other.booked_by
    