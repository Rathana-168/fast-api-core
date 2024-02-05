from app.base.router import BaseRouter

from .models import Stock
from .schemas import (
    StockCreateResponse,
    StockUpdateResponse,
    StockCreateSchema,
    StockUpdateSchema,
    StockListResponse
)


class StockRouter(BaseRouter):
    model = Stock
    childs_attr = [Stock.product]

    CREATE_RESPONSE_MODEL = StockCreateResponse
    UPDATE_RESPONSE_MODEL = StockUpdateResponse
    LIST_REPONSE_MODEL = StockListResponse

    CREATE_SCHEMA = StockCreateSchema
    UPDATE_SCHEMA = StockUpdateSchema
    


stock_router = StockRouter(prefix="/stock", tag=["Stock"])
