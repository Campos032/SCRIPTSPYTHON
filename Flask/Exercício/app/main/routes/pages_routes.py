from flask import Blueprint, render_template
from app.data.tasks_handler import TasksHandler
from app.data.auth_handler import AuthHandler
from flask_login import login_required
from app.errors.error_handler import handler_error


pages_route_bp = Blueprint("pages_route", __name__)


@pages_route_bp.route("/")
@pages_route_bp.route("/home")
def home_page():
    auth_handler = AuthHandler()
    http_response = auth_handler.check_login()
    tasks_handler = TasksHandler()
    tasks = tasks_handler.pick_up_tasks()
    
    return render_template("home.html", logged=http_response.body["logged"], tasks=tasks)


@pages_route_bp.route("/login&register")
def login_register_page():
    return render_template("login&register.html")


@login_required
@pages_route_bp.route("/view-tasks")
def view_tasks_page():
    try:
        tasks_handler = TasksHandler()
        tasks_data = tasks_handler.pick_up_tasks()

        return render_template("view_tasks.html")

    except Exception as exception:
        http_response = handler_error(exception)
        return render_template("error.html")
