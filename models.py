from datetime import datetime

from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        from_attributes = True


class JSONEncoderMixin(Base):
    """
    Миксин для автоматической сериализации datetime и других типов.
    """
    class Config:
        json_encoders = {
            datetime: lambda dt: dt.isoformat()
        }
