from flask import Blueprint, request, redirect, jsonify
from flask_login import login_required
from app.data.auth_handler import AuthHandler
from app.http_types.http_request import HttpRequest
from flask_login import current_user


auth_route_bp = Blueprint("auth_route", __name__)


@auth_route_bp.route("/login", methods=["POST"])
def login_page():
    http_request = HttpRequest(body=request.json)
    auth_handler = AuthHandler()
    http_response = auth_handler.login(http_request)
    
    return redirect("home")


@login_required
@auth_route_bp.route("/logout", methods=["POST"])
def logout_route():
    auth_handler = AuthHandler()
    http_response = auth_handler.logout()
    
    return redirect("home")


@auth_route_bp.route("/check-login")
def check_login():
    auth_handler = AuthHandler()
    http_response = auth_handler.check_login()
    return jsonify(http_response.body), http_response.status_code
