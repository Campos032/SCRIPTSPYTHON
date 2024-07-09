from typing import Dict
from app.models.settings.connect import db_connection_handler
from app.models.entities.users import Users
from app.models.entities.tasks import Tasks
from app.models.entities.user_task_association import UserTaskAssociation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from app.errors.error_handler import HttpConflictError


class UserTaskAssociationRepository:
    def register_user_to_task(self, user_task_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                user_id = user_task_info.get("user_id")
                task_id = user_task_info.get("task_id")

                # Verificar se o usuário e a tarefa existem
                user = database.session.query(Users).filter_by(user_id=user_id).first()
                task = database.session.query(Tasks).filter_by(task_id=task_id).first()

                if not user:
                    raise NoResultFound("User not found")
                if not task:
                    raise NoResultFound("Task not found")

                # Criar a associação entre usuário e tarefa
                user_task_association = UserTaskAssociation(
                    user_id=user_id,
                    task_id=task_id
                )
                database.session.add(user_task_association)
                database.session.commit()

                return user_task_info

            except IntegrityError:
                raise HttpConflictError("User already registered for this task!")
            except Exception as exception:
                database.session.rollback()
                raise exception
