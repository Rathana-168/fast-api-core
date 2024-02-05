from .models import ProductModel
from typing import List

from app.base.schemas import BaseResponse
from app.stock.models import Stock


class BaseProductResponse(ProductModel):
    stocks: List["Stock"]
    
    
class ProductResponse(BaseResponse):
    result: BaseProductResponse
    
    
class ListProductResponse(BaseResponse):
    result: List[BaseProductResponse]
    

class ProductCreateResponse(BaseResponse):
    result: BaseProductResponse


class ProductUpdateResponse(BaseResponse):
    result: BaseProductResponse


class ProductCreateSchema(ProductModel):
    pass


class ProductUpdateSchema(ProductCreateSchema):
    id: int
