from db.core import supabase

from .models import OrganizationCreate, OrganizationRead, OrganizationUpdate


def get_all():
    """
    Получить все организации.
    """
    response = supabase.table("organization").select("*").execute()
    return [OrganizationRead(**item) for item in response.data]


def join_org_by_id(employee_id: int, org_id: int):
    """
    Подключить сотрдуника к орге
    """
    response =  (
        supabase.table("employee")
        .update({"organization_id": org_id})
        .eq("id", employee_id)
        .execute()
    )
    return response


def get_by_id(org_id: int):
    """
    Получить организацию по ID.
    """
    response = (
        supabase.table("organization")
        .select("*")
        .eq("id", org_id)
        .execute()
    )
    return OrganizationRead(**response.data[0]) if response.data else None


def create(org_in: OrganizationCreate, owner_id: int):
    """
    Создать новую организацию.
    """
    org_data = org_in.dict(exclude_unset=True)
    org_data["owner_id"] = owner_id
    response = supabase.table("organization").insert(org_data).execute()
    
    if not response.data:
        raise ValueError("Ошибка при создании организации")
    
    return OrganizationRead(**response.data[0])


def update(org_id: int, org_in: OrganizationUpdate):
    """
    Обновить данные организации по ID.
    """
    response = (
        supabase.table("organization")
        .update(org_in.dict(exclude_unset=True))
        .eq("id", org_id)
        .execute()
    )
    return OrganizationRead(**response.data[0]) if response.data else None


def delete(org_id: int):
    """
    Удалить организацию по ID.
    """
    supabase.table("organization").delete().eq("id", org_id).execute()
