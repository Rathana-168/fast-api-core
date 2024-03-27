from app.base.router import BaseRouter
from .models import State
from .schemas import StateCreateSchema, StateUpdateSchema, ListStateResponse


class StateRouter(BaseRouter):
    model = State

    CREATE_SCHEMA = StateCreateSchema
    UPDATE_SCHEMA = StateUpdateSchema
    LIST_REPONSE_MODEL = ListStateResponse


state_router = StateRouter(prefix="/state", tag=["State"])
