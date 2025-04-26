from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from .models import OrganizationCreate, OrganizationRead, OrganizationUpdate
from .service import create, delete, get_all, get_by_id, update, join_org_by_id

router = APIRouter()


@router.get("/", response_model=list[OrganizationRead])
async def list_organizations():
    """
    Получить список всех организаций.
    """
    return get_all()


@router.post("/join/{org_id}")
async def join_org_employee_to_org(employee_id: int , org_id: int):
    """
    Подписываем сотрудника к организации
    """
    join_org = join_org_by_id(employee_id, org_id)
    if not join_org:
        raise HTTPException(status_code=404, detail="Не удалось вступить в организацию")
    return join_org


@router.get("/{org_id}", response_model=OrganizationRead)
async def get_organization(org_id: int):
    """
    Получить организацию по её ID.
    """
    organization = get_by_id(org_id)
    if not organization:
        raise HTTPException(status_code=404, detail="Организация не найдена")
    return organization


@router.post(
    "/",
    response_model=OrganizationRead,
    status_code=201
)
async def create_organization(org_data: OrganizationCreate, user_id: int):
    """
    Создать новую организацию.
    """
    return create(org_data, user_id)


@router.put("/{org_id}", response_model=OrganizationRead)
async def update_organization(org_id: int, org: OrganizationUpdate):
    """
    Обновить данные организации по её ID.
    """
    updated_org = update(org_id, org)
    if not updated_org:
        raise HTTPException(status_code=404, detail="Организация не найдена")
    return updated_org


@router.delete("/{org_id}", status_code=204)
async def delete_organization(org_id: int):
    """
    Удалить организацию по её ID.
    """
    delete(org_id)
    return {"message": "Организация успешно удалена"}
