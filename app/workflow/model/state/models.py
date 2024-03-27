from sqlmodel import SQLModel, Field, Relationship
from typing import List

class StateModel(SQLModel):
    name: str


class State(StateModel, table=True):
    __tablename__ = 'workflow_state'
    id: int | None = Field(default=None, primary_key=True)
    # transitions_source: List["Transition"] = Relationship(back_populates="source")
    # transitions_dest: List["Transition"] = Relationship(back_populates="dest")
