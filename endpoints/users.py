from fastapi import APIRouter, Depends, HTTPException, status
from repositories.users import UserRepository
router = APIRouter()
from .depends import get_current_user, get_user_repository
from typing import List, Dict
from models.user import User, UserIn

@router.get('/', response_model=List)
async def read_users(users: UserRepository = Depends(get_user_repository), limit: int = 100, skip: int = 100):
    return await users.get_all(limit=limit, skip=0)

@router.post('/create', response_model=Dict)
async def create(user: UserIn, users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)

@router.patch('/update', response_model=User)
async def update(id: int, user: UserIn, users: UserRepository = Depends(get_user_repository), current_user: User = Depends(get_current_user)):
    old_user = await users.get_by_id(id=id)
    if old_user is None or old_user.email !=  current_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found user')
    return await users.update(id=id, u=user)