from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.committee import Committee
from ...types import Response


def _get_kwargs(
    term: int,
    code: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/sejm/term{term}/committees/{code}".format(
            term=term,
            code=code,
        ),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Committee]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Committee.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Committee]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Committee]:
    """Returns a committee details

    Args:
        term (int):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Committee]
    """

    kwargs = _get_kwargs(
        term=term,
        code=code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Committee]:
    """Returns a committee details

    Args:
        term (int):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Committee
    """

    return sync_detailed(
        term=term,
        code=code,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: int,
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Committee]:
    """Returns a committee details

    Args:
        term (int):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Committee]
    """

    kwargs = _get_kwargs(
        term=term,
        code=code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Committee]:
    """Returns a committee details

    Args:
        term (int):
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Committee
    """

    return (
        await asyncio_detailed(
            term=term,
            code=code,
            client=client,
        )
    ).parsed
