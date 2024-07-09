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

    def get_all_tasks(self):
        with db_connection_handler as database:
            tasks = database.session.query(Tasks).all()

            if not tasks:
                raise HttpNotFoundError("Nada Encontrado!")

            return tasks

            # # Converter objetos Tasks para um formato que possa ser renderizado no Jinja2
            # tasks_list = []
            # for task in tasks:
            #     task_dict = {
            #         "task_id": task.task_id,
            #         "tarefa": task.tarefa,
            #         "description": task.description,
            #         # Adicione outros atributos conforme necessário
            #     }
            #     tasks_list.append(task_dict)
            # print(tasks_list)
            # return tasks_list

    