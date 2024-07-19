from flask_login import login_user, logout_user, current_user
from app.models.repository.users_repository import UsersRepository
from app.http_types.http_request import HttpRequest
from werkzeug.security import check_password_hash
from app.http_types.http_response import HttpResponse


class AuthHandler:
    def __init__(self):
        self.__users_repository = UsersRepository()
        
    def login(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        user = self.__users_repository.get_user_by_email(body)
        
        if user and check_password_hash(user.password, body["password"]):
            login_user(user)
            
            return HttpResponse(
                body={"logged": True,
                      "Response": "User Successfully Logged!"},
                status_code=200
            )
        
        return HttpResponse(
            body={"logged": False,
                  "Response": "Not authorized login!"},
            status_code=401
        )
    
    def logout(self) -> HttpResponse:
        logout_user()
        
        return HttpResponse(
            body={"logged": False,
                  "Response": "User Successfully Logged Out!"},
            status_code=200
        )
    
    def check_login(self) -> HttpResponse:
        if current_user.is_authenticated:
            return HttpResponse(
                body={"logged": True},
                status_code=200
            )
        return HttpResponse(
                body={"logged": False},
                status_code=200
            )
        