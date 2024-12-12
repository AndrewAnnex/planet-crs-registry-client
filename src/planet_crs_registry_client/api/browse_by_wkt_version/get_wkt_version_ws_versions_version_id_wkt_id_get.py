from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_not_found_error import HTTPNotFoundError
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    version_id: int,
    wkt_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/ws/versions/{version_id}/{wkt_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPNotFoundError, HTTPValidationError, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = response.text
        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = HTTPNotFoundError.from_dict(response.text)

        return response_404
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = HTTPNotFoundError.from_dict(response.text)

        return response_400
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPNotFoundError, HTTPValidationError, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    version_id: int,
    wkt_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HTTPNotFoundError, HTTPValidationError, str]]:
    """Get a WKT for a given version.

     Retrieve a WKT

    Args:
        version_id (int): Version of the WKT
        wkt_id (str): Identifier of the WKT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPNotFoundError, HTTPValidationError, str]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        wkt_id=wkt_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    version_id: int,
    wkt_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HTTPNotFoundError, HTTPValidationError, str]]:
    """Get a WKT for a given version.

     Retrieve a WKT

    Args:
        version_id (int): Version of the WKT
        wkt_id (str): Identifier of the WKT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPNotFoundError, HTTPValidationError, str]
    """

    return sync_detailed(
        version_id=version_id,
        wkt_id=wkt_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    version_id: int,
    wkt_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HTTPNotFoundError, HTTPValidationError, str]]:
    """Get a WKT for a given version.

     Retrieve a WKT

    Args:
        version_id (int): Version of the WKT
        wkt_id (str): Identifier of the WKT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPNotFoundError, HTTPValidationError, str]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        wkt_id=wkt_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    version_id: int,
    wkt_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HTTPNotFoundError, HTTPValidationError, str]]:
    """Get a WKT for a given version.

     Retrieve a WKT

    Args:
        version_id (int): Version of the WKT
        wkt_id (str): Identifier of the WKT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPNotFoundError, HTTPValidationError, str]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            wkt_id=wkt_id,
            client=client,
        )
    ).parsed
