from sqlmodel import SQLModel, Field, Relationship
from datetime import date
    

class ProductModel(SQLModel):
    name: str
    description: str
    expire_date: date | None = None

class Product(ProductModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    stocks: list["Stock"] = Relationship(back_populates="product")