import enum
import sqlalchemy as sa
from .base import metadata
import datetime

class MyEnum(enum.Enum):
    daily = 1
    weekly = 2
    monthly = 3


tasks = sa.Table(
    'tasks', 
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True),
    sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
    sa.Column('title', sa.String(200), primary_key=True),
    sa.Column('description', sa.String(10000)),
    sa.Column('is_active', sa.Boolean, default=True),
    sa.Column('end_time', sa.DateTime),
    sa.Column('created_at', sa.DateTime, default=datetime.datetime.utcnow),
    sa.Column('category', sa.Enum(MyEnum))
    )
