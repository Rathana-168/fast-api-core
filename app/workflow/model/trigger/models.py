from sqlmodel import SQLModel, Field, Relationship


class TriggerModel(SQLModel):
    id: int | None
    name: str


class Trigger(TriggerModel, table=True):
    __tablename__ = 'workflow_trigger'
    id: int | None = Field(default=None, primary_key=True)
    # transitions: list["Transition"] = Relationship(back_populates="trigger")
