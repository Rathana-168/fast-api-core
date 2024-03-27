from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


class TransitionModel(SQLModel):
    id: int | None
    source_id: int | None
    dest_id: int | None
    trigger_id: int | None
    conditions: str | None = None
    before: str | None = None
    after: str | None = None
    description: str | None = ''


class Transition(TransitionModel, table=True):
    __tablename__ = 'workflow_transition'
    id: int | None = Field(default=None, primary_key=True)
    source_id: int | None = Field(default=None, foreign_key="workflow_state.id")
    # source: Optional["State"] = Relationship(sa_relationship_kwargs=dict(foreign_keys=['Transition.source_id']))
    dest_id: int | None  = Field(default=None, foreign_key="workflow_state.id")
    # dest: Optional["State"] = Relationship(sa_relationship_kwargs=dict(foreign_keys=['Transition.dest_id']))
    trigger_id: int | None = Field(default=None, foreign_key="workflow_trigger.id")
    # trigger: Optional["Trigger"] = Relationship(back_populates="transitions")
    