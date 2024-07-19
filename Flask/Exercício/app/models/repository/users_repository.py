from typing import Dict
from app.models.settings.connect import db_connection_handler
from app.models.entities.users import Users
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from app.errors.error_types.http_conflict import HttpConflictError
from app.errors.error_types.http_not_found import HttpNotFoundError
from werkzeug.security import generate_password_hash


class UsersRepository:
    def insert_user(self, user_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                password_hesh = generate_password_hash(user_info.get("password"))
                user = (
                    Users(
                        user_id=user_info.get("uuid"),
                        email=user_info.get("email"),
                        password=password_hesh,
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

    def get_user_by_email(self, form_info: Dict) -> Users:
        try:
            with db_connection_handler as database:
                user = database.session.query(Users).filter_by(email=form_info["email"]).first()
                return user
            
        except NoResultFound:
            raise HttpNotFoundError("Email não cadastrado!")
        