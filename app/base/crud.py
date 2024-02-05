from fastapi import Depends
from sqlmodel import select, Session, SQLModel
from sqlalchemy.orm import selectinload
from app.core.database import get_session

class BaseCRUD:
    
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session
        
    
    async def query(self, model: SQLModel):
        statement = select(model)
        return statement
    
    
    async def create(self, model: SQLModel):
        self.session.add(model)
        await self.session.commit()
        return model
    
    
    async def update(self, model: SQLModel):
        self.session.add(model)
        await self.session.commit()
        return model

    
    async def get(self, model: SQLModel, id: int, **kwargs):
        statement = self.prepare_statement(model=model, **kwargs)
        statement = statement.where(model.id == id)
        result = await self.session.exec(statement)
        if result:
            return result.first()
        
        
    async def get_list(self, model: SQLModel, **kwargs):
        statement = self.prepare_statement(model=model, **kwargs)
        result = await self.session.exec(statement)
        if result:
            return result.all()
        
    
    def prepare_statement(self, model: SQLModel, **kwargs):
        statement = select(model)
        if select_attr := kwargs.get('select_attr'):
            statement = select(*select_attr)
        if childs := kwargs.get('childs'):
            statement = (statement.options(*[selectinload(child) for child in childs]))
        return statement