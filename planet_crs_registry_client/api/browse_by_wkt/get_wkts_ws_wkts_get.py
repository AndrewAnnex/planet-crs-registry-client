from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[None, Unset, int] = 50,
    offset: Union[None, Unset, int] = 0,
    is_clean_formatting: Union[None, Unset, bool] = True,
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

    json_is_clean_formatting: Union[None, Unset, bool]
    if isinstance(is_clean_formatting, Unset):
        json_is_clean_formatting = UNSET
    else:
        json_is_clean_formatting = is_clean_formatting
    params["is_clean_formatting"] = json_is_clean_formatting

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/ws/wkts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
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
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[None, Unset, int] = 50,
    offset: Union[None, Unset, int] = 0,
    is_clean_formatting: Union[None, Unset, bool] = True,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get information about WKTs.

     Lists all WKTs regardless of version

    Args:
        limit (Union[None, Unset, int]): Number of records to display Default: 50.
        offset (Union[None, Unset, int]): Number of records from which we start to display
            Default: 0.
        is_clean_formatting (Union[None, Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        is_clean_formatting=is_clean_formatting,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[None, Unset, int] = 50,
    offset: Union[None, Unset, int] = 0,
    is_clean_formatting: Union[None, Unset, bool] = True,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get information about WKTs.

     Lists all WKTs regardless of version

    Args:
        limit (Union[None, Unset, int]): Number of records to display Default: 50.
        offset (Union[None, Unset, int]): Number of records from which we start to display
            Default: 0.
        is_clean_formatting (Union[None, Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        is_clean_formatting=is_clean_formatting,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[None, Unset, int] = 50,
    offset: Union[None, Unset, int] = 0,
    is_clean_formatting: Union[None, Unset, bool] = True,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get information about WKTs.

     Lists all WKTs regardless of version

    Args:
        limit (Union[None, Unset, int]): Number of records to display Default: 50.
        offset (Union[None, Unset, int]): Number of records from which we start to display
            Default: 0.
        is_clean_formatting (Union[None, Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        is_clean_formatting=is_clean_formatting,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[None, Unset, int] = 50,
    offset: Union[None, Unset, int] = 0,
    is_clean_formatting: Union[None, Unset, bool] = True,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get information about WKTs.

     Lists all WKTs regardless of version

    Args:
        limit (Union[None, Unset, int]): Number of records to display Default: 50.
        offset (Union[None, Unset, int]): Number of records from which we start to display
            Default: 0.
        is_clean_formatting (Union[None, Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            is_clean_formatting=is_clean_formatting,
        )
    ).parsed
