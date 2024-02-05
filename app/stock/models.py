from sqlmodel import Field, Relationship
from typing import Optional

from app.base.models import AuditMixin
    

class StockModel(AuditMixin):
    product_id: int
    qty: int
    description: str | None

    
class Stock(StockModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    product_id: int = Field(default=None, foreign_key="product.id")
    product: Optional["Product"] = Relationship(back_populates="stocks")