from db.core import supabase

from .models import SessionCreate, SessionRead, SessionUpdate
from fastapi.encoders import jsonable_encoder


def get_all():
    """
    Получить все сессии.
    """
    response = supabase.table("session").select("*").execute()
    return [SessionRead(**item) for item in response.data]


def get_by_employee_id(employee_id: int):
    """
    Получить все сессии для конкретного сотрудника по его ID.
    """
    response = (
        supabase.table("session")
        .select("*")
        .eq("employee_id", employee_id)
        .execute()
    )
    return [SessionRead(**item) for item in response.data] if response.data else []

def get_by_id(session_id: int):
    """
    Получить сессию по ID.
    """
    response = (
        supabase.table("session")
        .select("*")
        .eq("id", session_id)
        .execute()
    )
    return SessionRead(**response.data[0]) if response.data else None


def create(session_in: SessionCreate):
    """
    Создать новую сессию.
    """
    session_data = session_in.dict()
    session_data["start_time"] = jsonable_encoder(session_data["start_time"])
    session_data["end_time"] = jsonable_encoder(session_data["end_time"])
    response = supabase.table("session").insert(session_data).execute()
    return SessionRead(**response.data[0])


def update(session_id: int, session_in: SessionUpdate):
    """
    Обновить данные сессии по ID.
    """
    session_data = session_in.dict()
    session_data["start_time"] = jsonable_encoder(session_data["start_time"])
    session_data["end_time"] = jsonable_encoder(session_data["end_time"])
    response = (
        supabase.table("session")
        .update(session_data)
        .eq("id", session_id)
        .execute()
    )
    return SessionRead(**response.data[0]) if response.data else None


def delete(session_id: int):
    """
    Удалить сессию по ID.
    """
    supabase.table("session").delete().eq("id", session_id).execute()
