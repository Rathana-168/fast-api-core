from fastapi import APIRouter
from .model.state.routers import state_router

import app.workflow.model.state.models
import app.workflow.model.trigger.models
import app.workflow.model.transition.models

router = APIRouter()
router.include_router(state_router.router)
