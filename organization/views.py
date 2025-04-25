from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from .models import OrganizationCreate, OrganizationRead, OrganizationUpdate
from .service import create, delete, get_all, get_by_id, update

router = APIRouter()


@router.get("/organizations/", response_model=list[OrganizationRead])
async def list_organizations():
    """
    Получить список всех организаций.
    """
    return get_all()


@router.get("/organizations/{org_id}", response_model=OrganizationRead)
async def get_organization(org_id: int):
    """
    Получить организацию по её ID.
    """
    organization = get_by_id(org_id)
    if not organization:
        raise HTTPException(status_code=404, detail="Организация не найдена")
    return organization


@router.post(
    "/organizations/",
    response_model=OrganizationRead,
    status_code=201
)
async def create_organization_endpoint(org_data: OrganizationCreate):
    """
    Создать новую организацию.
    """
    return create(org_data)


@router.put("/organizations/{org_id}", response_model=OrganizationRead)
async def update_existing_organization(org_id: int, org: OrganizationUpdate):
    """
    Обновить данные организации по её ID.
    """
    updated_org = update(org_id, org)
    if not updated_org:
        raise HTTPException(status_code=404, detail="Организация не найдена")
    return updated_org


@router.delete("/organizations/{org_id}", status_code=204)
async def delete_organization_endpoint(org_id: int):
    """
    Удалить организацию по её ID.
    """
    delete(org_id)
    return {"message": "Организация успешно удалена"}
