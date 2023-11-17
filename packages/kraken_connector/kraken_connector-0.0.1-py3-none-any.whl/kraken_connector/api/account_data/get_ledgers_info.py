from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.query_3 import Query3
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/private/QueryLedgers",
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[Query3]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Query3.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[Query3]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Response[Query3]:
    """Query Ledgers

     Retrieve information about specific ledger entries.

    **API Key Permissions Required:** `Data - Query ledger entries`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Query3]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Optional[Query3]:
    """Query Ledgers

     Retrieve information about specific ledger entries.

    **API Key Permissions Required:** `Data - Query ledger entries`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Query3
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Response[Query3]:
    """Query Ledgers

     Retrieve information about specific ledger entries.

    **API Key Permissions Required:** `Data - Query ledger entries`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Query3]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Optional[Query3]:
    """Query Ledgers

     Retrieve information about specific ledger entries.

    **API Key Permissions Required:** `Data - Query ledger entries`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Query3
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
