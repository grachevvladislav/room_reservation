from datetime import datetime

from pydantic import BaseModel, validator, root_validator


class ReservationBase(BaseModel):
    from_reserve: datetime
    to_reserve: datetime


class MeetingRoomUpdate(ReservationBase):
    pass

    @validator('from_reserve')
    def name_cant_be_numeric(cls, value: str):
        if value <= datetime.now():
            raise ValueError(
                'Время начала бронирования '
                'не может быть меньше текущего времени'
            )
        return value

    @root_validator(skip_on_failure=True)
    def to_grate_than_from(cls, values):
        if values['from_reserve'] >= values['to_reserve']:
            raise ValueError(
                'Время начала бронирования '
                'не может быть больше времени окончания'
            )
        return values


class ReservationCreate(MeetingRoomUpdate):
    meetingroom_id: int


class MeetingRoomDB(ReservationBase):
    id: int
    meetingroom_id: int

    class Config:
        orm_mode = True
