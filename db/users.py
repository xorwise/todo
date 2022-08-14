from email.policy import default
import sqlalchemy as sa
from .base import metadata
import datetime

users = sa.Table(
    'users', 
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True),
    sa.Column('email', sa.String(100), primary_key=True, unique=True),
    sa.Column('name', sa.String(50)),
    sa.Column('surname', sa.String(50)),
    sa.Column('hashed_password', sa.String(200), primary_key=True),
    sa.Column('created_at', sa.DateTime, default=datetime.datetime.utcnow),
    sa.Column('categories', sa.PickleType, default=[]),
    )

