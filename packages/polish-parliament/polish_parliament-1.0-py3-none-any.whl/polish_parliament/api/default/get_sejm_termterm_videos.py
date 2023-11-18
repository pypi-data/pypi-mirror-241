from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.video import Video
from ...types import UNSET, Response, Unset


def _get_kwargs(
    term: int,
    *,
    comm: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    offset: Union[Unset, None, int] = 0,
    since: Union[Unset, None, str] = UNSET,
    till: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["comm"] = comm

    params["limit"] = limit

    params["offset"] = offset

    params["since"] = since

    params["till"] = till

    params["title"] = title

    params["type"] = type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/sejm/term{term}/videos".format(
            term=term,
        ),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[List["Video"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Video.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[List["Video"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    *,
    client: Union[AuthenticatedClient, Client],
    comm: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    offset: Union[Unset, None, int] = 0,
    since: Union[Unset, None, str] = UNSET,
    till: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
) -> Response[List["Video"]]:
    """Returns a list of video transmissions

    Args:
        term (int):
        comm (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 50.
        offset (Union[Unset, None, int]):
        since (Union[Unset, None, str]):
        till (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Video']]
    """

    kwargs = _get_kwargs(
        term=term,
        comm=comm,
        limit=limit,
        offset=offset,
        since=since,
        till=till,
        title=title,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    *,
    client: Union[AuthenticatedClient, Client],
    comm: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    offset: Union[Unset, None, int] = 0,
    since: Union[Unset, None, str] = UNSET,
    till: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
) -> Optional[List["Video"]]:
    """Returns a list of video transmissions

    Args:
        term (int):
        comm (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 50.
        offset (Union[Unset, None, int]):
        since (Union[Unset, None, str]):
        till (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Video']
    """

    return sync_detailed(
        term=term,
        client=client,
        comm=comm,
        limit=limit,
        offset=offset,
        since=since,
        till=till,
        title=title,
        type=type,
    ).parsed


async def asyncio_detailed(
    term: int,
    *,
    client: Union[AuthenticatedClient, Client],
    comm: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    offset: Union[Unset, None, int] = 0,
    since: Union[Unset, None, str] = UNSET,
    till: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
) -> Response[List["Video"]]:
    """Returns a list of video transmissions

    Args:
        term (int):
        comm (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 50.
        offset (Union[Unset, None, int]):
        since (Union[Unset, None, str]):
        till (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Video']]
    """

    kwargs = _get_kwargs(
        term=term,
        comm=comm,
        limit=limit,
        offset=offset,
        since=since,
        till=till,
        title=title,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    *,
    client: Union[AuthenticatedClient, Client],
    comm: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    offset: Union[Unset, None, int] = 0,
    since: Union[Unset, None, str] = UNSET,
    till: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
) -> Optional[List["Video"]]:
    """Returns a list of video transmissions

    Args:
        term (int):
        comm (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 50.
        offset (Union[Unset, None, int]):
        since (Union[Unset, None, str]):
        till (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Video']
    """

    return (
        await asyncio_detailed(
            term=term,
            client=client,
            comm=comm,
            limit=limit,
            offset=offset,
            since=since,
            till=till,
            title=title,
            type=type,
        )
    ).parsed
