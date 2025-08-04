"""HTTP client to make requests to external services."""

from app.core.constants import HTTP_TIMEOUT
from typing import Any, Dict, Optional
import httpx
from app.core.logger_custom import log


class HttpRequest:
    """HTTP client to make requests to external services."""

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(base_url=base_url)

    async def get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> httpx.Response:
        """Make a GET request to the given endpoint."""
        try:
            response = await self.client.get(
                endpoint, params=params, timeout=HTTP_TIMEOUT
            )
            # response.raise_for_status()
        except Exception as exc:
            log.error(f"Error in post request: {exc}")
            return httpx.Response(status_code=500, content=b'{"response": ""}')
        return response

    async def post(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        """Make a POST request to the given endpoint."""
        try:
            response = await self.client.post(
                endpoint, data=data, json=json, timeout=HTTP_TIMEOUT
            )
        except Exception as exc:
            log.error(f"Error in post request: {exc}")
            return httpx.Response(status_code=500, content=b'{"response": ""}')

        # response.raise_for_status()
        return response

    async def put(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        """Make a PUT request to the given endpoint."""
        try:
            response = await self.client.put(
                endpoint, data=data, json=json, timeout=HTTP_TIMEOUT
            )
        except Exception as exc:
            log.error(f"Error in post request: {exc}")
            return httpx.Response(status_code=500, content=b'{"response": ""}')
        # response.raise_for_status()
        return response

    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()
