from fastapi import APIRouter
from app.interface.crud import CRUDInterface

from fastapi import Depends, HTTPException
from sqlmodel import Session
from app.core.database import get_session
from app.base.crud import BaseCRUD


class BaseRouter:
    model = None

    CREATE_RESPONSE_MODEL = None
    UPDATE_RESPONSE_MODEL = None
    LIST_REPONSE_MODEL = None
    READ_RESPONSE_MODEL = None
    DELETE_REPONSE_MODEL = None

    CREATE_SCHEMA = None
    UPDATE_SCHEMA = None

    def __init__(self, prefix: str = "", tag: str = None):
        self.router = APIRouter(prefix=prefix, tags=tag)
        self.initial_endpoint()

    def initial_endpoint(self):

        async def get_list(db: Session = Depends(get_session)):
            return await self.get_list(db)

        async def read(id: int, db: Session = Depends(get_session)):
            return await self.read(id, db)

        async def create(
            schema: self.CREATE_SCHEMA, db: Session = Depends(get_session)
        ):
            return await self.create(schema, db)

        async def update(
            id: int,
            schema: self.UPDATE_SCHEMA,
            db: Session = Depends(get_session),
        ):
            return await self.update(id=id, schema=schema, db=db)

        async def delete():
            return await self.delete()

        self.router.add_api_route(
            "/", get_list, methods=["GET"], response_model=self.LIST_REPONSE_MODEL
        )
        self.router.add_api_route(
            "/{id}", read, methods=["GET"], response_model=self.READ_RESPONSE_MODEL
        )
        self.router.add_api_route(
            "/",
            create,
            methods=["POST"],
            response_model=self.CREATE_RESPONSE_MODEL,
        )
        self.router.add_api_route(
            "/{id}",
            update,
            methods=["PUT"],
            response_model=self.UPDATE_RESPONSE_MODEL,
        )
        self.router.add_api_route(
            "/{id}",
            delete,
            methods=["DELETE"],
            response_model=self.DELETE_REPONSE_MODEL,
        )

    async def get_list(self, db: Session = Depends(get_session)):
        logic = BaseCRUD(session=db)
        return await logic.get_list(model=self.model)

    async def read(self, id: int, db: Session = Depends(get_session)):
        logic = BaseCRUD(session=db)
        return await logic.get(model=self.model, id=id)

    async def create(self, schema: CREATE_SCHEMA, db: Session = Depends(get_session)):
        obj = self.model.model_validate(schema.model_dump())
        logic = BaseCRUD(session=db)
        await logic.create(model=obj)
        await logic.session.refresh(obj)
        return obj

    async def update(
        self,
        id: int,
        schema: UPDATE_SCHEMA,
        db: Session = Depends(get_session),
    ):
        logic = BaseCRUD(session=db)

        obj = await logic.get(model=self.model, id=id)
        if not obj:
            raise HTTPException(status_code=404, detail="Product Not Found")

        update_data = schema.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj = await logic.update(model=obj)
        return obj

    def delete(self):
        return ""
