"""Main file to run the application"""

from app.middlewares.custom_middleware import middleware_general
from app.solution.routers.health_router import router as health_router
from app.solution.routers.media_router import router as media_router
from app.config.config import app


PREFIX_API = "/api-media"
# Middleware
app.middleware("http")(middleware_general)

# Routers
app.include_router(health_router, prefix=PREFIX_API + "/health")
app.include_router(media_router, prefix=PREFIX_API + "/media")
