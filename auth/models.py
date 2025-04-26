from models import Base
from employee.models import EmployeeRead

class Token(Base):
    access_token: str
    token_type: str


class TokenFull(Base):
    access_token: str


class UserLogin(Base):
    email: str
    password: str


class UserToken(Base):
    access_token: str
    token_type: str
    user_data: EmployeeRead