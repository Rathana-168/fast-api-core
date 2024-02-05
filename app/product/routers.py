from app.base.router import BaseRouter


from .models import Product
from .schemas import (
    ProductResponse,
    ListProductResponse,
    ProductCreateResponse,
    ProductUpdateResponse,
    ProductCreateSchema,
    ProductUpdateSchema
)


class ProductRouter(BaseRouter):
    model = Product
    childs_attr = [Product.stocks]

    
    CREATE_RESPONSE_MODEL = ProductCreateResponse
    UPDATE_RESPONSE_MODEL = ProductUpdateResponse
    LIST_REPONSE_MODEL = ListProductResponse
    READ_RESPONSE_MODEL = ProductResponse

    CREATE_SCHEMA = ProductCreateSchema
    UPDATE_SCHEMA = ProductUpdateSchema


product_router = ProductRouter(prefix="/product", tag=["Product"])
