from datetime import datetime, timedelta

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import (
    OAuth2PasswordBearer,
)

from db.core import supabase
from employee.service import get_by_email
from settings import JWT_ALGO, JWT_SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGO)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGO])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    response = get_by_email(email)
    user = response.data[0] if response.data else None
    if user is None:
        raise credentials_exception
    return user


# def get_current_user(
#         credentials: HTTPAuthorizationCredentials = Depends(security)
# ):
#     try:
#         token = credentials.credentials
#         # Remove 'Bearer ' prefix if present
#         if token.startswith("Bearer "):
#             token = token.split(" ")[1]
#         # Add 'options' parameter to ignore audience claim
#         payload = jwt.decode(
#             token,
#             SUPABASE_JWT_SECRET,
#             algorithms=['HS256'],
#             options={"verify_aud": False}
#         )
#         user_id = payload.get('sub')
#         if user_id is None:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Invalid authentication credentials"
#             )
#         return payload
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Token has expired"
#         )
#     except jwt.PyJWTError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Could not validate credentials"
#         )
