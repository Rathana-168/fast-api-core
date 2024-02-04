from fastapi import Depends, HTTPException
from sqlmodel import Session
from app.core.database import get_session
from app.base.crud import BaseCRUD

from app.base.router import BaseRouter


from .models import Product
from .schemas import (
    ProductCreateResponse,
    ProductUpdateResponse,
    ProductCreateSchema,
    ProductUpdateSchema,
)


class ProductRouter(BaseRouter):
    model = Product

    CREATE_RESPONSE_MODEL = ProductCreateResponse
    UPDATE_RESPONSE_MODEL = ProductUpdateResponse

    CREATE_SCHEMA = ProductCreateSchema
    UPDATE_SCHEMA = ProductUpdateSchema


product_router = ProductRouter(prefix="/product", tag=["Product"])
