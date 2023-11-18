from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    term: int,
    num: str,
    key: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/sejm/term{term}/interpellations/{num}/reply/{key}/body".format(
            term=term,
            num=num,
            key=key,
        ),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[str]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(str, response.text)
        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    num: str,
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[str]:
    """Returns a reply body in HTML format

    Args:
        term (int):
        num (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        term=term,
        num=num,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    num: str,
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[str]:
    """Returns a reply body in HTML format

    Args:
        term (int):
        num (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        term=term,
        num=num,
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: int,
    num: str,
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[str]:
    """Returns a reply body in HTML format

    Args:
        term (int):
        num (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        term=term,
        num=num,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    num: str,
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[str]:
    """Returns a reply body in HTML format

    Args:
        term (int):
        num (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            term=term,
            num=num,
            key=key,
            client=client,
        )
    ).parsed
