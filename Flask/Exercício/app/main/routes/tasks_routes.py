from flask import Blueprint, jsonify, request, render_template
from app.http_types.http_request import HttpRequest
from app.data.tasks_handler import TasksHandler
from app.errors.error_handler import handler_error

tasks_route_bp = Blueprint("tasks_route", __name__)


@tasks_route_bp.route("/tasks", methods=["POST"])
def create_task():
    try:
        http_request = HttpRequest(body=request.json)
        tasks_handler = TasksHandler()
        http_response = tasks_handler.register(http_request)

        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        http_response = handler_error(exception)
        return jsonify(http_response.body), http_response.status_code

@tasks_route_bp.route("/tasks/edit", methods=["POST"])
def edit_task():
    pass

@tasks_route_bp.route("/tasks/submit", methods=["GET"])
def submit_tasks():
    try:
        tasks_handler = TasksHandler()
        tasks_data = tasks_handler.pick_up_tasks()

        return render_template("view_tasks.html", tasks_list=tasks_data)

    except Exception as exception:
        http_response = handler_error(exception)
        return jsonify(http_response.body), http_response.status_code
