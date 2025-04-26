from typing import Optional

from models import Base


class OrganizationCreate(Base):
    id: int
    name: str
    email: str
    # owner_id: Optional[int] = None


class OrganizationUpdate(Base):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    # owner_id: Optional[int] = None


class OrganizationRead(Base):
    id: int
    name: str
    email: str
    owner_id: Optional[int] = None
