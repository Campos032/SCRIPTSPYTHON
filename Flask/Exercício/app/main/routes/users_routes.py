from flask import Blueprint, jsonify, request
from app.http_types.http_request import HttpRequest
from app.data.users_handler import UsersHandler
from app.errors.error_handler import handler_error

users_route_bp = Blueprint("users_route", __name__)


@users_route_bp.route("/users", methods=["POST"])
def create_user():
    try:
        http_request = HttpRequest(body=request.json)
        users_handler = UsersHandler()
        http_response = users_handler.register(http_request)
        
        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        http_response = handler_error(exception)
        return jsonify(http_response.body), http_response.status_code
