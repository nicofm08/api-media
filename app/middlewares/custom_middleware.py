"""Custom middleware for FastAPI application."""

from urllib.parse import urlparse
from fastapi import Request
from app.core.logger_custom import log
from app.core.constants import LOG_MIDDLEWARE


excluded_routes = [
    ("docs", "GET"),
    ("openapi.json", "GET"),
    ("health", "POST"),
]


async def middleware_general(request: Request, call_next) -> Request:
    """Middleware for general purposes."""
    parsed_url = urlparse(str(request.url))
    path_segments = parsed_url.path.split("/")
    last_segment = path_segments[-1]
    method = str(request.method)
    route = (last_segment, method)

    if method == "OPTIONS":
        return await call_next(request)
    if route in excluded_routes:
        log.info(f"{LOG_MIDDLEWARE} Excluded route `{route}`")
        return await call_next(request)
    log.info(f"{LOG_MIDDLEWARE} request pass through middleware")
    return await call_next(request)
