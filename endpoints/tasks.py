from fastapi import APIRouter, Depends, HTTPException, status
from .depends import get_task_repository, get_current_user
from repositories.tasks import TaskRepository
from models.tasks import Task, TaskIn
from models.user import User
from typing import List

router = APIRouter()

@router.get('/', response_model=List[Task])
async def read_tasks(limit: int = 100, skip: int = 100, tasks: TaskRepository = Depends(get_task_repository)):
    return await tasks.list(limit=limit, skip=skip)

@router.post('/create', response_model=dict)
async def create_task(task: TaskIn, tasks: TaskRepository = Depends(get_task_repository), current_user: User = Depends(get_current_user)):
    return await tasks.create(user_id=current_user.id, t=task)

@router.patch('/update', response_model=dict)
async def update_task( id: int, task: TaskIn, tasks: TaskRepository = Depends(get_task_repository), current_user: User = Depends(get_current_user)):
    task = await tasks.get_by_id(id=id)
    if task is None or task.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    return await tasks.update(id=id, user_id=current_user.id, t=task)

@router.delete('/')
async def delete_task(id: int, tasks: TaskRepository = Depends(get_task_repository), current_user: User = Depends(get_current_user)):
    task = await tasks.get_by_id(id=id)
    if task is None or task.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    result = await tasks.delete(id=id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    return {'status': True}