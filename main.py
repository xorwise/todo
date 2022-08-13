from fastapi import FastAPI
import uvicorn
from db.base import database
from endpoints.users import router
from endpoints.auth import router as auth_router
from endpoints.tasks import router as task_router



app = FastAPI(title='ToDo')
app.include_router(router, prefix='/users', tags=['users'])
app.include_router(auth_router, prefix='/auth', tags=['auth'])
app.include_router(task_router, prefix='/tasks', tags=['tasks'])

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)