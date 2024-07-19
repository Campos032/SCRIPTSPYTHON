from typing import Dict, List
from app.models.settings.connect import db_connection_handler
from app.models.entities.users import Users
from app.models.entities.tasks import Tasks 
from app.models.entities.user_task_association import UserTaskAssociation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from app.errors.error_handler import HttpConflictError
from app.errors.error_handler import HttpNotFoundError


class TasksRepository:
    def insert_task(self, task_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                task = (
                    Tasks(
                        task_id=task_info.get("uuid"),
                        tarefa=task_info.get("tarefa"),
                        description=task_info.get("description"))
                    )
                database.session.add(task)
                database.session.commit()
                            
                return task_info
            
            except IntegrityError:
                raise HttpConflictError("Tarefa já cadastrado!")
            except Exception as exception:
                database.session.rollback()
                raise exception

    def edit_task(self, task_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                task_for_update = database.session.query(Tasks).filter_by(task_id=task_info["task_id"]).first()
                
                if not task_for_update:
                    raise NoResultFound("Tarefa Não Encontrada!")
                
                task_for_update.tarefa = task_info["tarefa"]
                task_for_update.description = task_info["description"]
                
                database.session.commit()
            
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_all_tasks(self):
        with db_connection_handler as database:
            tasks = database.session.query(Tasks).all()

            if not tasks:
                raise NoResultFound("Nada Encontrado!")

            return tasks
        
    def remove_task(self, task_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                task_for_remove = database.session.query(Tasks).filter_by(task_id=task_info["task_id"]).first()
                
                if not task_for_remove:
                    raise NoResultFound("Tarefa Não Encontrada!")
                
                database.session.delete(task_for_remove)
                database.session.commit()
            
            except Exception as exception:
                database.session.rollback()
                raise exception
