from fastapi import APIRouter, HTTPException

from .models import EmployeeCreate, EmployeeRead, EmployeeUpdate
from .service import create, delete, get_all, get_by_id, update

router = APIRouter()


@router.get("/", response_model=list[EmployeeRead])
async def list_employees():
    """
    Получить список всех сотрудников.
    """
    return get_all()


@router.get("/{employee_id}", response_model=EmployeeRead)
async def get_employee(employee_id: int):
    """
    Получить сотрудника по его ID.
    """
    employee = get_by_id(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")
    return employee


# @router.post("/", response_model=EmployeeRead, status_code=201)
# async def create_employee(employee_data: EmployeeCreate):
#     """
#     Создать нового сотрудника.
#     """
#     return create(employee_data)


@router.put("/{employee_id}", response_model=EmployeeRead)
async def update_existing_employee(employee_id: int, employee: EmployeeUpdate):
    """
    Обновить данные сотрудника по его ID.
    Используется модель EmployeeUpdate с частичным обновлением.
    """
    updated_employee = update(employee_id, employee)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")
    return updated_employee


@router.delete("/{employee_id}", status_code=204)
async def delete_employee(employee_id: int):
    """
    Удалить сотрудника по его ID.
    """
    delete(employee_id)
    return {"message": "Сотрудник успешно удален"}
