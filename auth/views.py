from datetime import timedelta

import jwt
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from starlette import status
from starlette.responses import Response

from employee.models import EmployeeCreate, EmployeeRead
from employee.service import create, get_by_email
from settings import JWT_SECRET_KEY

from .models import TokenFull, UserLogin, UserToken
from .security import authenticate_user, get_password_hash
from .service import create_access_token

router = APIRouter()


@router.post("/login")
async def login_for_access_token(user_login: UserLogin):
    """
    Аутентификация пользователя и выдача токена.
    """
    user = authenticate_user(user_login.email, user_login.password)
    user_data = get_by_email(user_login.email)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_data": user_data 
    }


@router.post("/validate-token", response_model=UserToken)
async def validate_token(token: TokenFull) -> bool:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token format. Expected 'Bearer <token>'"
        )
    token = token.access_token.split(' ')[1]
    payload = jwt.decode(
        jwt=token,
        key=JWT_SECRET_KEY,
        algorithms=["HS256"]
    )
    email = payload.get("sub")
    user_data = get_by_email(email)
    user_data = EmployeeRead(**dict(user_data))
    return {
        "access_token": token,
        "token_type": "bearer",
        "user_data": user_data
    }


@router.post("/sign-up", response_model=UserToken, status_code=201)
async def register_employee(employee_data: EmployeeCreate):
    """
    Регистрация нового сотрудника.
    """
    user_data = get_by_email(employee_data.email)

    employee_data.hashed_password = get_password_hash(
        employee_data.hashed_password
    )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": employee_data.email}, expires_delta=access_token_expires
    )
    user_data = create(employee_data)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_data": dict(user_data) 
    }


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
