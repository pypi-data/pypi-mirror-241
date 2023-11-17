from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.get_trades_info_response_200 import GetTradesInfoResponse200
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/private/QueryTrades",
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[GetTradesInfoResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetTradesInfoResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[GetTradesInfoResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Response[GetTradesInfoResponse200]:
    """Query Trades Info

     Retrieve information about specific trades/fills.

    **API Key Permissions Required:** `Orders and trades - Query closed orders & trades`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[GetTradesInfoResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Optional[GetTradesInfoResponse200]:
    """Query Trades Info

     Retrieve information about specific trades/fills.

    **API Key Permissions Required:** `Orders and trades - Query closed orders & trades`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        GetTradesInfoResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Response[GetTradesInfoResponse200]:
    """Query Trades Info

     Retrieve information about specific trades/fills.

    **API Key Permissions Required:** `Orders and trades - Query closed orders & trades`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[GetTradesInfoResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Optional[GetTradesInfoResponse200]:
    """Query Trades Info

     Retrieve information about specific trades/fills.

    **API Key Permissions Required:** `Orders and trades - Query closed orders & trades`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        GetTradesInfoResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
