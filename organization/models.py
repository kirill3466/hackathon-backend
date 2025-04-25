from models import Base


class OrganizationCreate(Base):
    id: int
    name: str
    email: str


class OrganizationUpdate(Base):
    name: str
    email: str


class OrganizationRead(Base):
    name: str
    email: str
