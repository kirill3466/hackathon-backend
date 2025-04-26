from models import Base


class ResultCreate(Base):
    type: str
    score: float
    stress_level: str
    employee_id: int


class ResultUpdate(Base):
    type: str
    score: float
    stress_level: str | None = "Normal"
    employee_id: int


class ResultRead(Base):
    id: int
    type: str
    score: float
    stress_level: str
    employee_id: int
