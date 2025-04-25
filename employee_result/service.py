from db.core import supabase

from .models import ResultCreate, ResultRead, ResultUpdate


def get_all():
    """
    Получить все результаты.
    """
    response = supabase.table("result").select("*").execute()
    return [ResultRead(**item) for item in response.data]


def get_by_id(result_id: int):
    """
    Получить результат по ID.
    """
    response = (
        supabase.table("result")
        .select("*")
        .eq("id", result_id)
        .execute()
    )
    return ResultRead(**response.data[0]) if response.data else None


def create(result_in: ResultCreate):
    """
    Создать новый результат.
    """
    result_data = result_in.dict()
    response = supabase.table("result").insert(result_data).execute()
    return ResultRead(**response.data[0])


def update(result_id: int, result_in: ResultUpdate):
    """
    Обновить данные результата по ID.
    """
    response = (
        supabase.table("result")
        .update(result_in.dict(exclude_unset=True))
        .eq("id", result_id)
        .execute()
    )
    return ResultRead(**response.data[0]) if response.data else None


def delete(result_id: int):
    """
    Удалить результат по ID.
    """
    supabase.table("result").delete().eq("id", result_id).execute()
