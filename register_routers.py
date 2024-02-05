from app import app
from app.product.routers import product_router
from app.stock.routers import stock_router



app.include_router(product_router.router)
app.include_router(stock_router.router)