from sqlmodel import SQLModel
from datetime import datetime


class AuditMixin(SQLModel):
    created_on: datetime = datetime.now()
    created_by: str | None = None
    modified_on: datetime | None = None
    modified_by: str | None = None
    active: bool | None = True