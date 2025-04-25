from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from .models import ResultCreate, ResultRead, ResultUpdate
from .service import create, delete, get_all, get_by_id, update


router = APIRouter()


@router.get("/", response_model=list[ResultRead])
async def list_results():
    """
    Получить список всех результатов.
    """
    return get_all()


@router.get("/{result_id}", response_model=ResultRead)
async def get_result(result_id: int):
    """
    Получить результат по его ID.
    """
    result = get_by_id(result_id)
    if not result:
        raise HTTPException(status_code=404, detail="Результат не найден")
    return result


@router.post("/", response_model=ResultRead, status_code=201)
async def create_result_endpoint(result_data: ResultCreate):
    """
    Создать новый результат.
    """
    return create(result_data)


@router.put("/{result_id}", response_model=ResultRead)
async def update_existing_result(result_id: int, result: ResultUpdate):
    """
    Обновить данные результата по его ID.
    """
    updated_result = update(result_id, result)
    if not updated_result:
        raise HTTPException(status_code=404, detail="Результат не найден")
    return updated_result


@router.delete("/{result_id}", status_code=204)
async def delete_result_endpoint(result_id: int):
    """
    Удалить результат по его ID.
    """
    delete(result_id)
    return {"message": "Результат успешно удален"}
