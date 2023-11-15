import functools
import json
from typing import (
    Any,
    List,
    Optional,
    TYPE_CHECKING,
    Dict, Iterable, Callable,
)
from urllib.parse import urljoin

import requests
from requests import Response

from scale_egp.exceptions import exception_from_response
from scale_egp.utils.model_utils import BaseModel

if TYPE_CHECKING:
    from scale_egp.sdk.client import EGPClient

DEFAULT_TIMEOUT = 60


def handle_api_exceptions(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.status_code != 200:
            raise exception_from_response(response)
        return response
    return wrapper


class APIEngine:

    def __init__(self, api_client: "EGPClient"):
        self._api_client = api_client

    def _post(
        self,
        sub_path: str,
        request: Optional[BaseModel] = None,
        timeout: Optional[int] = None,
        stream: bool = False,
    ) -> Response:
        response = self._raw_post(
            sub_path=sub_path,
            request_json=request.model_dump() if request is not None else None,
            timeout=timeout if timeout is not None else DEFAULT_TIMEOUT,
            stream=stream,
        )
        return response

    def _post_stream(
        self,
        sub_path: str,
        request: Optional[BaseModel] = None,
        timeout: Optional[int] = None,
    ) -> Iterable[Dict[str, Any]]:
        response = self._raw_post(
            sub_path=sub_path,
            request_json=request.model_dump() if request is not None else None,
            timeout=timeout if timeout is not None else DEFAULT_TIMEOUT,
            stream=True,
        )
        for raw_event in response.iter_lines():
            if raw_event:
                event_str = raw_event.decode()
                if event_str.startswith('data: '):
                    event_json_str = event_str[len('data: '):]
                    try:
                        yield json.loads(event_json_str)
                    except json.JSONDecodeError:
                        raise ValueError(f"Invalid JSON payload: {event_json_str}")

    def _post_batch(
        self,
        sub_path: str,
        request_batch: Optional[List[BaseModel]] = None,
        timeout: Optional[int] = None,
    ) -> Response:
        response = self._raw_post(
            sub_path=sub_path,
            request_json=[request.model_dump() for request in request_batch],
            timeout=timeout if timeout is not None else DEFAULT_TIMEOUT,
        )
        return response

    def _get(
        self,
        sub_path: str,
        query_params: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
    ) -> Response:
        response = self._raw_get(
            sub_path=sub_path,
            query_params=query_params,
            timeout=timeout if timeout is not None else DEFAULT_TIMEOUT,
        )
        return response

    def _patch(
        self,
        sub_path: str,
        request: Optional[BaseModel] = None,
        timeout: Optional[int] = None,
    ) -> Response:
        response = self._raw_patch(
            sub_path=sub_path,
            request_json=request.model_dump() if request is not None else None,
            timeout=timeout if timeout is not None else DEFAULT_TIMEOUT,
        )
        return response

    def _delete(
        self,
        sub_path: str,
        timeout: Optional[int] = None,
    ) -> Response:
        response = self._raw_delete(
            sub_path=sub_path,
            timeout=timeout if timeout is not None else DEFAULT_TIMEOUT,
        )
        return response

    @handle_api_exceptions
    def _raw_post(
        self,
        sub_path: str,
        request_json: Optional[Dict[str, Any]] = None,
        stream: bool = False,
        timeout: Optional[int] = None,
        additional_headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        response = requests.post(
            urljoin(self._api_client.endpoint_url, sub_path),
            json=request_json,
            timeout=timeout if timeout is not None else DEFAULT_TIMEOUT,
            headers={
                "x-api-key": self._api_client.api_key,
                **(additional_headers if additional_headers is not None else {}),
            },
            stream=stream,
        )
        return response

    @handle_api_exceptions
    def _raw_get(
        self,
        sub_path: str,
        timeout: Optional[int] = None,
        query_params: Optional[Dict[str, str]] = None,
        additional_headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        response = requests.get(
            urljoin(self._api_client.endpoint_url, sub_path),
            timeout=timeout if timeout is not None else DEFAULT_TIMEOUT,
            params=query_params,
            headers={
                "x-api-key": self._api_client.api_key,
                **(additional_headers if additional_headers is not None else {}),
            },
        )
        return response

    @handle_api_exceptions
    def _raw_patch(
        self,
        sub_path: str,
        request_json: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        additional_headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        response = requests.patch(
            urljoin(self._api_client.endpoint_url, sub_path),
            json=request_json,
            timeout=timeout if timeout is not None else DEFAULT_TIMEOUT,
            headers={
                "x-api-key": self._api_client.api_key,
                **(additional_headers if additional_headers is not None else {}),
            },
        )
        return response

    @handle_api_exceptions
    def _raw_delete(
        self,
        sub_path: str,
        timeout: Optional[int] = None,
        additional_headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        response = requests.delete(
            urljoin(self._api_client.endpoint_url, sub_path),
            timeout=timeout if timeout is not None else DEFAULT_TIMEOUT,
            headers={
                "x-api-key": self._api_client.api_key,
                **(additional_headers if additional_headers is not None else {}),
            },
        )
        return response
