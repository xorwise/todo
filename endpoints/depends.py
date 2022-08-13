from core.security import JWTBearer, decode_access_token
from repositories.users import UserRepository
from db.base import database
from models.user import User
from fastapi import Depends, HTTPException, status
from repositories.tasks import TaskRepository

def get_user_repository() -> UserRepository:
    return UserRepository(database)

def get_task_repository() -> TaskRepository:
    return TaskRepository(database)

async def get_current_user(users: UserRepository = Depends(get_user_repository), token: str = Depends(JWTBearer())) -> User:
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Credentials are invalid')
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception
    email: str = payload.get('sub')
    user = await users.get_by_email(email=email)
    if user is None:
        raise cred_exception
    return user