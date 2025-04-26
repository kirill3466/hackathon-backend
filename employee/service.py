from db.core import supabase
from .models import EmployeeCreate, EmployeeUpdate, EmployeeRead


def get_all():
    """
    Получить всех сотрудников.
    """
    response = supabase.table("employee").select("*").execute()
    return [EmployeeRead(**item) for item in response.data]


def get_by_id(employee_id: int):
    """
    Получить сотрудника по ID.
    """
    response = (
        supabase.table("employee")
        .select("*")
        .eq("id", employee_id)
        .execute()
    )
    return EmployeeRead(**response.data[0]) if response.data else None


def get_by_username(username: str):
    """
    Получить сотрудника по username.
    """
    response = (
        supabase.table("employee")
        .select("*")
        .eq("username", username)
        .execute()
    )
    return EmployeeRead(**response.data[0]) if response.data else None


def get_by_email(email: str):
    """
    Получить сотрудника по email.
    """
    response = (
        supabase.table("employee")
        .select("*")
        .eq("email", email)
        .execute()
    )
    return EmployeeRead(**response.data[0]) if response.data else None


def create(employee_in: EmployeeCreate):
    """
    Создать нового сотрудника.
    """
    employee_data = employee_in.dict()
    response = supabase.table("employee").insert(employee_data).execute()
    return EmployeeRead(**response.data[0])


def update(employee_id: int, employee_in: EmployeeUpdate):
    """
    Обновить данные сотрудника по ID.
    """
    response = (
        supabase.table("employee")
        .update(employee_in.dict(exclude_unset=True))
        .eq("id", employee_id)
        .execute()
    )
    return EmployeeRead(**response.data[0]) if response.data else None


def delete(employee_id: int):
    """
    Удалить сотрудника по ID.
    """
    supabase.table("employee").delete().eq("id", employee_id).execute()
