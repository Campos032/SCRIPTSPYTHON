from app.models.settings.base import Base
from sqlalchemy import Column, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class UserTaskAssociation(Base):
    __tablename__ = 'user_task_association'

    user_id = Column(String(100), ForeignKey('users.user_id'), primary_key=True)
    task_id = Column(String(100), ForeignKey('tasks.task_id'), primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False, default=func.current_timestamp())

    user = relationship("Users", back_populates="tasks")
    task = relationship("Tasks", back_populates="users")
