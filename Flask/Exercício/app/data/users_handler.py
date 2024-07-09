import uuid
from app.models.repository.users_repository import UsersRepository
from app.http_types.http_request import HttpRequest
from app.http_types.http_response import HttpResponse


class UsersHandler:
    def __init__(self) -> None:
        self.__users_repository = UsersRepository()
    
    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())
        self.__users_repository.insert_user(body)
        
        return HttpResponse(
            body={"user_id": body["uuid"],
                  "Registro": "Sucesso"},
            status_code=200
        )
    