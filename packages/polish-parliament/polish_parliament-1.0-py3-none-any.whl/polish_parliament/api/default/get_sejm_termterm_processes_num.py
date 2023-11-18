from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.process_details import ProcessDetails
from ...types import Response


def _get_kwargs(
    term: int,
    num: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/sejm/term{term}/processes/{num}".format(
            term=term,
            num=num,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ProcessDetails]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ProcessDetails.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProcessDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    term: int,
    num: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ProcessDetails]:
    """Returns information about a process for a given print number

    Args:
        term (int):
        num (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcessDetails]
    """

    kwargs = _get_kwargs(
        term=term,
        num=num,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    term: int,
    num: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ProcessDetails]:
    """Returns information about a process for a given print number

    Args:
        term (int):
        num (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcessDetails
    """

    return sync_detailed(
        term=term,
        num=num,
        client=client,
    ).parsed


async def asyncio_detailed(
    term: int,
    num: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ProcessDetails]:
    """Returns information about a process for a given print number

    Args:
        term (int):
        num (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcessDetails]
    """

    kwargs = _get_kwargs(
        term=term,
        num=num,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    term: int,
    num: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ProcessDetails]:
    """Returns information about a process for a given print number

    Args:
        term (int):
        num (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcessDetails
    """

    return (
        await asyncio_detailed(
            term=term,
            num=num,
            client=client,
        )
    ).parsed
