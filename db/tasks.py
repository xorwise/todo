import sqlalchemy as sa
from .base import metadata
import datetime
import enum



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
    )
