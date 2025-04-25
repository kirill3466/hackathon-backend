from datetime import timedelta

from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from starlette.responses import Response

from employee.models import EmployeeCreate, EmployeeRead
from employee.service import create

from .models import UserLogin
from .security import get_password_hash, authenticate_user
from .service import create_access_token

router = APIRouter()


@router.post("/login")
async def login_for_access_token(user_login: UserLogin):
    """
    Аутентификация пользователя и выдача токена.
    """
    user = authenticate_user(user_login.username, user_login.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup", response_model=EmployeeRead, status_code=201)
async def register_employee(employee_data: EmployeeCreate):
    """
    Регистрация нового сотрудника.
    """
    employee_data.hashed_password = get_password_hash(
        employee_data.hashed_password
    )
    return create(employee_data)


@router.get("/logout")
async def logout(response: Response):
    response = RedirectResponse("/login", status_code=303)
    response.delete_cookie(key="access_token")
    return response


# @router.post("/signup")
# async def signup(email: str = Form(...), password: str = Form(...)):
#     try:
#         auth_response = supabase.auth.sign_up({
#             'email': email,
#             'password': password
#         })
#         if auth_response.user is None:
#             raise HTTPException(status_code=400, detail="Signup failed")
#         return RedirectResponse("/login", status_code=303)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
