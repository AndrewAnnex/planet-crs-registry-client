from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_not_found_error import HTTPNotFoundError
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    search_term_kw: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["search_term_kw"] = search_term_kw

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/ws/search/count",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPNotFoundError, HTTPValidationError, int]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(int, response.json())
        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = HTTPNotFoundError.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPNotFoundError, HTTPValidationError, int]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search_term_kw: str,
) -> Response[Union[HTTPNotFoundError, HTTPValidationError, int]]:
    """Count WKT by keyword

     Count WKT by keyword

    Args:
        search_term_kw (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPNotFoundError, HTTPValidationError, int]]
    """

    kwargs = _get_kwargs(
        search_term_kw=search_term_kw,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    search_term_kw: str,
) -> Optional[Union[HTTPNotFoundError, HTTPValidationError, int]]:
    """Count WKT by keyword

     Count WKT by keyword

    Args:
        search_term_kw (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPNotFoundError, HTTPValidationError, int]
    """

    return sync_detailed(
        client=client,
        search_term_kw=search_term_kw,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search_term_kw: str,
) -> Response[Union[HTTPNotFoundError, HTTPValidationError, int]]:
    """Count WKT by keyword

     Count WKT by keyword

    Args:
        search_term_kw (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPNotFoundError, HTTPValidationError, int]]
    """

    kwargs = _get_kwargs(
        search_term_kw=search_term_kw,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    search_term_kw: str,
) -> Optional[Union[HTTPNotFoundError, HTTPValidationError, int]]:
    """Count WKT by keyword

     Count WKT by keyword

    Args:
        search_term_kw (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPNotFoundError, HTTPValidationError, int]
    """

    return (
        await asyncio_detailed(
            client=client,
            search_term_kw=search_term_kw,
        )
    ).parsed
