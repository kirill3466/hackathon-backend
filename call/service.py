from db.core import supabase

from .models import CallCreate, CallRead, CallUpdate


def get_all():
    """
    Получить все звонки.
    """
    response = supabase.table("call").select("*").execute()
    return [CallRead(**item) for item in response.data]


def get_by_id(call_id: int):
    """
    Получить звонок по ID.
    """
    response = (
        supabase.table("call")
        .select("*")
        .eq("id", call_id)
        .execute()
    )
    return CallRead(**response.data[0]) if response.data else None


def create(call_in: CallCreate):
    """
    Создать новый звонок.
    """
    call_data = call_in.dict()
    response = supabase.table("call").insert(call_data).execute()
    return CallRead(**response.data[0])


def update(call_id: int, call_in: CallUpdate):
    """
    Обновить данные звонка по ID.
    """
    response = (
        supabase.table("call")
        .update(call_in.dict(exclude_unset=True))
        .eq("id", call_id)
        .execute()
    )
    return CallRead(**response.data[0]) if response.data else None


def delete(call_id: int):
    """
    Удалить звонок по ID.
    """
    supabase.table("call").delete().eq("id", call_id).execute()
