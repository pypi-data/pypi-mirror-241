from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.club import Club
from ...types import Response


def _get_kwargs(
    term: int,
    id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/sejm/term{term}/clubs/{id}".format(
            term=term,
            id=id,
        ),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Club]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Club.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Club]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Club]:
    """Returns information about a club

    Args:
        term (int):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Club]
    """

    kwargs = _get_kwargs(
        term=term,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Club]:
    """Returns information about a club

    Args:
        term (int):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Club
    """

    return sync_detailed(
        term=term,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: int,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Club]:
    """Returns information about a club

    Args:
        term (int):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Club]
    """

    kwargs = _get_kwargs(
        term=term,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Club]:
    """Returns information about a club

    Args:
        term (int):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Club
    """

    return (
        await asyncio_detailed(
            term=term,
            id=id,
            client=client,
        )
    ).parsed
