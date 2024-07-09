from flask import Flask
from flask_cors import CORS
from app.models.settings.connect import db_connection_handler
from app.main.routes.users_routes import users_route_bp
from app.main.routes.tasks_routes import tasks_route_bp
# from app.main.routes.check_in_routes import check_in_route_bp

db_connection_handler.connect_to_db()

app = Flask(__name__, template_folder=r"C:\projetos\SCRIPTSPYTHON\Flask\Exercício\app\templates")
CORS(app)

app.register_blueprint(users_route_bp)
app.register_blueprint(tasks_route_bp)
# app.register_blueprint(check_in_route_bp)
