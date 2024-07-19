import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from app.models.settings.connect import db_connection_handler
from app.main.routes.users_routes import users_route_bp
from app.main.routes.tasks_routes import tasks_route_bp
from app.main.routes.pages_routes import pages_route_bp
from app.main.routes.auth_routes import auth_route_bp
from .flask_login import login_manager


db_connection_handler.connect_to_db()

load_dotenv()

app = Flask(__name__,
            template_folder=os.getenv("TEMPLATE_FOLDER", "C:/projetos/SCRIPTSPYTHON/Flask/Exercício/app/templates"),
            static_folder=os.getenv("STATIC_FOLDER", "C:/projetos/SCRIPTSPYTHON/Flask/Exercício/app/static"),
            )

app.config["HOST"] = os.getenv("HOST", "0.0.0.0")
app.config["PORT"] = int(os.getenv("PORT", "5000"))
app.config["DEBUG"] = os.getenv("DEBUG", "False").lower() in ["true", "1", "t", "y", "yes"]
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret_key")

login_manager.init_app(app)

CORS(app)

app.register_blueprint(users_route_bp)
app.register_blueprint(tasks_route_bp)
app.register_blueprint(pages_route_bp)
app.register_blueprint(auth_route_bp)
