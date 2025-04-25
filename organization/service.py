from db.core import supabase

from .models import OrganizationCreate, OrganizationRead, OrganizationUpdate


def get_all():
    """
    Получить все организации.
    """
    response = supabase.table("organization").select("*").execute()
    return [OrganizationRead(**item) for item in response.data]


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


def create(org_in: OrganizationCreate):
    """
    Создать новую организацию.
    """
    org_data = org_in.dict()
    response = supabase.table("organization").insert(org_data).execute()
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
