from db.tasks import tasks
from datetime import datetime
from .base import BaseRepository
from models.tasks import Task, TaskIn
from typing import List

class TaskRepository(BaseRepository):

    async def create(self, user_id: int, t: TaskIn) -> dict:
        task = Task(
            user_id=user_id,
            title=t.title,
            description=t.description,
            is_active=True,
            end_time=t.end_time,
            created_at=datetime.now(),
            )
        
        values = {**task.dict()}
        values.pop('id', None)
        query = tasks.insert().values(**values)
        task.id = await self.database.execute(query=query)
        return task

    async def update(self, id: int, user_id: int, t: TaskIn) -> dict:
        task = Task(
            id=id,
            user_id=user_id,
            title=t.title,
            description=t.description,
            is_active=True,
            end_time=t.end_time,
            created_at=datetime.now(),
            )
        
        values = {**task.dict()}
        values.pop('created_at', None)
        query = tasks.update().where(tasks.c.id==id).values(**values)
        await self.database.execute(query=query)
        return task

    async def list(self, limit: int = 100, skip: int = 100) -> List[Task]:
        query = tasks.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)


    async def delete(self, id: int):
        query = tasks.delete().where(tasks.c.id==id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Task:
        query= tasks.select().where(tasks.c.id==id)
        task = await self.database.fetch_one(query=query)
        return Task.parse_obj(task)