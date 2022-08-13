from starlette.config import Config

config = Config('.env')

DATABASE_URL = config('DB_URL', cast=str, default='')
ACCESS_TOKEN_EXPIRE_TIME = 60
ALGORITHM= 'HS256'
SECRET_KEY = config('SECRET_KEY', cast=str, default='8324dce24672285457bfa42c007651ad')