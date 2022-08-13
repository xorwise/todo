from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr
from datetime import datetime

class User(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    name: str
    surname: str
    hashed_password: str
    created_at: datetime

class UserIn(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: constr(min_length=6,)
    password2: str

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError("passwords don't match")
        return v