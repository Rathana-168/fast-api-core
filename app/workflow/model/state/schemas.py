from .models import StateModel
from typing import List

from app.base.responses import BaseResponse
from app.workflow.model.transition.models import TransitionModel


class BaseStateResponse(StateModel):
    transitions: List["TransitionModel"] = []


class StateResponse(BaseResponse):
    result: BaseStateResponse


class ListStateResponse(BaseResponse):
    result: List[BaseStateResponse]


class StateCreateResponse(BaseResponse):
    result: BaseStateResponse


class StateUpdateResponse(BaseResponse):
    result: BaseStateResponse


class StateCreateSchema(StateModel):
    pass


class StateUpdateSchema(StateCreateSchema):
    id: int
