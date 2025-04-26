from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from .models import ResultCreate, ResultRead, ResultUpdate
from .service import create, delete, get_all, get_by_id, update, get_by_employee_id, get_by_employee_id_and_type


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


@router.get("/{employee_id}", response_model=list[ResultRead])
async def list_results_by_employee(employee_id: int):
    """
    Получить все результаты для конкретного сотрудника по его ID.
    """
    results = get_by_employee_id(employee_id)
    if not results:
        raise HTTPException(status_code=404, detail="Результаты для этого сотрудника не найдены")
    return results


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


@router.get("/{employee_id}/audio", response_model=list[ResultRead])
async def list_audio_results_by_employee(employee_id: int):
    """
    Получить все аудио-результаты для конкретного сотрудника по его ID.
    """
    results = get_by_employee_id_and_type(employee_id, "audio")
    if not results:
        raise HTTPException(status_code=404, detail="Аудио-результаты для этого сотрудника не найдены")
    return results


@router.get("/{employee_id}/video", response_model=list[ResultRead])
async def list_video_results_by_employee(employee_id: int):
    """
    Получить все видео-результаты для конкретного сотрудника по его ID.
    """
    results = get_by_employee_id_and_type(employee_id, "video")
    if not results:
        raise HTTPException(status_code=404, detail="Видео-результаты для этого сотрудника не найдены")
    return results


@router.get("/{employee_id}/test", response_model=list[ResultRead])
async def list_test_results_by_employee(employee_id: int):
    """
    Получить все тестовые результаты для конкретного сотрудника по его ID.
    """
    results = get_by_employee_id_and_type(employee_id, "test")
    if not results:
        raise HTTPException(status_code=404, detail="Тестовые результаты для этого сотрудника не найдены")
    return results