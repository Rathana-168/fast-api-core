from pydantic import BaseModel
from typing import Any

class BaseResponse(BaseModel):
    status_code: int = 200
    message: str | None = ''
    total_result: int | None = 0
    result: Any