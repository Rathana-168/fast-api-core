from fastapi import Depends, HTTPException
from sqlmodel import Session
from app.core.database import get_session
from app.base.crud import BaseCRUD

from app.base.router import BaseRouter


from .models import Product
from .schemas import ProductCreateResponse, ProductUpdateResponse, ProductCreateSchema, ProductUpdateSchema


class  ProductRouter(BaseRouter):
    model = Product
    
    CREATE_RESPONSE_MODEL = ProductCreateResponse
    UPDATE_RESPONSE_MODEL = ProductUpdateResponse

    CREATE_SCHEMA = ProductCreateSchema
    UPDATE_SCHEMA = ProductUpdateSchema
    
    
    async def list(self, db: Session = Depends(get_session)):
        logic = BaseCRUD(session=db)
        return await logic.get_list(model=self.model)
    
    
    async def read(self, id: int, db: Session = Depends(get_session)):
        logic = BaseCRUD(session=db)
        return await logic.get(model=self.model, id=id)
    
    
    async def create(self, schema: CREATE_SCHEMA, db: Session = Depends(get_session)):
        product = self.model.model_validate(schema.model_dump())
        logic = BaseCRUD(session=db)
        await logic.create(model=product)
        return product
    
    
    async def update(self, id: int, schema: UPDATE_SCHEMA, db: Session = Depends(get_session)):
        logic = BaseCRUD(session=db)
        
        product = await logic.get(model=self.model, id=id)
        if not product:
            raise HTTPException(status_code=404, detail="Product Not Found")
        
        update_data = schema.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            if hasattr(product, key):
                setattr(product, key, value)
                
        product = await logic.update(model=product)
        return product
    
    
    def delete(self):
        return super().delete()
    

product_router = ProductRouter(prefix='/product', tag=['Product'])