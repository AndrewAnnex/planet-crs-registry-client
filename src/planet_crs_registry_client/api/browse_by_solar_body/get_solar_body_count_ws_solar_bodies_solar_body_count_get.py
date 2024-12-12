from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_not_found_error import HTTPNotFoundError
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    solar_body: str,
    *,
    limit: Union[None, Unset, int] = 50,
    offset: Union[None, Unset, int] = 0,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_limit: Union[None, Unset, int]
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_offset: Union[None, Unset, int]
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/ws/solar_bodies/{solar_body}/count",
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
    solar_body: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[None, Unset, int] = 50,
    offset: Union[None, Unset, int] = 0,
) -> Response[Union[HTTPNotFoundError, HTTPValidationError, int]]:
    """Count the number of WKTs for a given solar body

     Count the number of WKTs for a given solar body

    Args:
        solar_body (str):
        limit (Union[None, Unset, int]): Number of records to display Default: 50.
        offset (Union[None, Unset, int]): Number of records from which we start to display
            Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPNotFoundError, HTTPValidationError, int]]
    """

    kwargs = _get_kwargs(
        solar_body=solar_body,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    solar_body: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[None, Unset, int] = 50,
    offset: Union[None, Unset, int] = 0,
) -> Optional[Union[HTTPNotFoundError, HTTPValidationError, int]]:
    """Count the number of WKTs for a given solar body

     Count the number of WKTs for a given solar body

    Args:
        solar_body (str):
        limit (Union[None, Unset, int]): Number of records to display Default: 50.
        offset (Union[None, Unset, int]): Number of records from which we start to display
            Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPNotFoundError, HTTPValidationError, int]
    """

    return sync_detailed(
        solar_body=solar_body,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    solar_body: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[None, Unset, int] = 50,
    offset: Union[None, Unset, int] = 0,
) -> Response[Union[HTTPNotFoundError, HTTPValidationError, int]]:
    """Count the number of WKTs for a given solar body

     Count the number of WKTs for a given solar body

    Args:
        solar_body (str):
        limit (Union[None, Unset, int]): Number of records to display Default: 50.
        offset (Union[None, Unset, int]): Number of records from which we start to display
            Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPNotFoundError, HTTPValidationError, int]]
    """

    kwargs = _get_kwargs(
        solar_body=solar_body,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    solar_body: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[None, Unset, int] = 50,
    offset: Union[None, Unset, int] = 0,
) -> Optional[Union[HTTPNotFoundError, HTTPValidationError, int]]:
    """Count the number of WKTs for a given solar body

     Count the number of WKTs for a given solar body

    Args:
        solar_body (str):
        limit (Union[None, Unset, int]): Number of records to display Default: 50.
        offset (Union[None, Unset, int]): Number of records from which we start to display
            Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPNotFoundError, HTTPValidationError, int]
    """

    return (
        await asyncio_detailed(
            solar_body=solar_body,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
