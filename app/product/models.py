from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from datetime import date
    

class ProductModel(SQLModel):
    name: str
    description: str
    expire_date: date | None = None
    
66
class Product(ProductModel, table=True):
    id: int | None = Field(default=None, primary_key=True)