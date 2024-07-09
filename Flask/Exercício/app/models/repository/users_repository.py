from typing import Dict
from app.models.settings.connect import db_connection_handler
from app.models.entities.users import Users
from app.models.entities.tasks import Tasks 
from app.models.entities.user_task_association import UserTaskAssociation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from app.errors.error_types.http_conflict import HttpConflictError


class UsersRepository:
    def insert_user(self, user_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                user = (
                    Users(
                        user_id=user_info.get("uuid"),
                        email=user_info.get("email"),
                        password=user_info.get("password"),
                        nickname=user_info.get("nickname"))
                    )
                database.session.add(user)
                database.session.commit()

                return user_info

            except IntegrityError:
                raise HttpConflictError("Email já cadastrado!")
            except Exception as exception:
                database.session.rollback()
                raise exception

    # def registry_in_task(self, task_info: Dict) -> Dict:
    #     with db_connetction_handler as database:
    #         try:
    #             user = (
    #                 Users(
    #                     user_id=user_info.get("uuid"),
    #                     email=user_info.get("email"),
    #                     password=user_info.get("password"),
    #                     nickname=user_info.get("nickname"))
    #             )
    #             database.session.add(user)
    #             database.session.commit()
    #
    #             return user_info
    #
    #         except IntegrityError:
    #             raise HttpConflictError("Email já cadastrado!")
    #         except Exception as exception:
    #             database.session.rollback()
    #             raise exception
