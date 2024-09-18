from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search_term_kw: str,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 100,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["search_term_kw"] = search_term_kw

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/web/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = response.json()
        return response_200
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
    search_term_kw: str,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 100,
) -> Response[Union[Any, HTTPValidationError]]:
    """Search

     Returns the representation related to the output of the search query.

    Args:
        request (Request): Request
        search_term_kw (str): term to search
        page (int, optional): Current page to display. Defaults to 1.
        limit (int, optional): number of records per page. Defaults to 100.

    Returns:
        object : The representation related to the output of the search query

    Raises:
        HTTPException: If the response indicates an error (status code >= 400).

    Args:
        search_term_kw (str):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        search_term_kw=search_term_kw,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    search_term_kw: str,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 100,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Search

     Returns the representation related to the output of the search query.

    Args:
        request (Request): Request
        search_term_kw (str): term to search
        page (int, optional): Current page to display. Defaults to 1.
        limit (int, optional): number of records per page. Defaults to 100.

    Returns:
        object : The representation related to the output of the search query

    Raises:
        HTTPException: If the response indicates an error (status code >= 400).

    Args:
        search_term_kw (str):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        search_term_kw=search_term_kw,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search_term_kw: str,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 100,
) -> Response[Union[Any, HTTPValidationError]]:
    """Search

     Returns the representation related to the output of the search query.

    Args:
        request (Request): Request
        search_term_kw (str): term to search
        page (int, optional): Current page to display. Defaults to 1.
        limit (int, optional): number of records per page. Defaults to 100.

    Returns:
        object : The representation related to the output of the search query

    Raises:
        HTTPException: If the response indicates an error (status code >= 400).

    Args:
        search_term_kw (str):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        search_term_kw=search_term_kw,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    search_term_kw: str,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 100,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Search

     Returns the representation related to the output of the search query.

    Args:
        request (Request): Request
        search_term_kw (str): term to search
        page (int, optional): Current page to display. Defaults to 1.
        limit (int, optional): number of records per page. Defaults to 100.

    Returns:
        object : The representation related to the output of the search query

    Raises:
        HTTPException: If the response indicates an error (status code >= 400).

    Args:
        search_term_kw (str):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            search_term_kw=search_term_kw,
            page=page,
            limit=limit,
        )
    ).parsed
