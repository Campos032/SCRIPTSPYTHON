from flask_login import LoginManager
from app.models.entities.users import Users
from app.models.settings.connect import db_connection_handler

login_manager = LoginManager()

login_manager.login_view = "login&register"


@login_manager.user_loader
def load_user(user_id):
    with db_connection_handler as database:
        id = database.session.query(Users).get(user_id)
        if id:
            return id
        return None
