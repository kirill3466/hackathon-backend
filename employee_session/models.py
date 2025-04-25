from datetime import datetime

from models import Base


class SessionCreate(Base):
    id: int
    start_time: datetime
    end_time: datetime
    total_calls: int
    status: bool
    employee_id: int


class SessionUpdate(Base):
    start_time: datetime
    end_time: datetime
    total_calls: int
    status: bool
    employee_id: int


class SessionRead(Base):
    start_time: datetime
    end_time: datetime
    total_calls: int
    status: bool
    employee_id: int
