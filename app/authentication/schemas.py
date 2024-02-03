from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    
    
class RegisterUserResponse(BaseModel):
    username: str
    email: str
    full_name: str
    

class RegisterUserSchema(RegisterUserResponse):
    password: str
