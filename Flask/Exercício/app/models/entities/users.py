from app.models.settings.base import Base
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from flask_login import UserMixin


class Users(Base, UserMixin):
    __tablename__ = "users"
    
    user_id = Column(String, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    nickname = Column(String, unique=True)
    created_at = Column(TIMESTAMP, default=func.current_timestamp())

    tasks = relationship("UserTaskAssociation", back_populates="user")
    
    def get_id(self):
        return self.user_id
    
    def __repr__(self):
        return f"Users [nickname={self.nickname}, email={self.email}, user_id={self.user_id}"
