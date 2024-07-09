import uuid
from typing import List
from app.models.repository.tasks_repository import TasksRepository
from app.http_types.http_request import HttpRequest
from app.http_types.http_response import HttpResponse


class TasksHandler:
    def __init__(self) -> None:
        self.__tasks_repository = TasksRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())
        self.__tasks_repository.insert_task(body)

        return HttpResponse(
            body={"task_id": body["uuid"],
                  "Registro": "Sucesso"},
            status_code=200
        )
    
    def pick_up_tasks(self):
        return self.__tasks_repository.get_all_tasks()
