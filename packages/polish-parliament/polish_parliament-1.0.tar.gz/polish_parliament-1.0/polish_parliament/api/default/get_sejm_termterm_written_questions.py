import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.written_question import WrittenQuestion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    term: int,
    *,
    from_: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    modified_since: Union[Unset, None, datetime.datetime] = UNSET,
    offset: Union[Unset, None, int] = 0,
    since: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    till: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["from"] = from_

    params["limit"] = limit

    json_modified_since: Union[Unset, None, str] = UNSET
    if not isinstance(modified_since, Unset):
        json_modified_since = modified_since.isoformat() if modified_since else None

    params["modifiedSince"] = json_modified_since

    params["offset"] = offset

    params["since"] = since

    params["sort_by"] = sort_by

    params["till"] = till

    params["title"] = title

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/sejm/term{term}/writtenQuestions".format(
            term=term,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["WrittenQuestion"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = WrittenQuestion.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["WrittenQuestion"]]:
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
    from_: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    modified_since: Union[Unset, None, datetime.datetime] = UNSET,
    offset: Union[Unset, None, int] = 0,
    since: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    till: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
) -> Response[List["WrittenQuestion"]]:
    """Returns a list of written questions

    Args:
        term (int):
        from_ (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 50.
        modified_since (Union[Unset, None, datetime.datetime]):  Example: 2022-03-10 12:15:50.
        offset (Union[Unset, None, int]):
        since (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):
        till (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        to (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['WrittenQuestion']]
    """

    kwargs = _get_kwargs(
        term=term,
        from_=from_,
        limit=limit,
        modified_since=modified_since,
        offset=offset,
        since=since,
        sort_by=sort_by,
        till=till,
        title=title,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    modified_since: Union[Unset, None, datetime.datetime] = UNSET,
    offset: Union[Unset, None, int] = 0,
    since: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    till: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
) -> Optional[List["WrittenQuestion"]]:
    """Returns a list of written questions

    Args:
        term (int):
        from_ (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 50.
        modified_since (Union[Unset, None, datetime.datetime]):  Example: 2022-03-10 12:15:50.
        offset (Union[Unset, None, int]):
        since (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):
        till (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        to (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['WrittenQuestion']
    """

    return sync_detailed(
        term=term,
        client=client,
        from_=from_,
        limit=limit,
        modified_since=modified_since,
        offset=offset,
        since=since,
        sort_by=sort_by,
        till=till,
        title=title,
        to=to,
    ).parsed


async def asyncio_detailed(
    term: int,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    modified_since: Union[Unset, None, datetime.datetime] = UNSET,
    offset: Union[Unset, None, int] = 0,
    since: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    till: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
) -> Response[List["WrittenQuestion"]]:
    """Returns a list of written questions

    Args:
        term (int):
        from_ (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 50.
        modified_since (Union[Unset, None, datetime.datetime]):  Example: 2022-03-10 12:15:50.
        offset (Union[Unset, None, int]):
        since (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):
        till (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        to (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['WrittenQuestion']]
    """

    kwargs = _get_kwargs(
        term=term,
        from_=from_,
        limit=limit,
        modified_since=modified_since,
        offset=offset,
        since=since,
        sort_by=sort_by,
        till=till,
        title=title,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 50,
    modified_since: Union[Unset, None, datetime.datetime] = UNSET,
    offset: Union[Unset, None, int] = 0,
    since: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    till: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
) -> Optional[List["WrittenQuestion"]]:
    """Returns a list of written questions

    Args:
        term (int):
        from_ (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 50.
        modified_since (Union[Unset, None, datetime.datetime]):  Example: 2022-03-10 12:15:50.
        offset (Union[Unset, None, int]):
        since (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):
        till (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        to (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['WrittenQuestion']
    """

    return (
        await asyncio_detailed(
            term=term,
            client=client,
            from_=from_,
            limit=limit,
            modified_since=modified_since,
            offset=offset,
            since=since,
            sort_by=sort_by,
            till=till,
            title=title,
            to=to,
        )
    ).parsed
