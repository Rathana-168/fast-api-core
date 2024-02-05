from .models import StockModel
from app.product.models import Product


class StockCreateResponse(StockModel):
    pass


class StockUpdateResponse(StockCreateResponse):
    id: int


class StockListResponse(StockCreateResponse):
    product: Product | None = None
    

class StockCreateSchema(StockModel):
    pass


class StockUpdateSchema(StockCreateSchema):
    id: int


