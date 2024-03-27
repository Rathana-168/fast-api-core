from app import app, settings

# Modules Register Routers
import register_routers

# Main Routers
from app.authentication.routers import router as auth_router
app.include_router(auth_router)


@app.get('/init-db')
async def initialize_db():
    print('ok')
    from app.core.database import init_db
    await init_db()
    return 'All Tables has created successfully'


@app.get('/app-info')
async def app_info():
    return {
        "project_name": settings.project_name,
        "description": settings.description,
        "version": settings.version,
        "python version": settings.python_version
    }