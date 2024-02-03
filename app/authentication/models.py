from pydantic import BaseModel
from sqlmodel import SQLModel, Field
    

class UserModel(SQLModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class User(UserModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str