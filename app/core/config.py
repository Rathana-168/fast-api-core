from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Base
    api_v1_prefix: str
    debug: bool
    project_name: str
    version: str
    description: str
    
    # Secret Key
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Database
    SERVER: str
    PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str