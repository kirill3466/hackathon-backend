from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from .models import SessionCreate, SessionRead, SessionUpdate
from .service import create, delete, get_all, get_by_employee_id, get_by_id, update

router = APIRouter()


@router.get("/", response_model=list[SessionRead])
async def list_sessions():
    """
    Получить список всех сессий.
    """
    return get_all()


@router.get("/{employee_id}", response_model=list[SessionRead])
async def list_sessions_by_employee(employee_id: int):
    """
    Получить все сессии для конкретного сотрудника по его ID.
    """
    sessions = get_by_employee_id(employee_id)
    if not sessions:
        raise HTTPException(status_code=404, detail="Сессии для этого сотрудника не найдены")
    return sessions


@router.get("/{session_id}", response_model=SessionRead)
async def get_session(session_id: int):
    """
    Получить сессию по её ID.
    """
    session = get_by_id(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Сессия не найдена")
    return session


@router.post("/", response_model=SessionRead, status_code=201)
async def create_session_endpoint(session_data: SessionCreate):
    """
    Создать новую сессию.
    """
    return create(session_data)


@router.put("/{session_id}", response_model=SessionRead)
async def update_existing_session(session_id: int, session: SessionUpdate):
    """
    Обновить данные сессии по её ID.
    """
    updated_session = update(session_id, session)
    if not updated_session:
        raise HTTPException(status_code=404, detail="Сессия не найдена")
    return updated_session


@router.delete("/{session_id}", status_code=204)
async def delete_session_endpoint(session_id: int):
    """
    Удалить сессию по её ID.
    """
    delete(session_id)
    return {"message": "Сессия успешно удалена"}
