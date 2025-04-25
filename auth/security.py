from passlib.context import CryptContext

from db.core import supabase

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str):
    """
    Проверка имени пользователя и пароля через Supabase.
    """
    response = (
        supabase.table("employee")
        .select("id, username, hashed_password")
        .eq("username", username)
        .execute()
    )
    user = response.data[0] if response.data else None
    if not user or not verify_password(password, user["hashed_password"]):
        return None
    return user
