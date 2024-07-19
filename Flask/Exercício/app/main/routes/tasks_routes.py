from flask import Blueprint, jsonify, request, render_template
from app.http_types.http_request import HttpRequest
from app.data.tasks_handler import TasksHandler
from app.errors.error_handler import handler_error
from flask_login import login_required


tasks_route_bp = Blueprint("tasks_route", __name__)


@login_required
@tasks_route_bp.route("/tasks/create", methods=["POST"])
def create_task():
    try:
        http_request = HttpRequest(body=request.json)
        tasks_handler = TasksHandler()
        http_response = tasks_handler.register(http_request)

        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        http_response = handler_error(exception)
        return jsonify(http_response.body), http_response.status_code


@login_required
@tasks_route_bp.route("/tasks/read", methods=["GET"])
def read_tasks():
    try:
        tasks_handler = TasksHandler()
        tasks_data = tasks_handler.pick_up_tasks()

        return render_template("view_tasks.html", tasks=tasks_data)

    except Exception as exception:
        http_response = handler_error(exception)
        return jsonify(http_response.body), http_response.status_code


@login_required
@tasks_route_bp.route("/tasks/update", methods=["POST"])
def update_task():
    try:
        http_request = HttpRequest(body=request.json)
        tasks_handler = TasksHandler()
        http_response = tasks_handler.modify_task(http_request)

        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        http_response = handler_error(exception)
        return jsonify(http_response.body), http_response.status_code


@login_required
@tasks_route_bp.route("/tasks/delete", methods=["POST"])
def delete_task():
    try:
        http_request = HttpRequest(body=request.json)
        tasks_handler = TasksHandler()
        http_response = tasks_handler.exclude_task(http_request)

        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        http_response = handler_error(exception)
        return jsonify(http_response.body), http_response.status_code
