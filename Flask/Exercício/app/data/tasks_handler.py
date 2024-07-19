import uuid
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
    
    def modify_task(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        self.__tasks_repository.edit_task(body)
        
        return HttpResponse(
            body={"task_id": body["task_id"],
                  "Update": "Update successfuly!"},
            status_code=200
        )
        
    def pick_up_tasks(self):
        return self.__tasks_repository.get_all_tasks()
    
    def exclude_task(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        self.__tasks_repository.remove_task(body)
        
        return HttpResponse(
            body={"Delete": "Delete successfuly!"},
            status_code=200
        )
