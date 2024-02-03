from .models import ProductModel


class ProductCreateResponse(ProductModel):
    pass


class ProductUpdateResponse(ProductCreateResponse):
    id: int


class ProductCreateSchema(ProductModel):
    pass


class ProductUpdateSchema(ProductCreateSchema):
    id: int
    