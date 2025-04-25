from models import Base


class Token(Base):
    access_token: str
    token_type: str


class UserLogin(Base):
    username: str
    password: str
