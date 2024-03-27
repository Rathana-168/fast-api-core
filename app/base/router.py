from fastapi import APIRouter, status
from pydantic import BaseModel
from typing import TypeVar

from fastapi import Depends, HTTPException
from sqlmodel import Session
from app.authentication.jwt import get_current_user
from app.core.database import get_session
from app.base.crud import BaseCRUD
from app.base.responses import BaseResponse


class BaseRouter:
    model = None
    dependencies = []
    childs_attr = []

    CREATE_RESPONSE_MODEL = TypeVar('CREATE_RESPONSE_MODEL', bound=BaseResponse)
    UPDATE_RESPONSE_MODEL = TypeVar('UPDATE_RESPONSE_MODEL', bound=BaseResponse)
    LIST_REPONSE_MODEL = TypeVar('LIST_REPONSE_MODEL', bound=BaseResponse)
    READ_RESPONSE_MODEL = TypeVar('READ_RESPONSE_MODEL', bound=BaseResponse)
    DELETE_REPONSE_MODEL = TypeVar('DELETE_REPONSE_MODEL', bound=BaseResponse)

    CREATE_SCHEMA = None
    UPDATE_SCHEMA = None

    def __init__(self, prefix: str = "", tag: str = None):
        self.router = APIRouter(prefix=prefix, tags=tag, dependencies=self.dependencies)
        self.initial_endpoint()

    def _get_childs_attr(self):
        return self.childs_attr

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
        result = await logic.get_list(model=self.model, childs=self._get_childs_attr())
        return BaseResponse(message="succesfully", result=result)

    async def read(self, id: int, db: Session = Depends(get_session)):
        logic = BaseCRUD(session=db)
        obj = await logic.get(model=self.model, id=id, childs=self._get_childs_attr())
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
        return BaseResponse(message="succesfully", result=obj)

    async def create(self, schema: BaseModel, db: Session = Depends(get_session)):
        obj = self.model.model_validate(schema.model_dump())
        logic = BaseCRUD(session=db)
        await logic.create(model=obj)
        await logic.session.refresh(obj)
        return BaseResponse(message="Record has created successfully", result=obj)

    async def update(
        self,
        id: int,
        schema: BaseModel,
        db: Session = Depends(get_session),
    ):
        logic = BaseCRUD(session=db)

        obj = await logic.get(model=self.model, id=id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

        update_data = schema.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj = await logic.update(model=obj)
        return BaseResponse(message="Record has updated successfully", result=obj)

    def delete(self):
        return BaseResponse(message="Record has updated successfully", result='')
