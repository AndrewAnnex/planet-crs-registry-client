from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exception_report import ExceptionReport
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    iau_version: int,
    code: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/ws/IAU/{iau_version}/{code}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ExceptionReport, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = response.json()
        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ExceptionReport.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ExceptionReport.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ExceptionReport, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    iau_version: int,
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ExceptionReport, HTTPValidationError]]:
    """Get the GML representation for a given WKT

     The GML representation for a given WKT

    Args:
        iau_version (int): Version of the WKT
        code (str): Identifier of the WKT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionReport, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        iau_version=iau_version,
        code=code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    iau_version: int,
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ExceptionReport, HTTPValidationError]]:
    """Get the GML representation for a given WKT

     The GML representation for a given WKT

    Args:
        iau_version (int): Version of the WKT
        code (str): Identifier of the WKT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionReport, HTTPValidationError]
    """

    return sync_detailed(
        iau_version=iau_version,
        code=code,
        client=client,
    ).parsed


async def asyncio_detailed(
    iau_version: int,
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ExceptionReport, HTTPValidationError]]:
    """Get the GML representation for a given WKT

     The GML representation for a given WKT

    Args:
        iau_version (int): Version of the WKT
        code (str): Identifier of the WKT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExceptionReport, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        iau_version=iau_version,
        code=code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    iau_version: int,
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ExceptionReport, HTTPValidationError]]:
    """Get the GML representation for a given WKT

     The GML representation for a given WKT

    Args:
        iau_version (int): Version of the WKT
        code (str): Identifier of the WKT

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExceptionReport, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            iau_version=iau_version,
            code=code,
            client=client,
        )
    ).parsed
