from app.models.settings.base import Base
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Tasks(Base):  # Herda de Base os atributos utilizados para declararmos nossas tabelas e indica para o SQLalchemy que isso é uma tabela
    __tablename__ = "tasks"
    
    task_id = Column(String, primary_key=True)
    tarefa = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=func.current_timestamp())

    users = relationship("UserTaskAssociation", back_populates="task")
    
    def __repr__(self):
        return f"Tasks [tarefa={self.tarefa}, description={self.description}, task_id={self.task_id}]"