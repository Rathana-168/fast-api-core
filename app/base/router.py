from fastapi import APIRouter
from app.interface.crud import CRUDInterface


class BaseRouter(CRUDInterface):
    model = None
    
    CREATE_RESPONSE_MODEL = None
    UPDATE_RESPONSE_MODEL = None
    LIST_REPONSE_MODEL = None
    READ_RESPONSE_MODEL = None
    DELETE_REPONSE_MODEL = None
    
    CREATE_SCHEMA = None
    UPDATE_SCHEMA = None

    def __init__(self, prefix: str = "", tag: str = None):
        self.router = APIRouter(prefix=prefix, tags=tag)
        self.initial_endpoint()
        
        
    def initial_endpoint(self):
        self.router.add_api_route("/", self.list, methods=["GET"], response_model=self.LIST_REPONSE_MODEL)
        self.router.add_api_route("/{id}", self.read, methods=["GET"], response_model=self.READ_RESPONSE_MODEL)
        self.router.add_api_route("/", self.create, methods=["POST"], response_model=self.CREATE_RESPONSE_MODEL)
        self.router.add_api_route("/{id}", self.update, methods=["PUT"], response_model=self.UPDATE_RESPONSE_MODEL)
        self.router.add_api_route("/{id}", self.delete, methods=["DELETE"], response_model=self.DELETE_REPONSE_MODEL)
