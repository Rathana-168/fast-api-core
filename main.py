from app import app

from app.authentication.routers import router as auth_router
from app.product.routers import product_router

from app.product.models import Product


app.include_router(auth_router)
app.include_router(product_router.router)


from app.core.database import init_db

@app.get('/init-db')
async def create_db():
    await init_db()
    return 'Hello World'