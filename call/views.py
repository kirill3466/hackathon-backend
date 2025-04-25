from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from .models import CallCreate, CallRead, CallUpdate
from .service import create, delete, get_all, get_by_id, update

router = APIRouter()


@router.get("/", response_model=list[CallRead])
async def list_calls():
    """
    Получить список всех звонков.
    """
    return get_all()


@router.get("/{call_id}", response_model=CallRead)
async def get_call(call_id: int):
    """
    Получить звонок по его ID.
    """
    call = get_by_id(call_id)
    if not call:
        raise HTTPException(status_code=404, detail="Звонок не найден")
    return call


@router.post("/", response_model=CallRead, status_code=201)
async def create_call_endpoint(call_data: CallCreate):
    """
    Создать новый звонок.
    """
    return create(call_data)


@router.put("/{call_id}", response_model=CallRead)
async def update_existing_call(call_id: int, call: CallUpdate):
    """
    Обновить данные звонка по его ID.
    """
    updated_call = update(call_id, call)
    if not updated_call:
        raise HTTPException(status_code=404, detail="Звонок не найден")
    return updated_call


@router.delete("/{call_id}", status_code=204)
async def delete_call_endpoint(call_id: int):
    """
    Удалить звонок по его ID.
    """
    delete(call_id)
    return {"message": "Звонок успешно удален"}
