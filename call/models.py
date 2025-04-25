from models import Base


class CallCreate(Base):
    id: int
    call_from: str
    call_to: int
    duration: float


class CallUpdate(Base):
    call_from: str
    call_to: int
    duration: float


class CallRead(Base):
    call_from: str
    call_to: int
    duration: float
