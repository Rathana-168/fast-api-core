from datetime import timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel.ext.asyncio.session import AsyncSession

from app import settings
from app.core.database import get_session

from .models import UserModel, User
from .jwt import authenticate_user, create_access_token, get_current_active_user, get_password_hash
from .schemas import RegisterUserResponse, RegisterUserSchema, Token

router = APIRouter()

@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db_session: AsyncSession = Depends(get_session)
) -> Token:
    user = await authenticate_user(db_session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me/", response_model=UserModel)
async def read_users_me(
    current_user: Annotated[UserModel, Depends(get_current_active_user)]
):
    return current_user


@router.post('/create-user', response_model=RegisterUserResponse)
async def create_user(
    user: RegisterUserSchema, 
    db: AsyncSession = Depends(get_session)
):
    new_user = User(**user.model_dump())
    new_user.hashed_password = get_password_hash(user.password)
    db.sync_session.add(new_user)
    await db.commit()
    
    return RegisterUserResponse.model_validate(user.model_dump())