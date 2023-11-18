from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.voting import Voting
from ...types import Response


def _get_kwargs(
    term: int,
    sitting: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/sejm/term{term}/votings/{sitting}".format(
            term=term,
            sitting=sitting,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["Voting"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Voting.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["Voting"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    sitting: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["Voting"]]:
    """Returns a list of votings for a given sitting

    Args:
        term (int):
        sitting (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Voting']]
    """

    kwargs = _get_kwargs(
        term=term,
        sitting=sitting,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    sitting: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["Voting"]]:
    """Returns a list of votings for a given sitting

    Args:
        term (int):
        sitting (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Voting']
    """

    return sync_detailed(
        term=term,
        sitting=sitting,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: int,
    sitting: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["Voting"]]:
    """Returns a list of votings for a given sitting

    Args:
        term (int):
        sitting (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Voting']]
    """

    kwargs = _get_kwargs(
        term=term,
        sitting=sitting,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    sitting: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["Voting"]]:
    """Returns a list of votings for a given sitting

    Args:
        term (int):
        sitting (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Voting']
    """

    return (
        await asyncio_detailed(
            term=term,
            sitting=sitting,
            client=client,
        )
    ).parsed
