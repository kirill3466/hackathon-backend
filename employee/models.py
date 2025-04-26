from models import Base


class EmployeeCreate(Base):
    username: str | None = None
    hashed_password: str
    organization_id: int | None = None
    name: str
    surname: str
    email: str
    phone: str
    is_active: bool | None = None
    is_ready: bool | None = None
    status: str | None = None


class EmployeeUpdate(Base):
    username: str | None = None
    hashed_password: str | None = None
    name: str | None = None
    surname: str | None = None
    email: str | None = None
    phone: str | None = None
    is_active: bool | None = None
    is_ready: bool | None = None
    status: str | None = None


class EmployeeRead(Base):
    id: int
    username: str | None = None
    name: str
    surname: str
    email: str
    phone: str
    is_active: bool | None = None
    is_ready: bool | None = None
    status: str | None = None
