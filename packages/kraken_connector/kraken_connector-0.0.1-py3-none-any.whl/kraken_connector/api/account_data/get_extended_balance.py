from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.balanceex_2 import Balanceex2
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/private/BalanceEx",
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[Balanceex2]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Balanceex2.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[Balanceex2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Response[Balanceex2]:
    """Get Extended Balance

     Retrieve all extended account balances, including credits and held amounts. Balance available for
    trading is calculated as: `available balance = balance + credit - credit_used - hold_trade`

    **API Key Permissions Required:** `Funds permissions - Query`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Balanceex2]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Optional[Balanceex2]:
    """Get Extended Balance

     Retrieve all extended account balances, including credits and held amounts. Balance available for
    trading is calculated as: `available balance = balance + credit - credit_used - hold_trade`

    **API Key Permissions Required:** `Funds permissions - Query`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Balanceex2
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Response[Balanceex2]:
    """Get Extended Balance

     Retrieve all extended account balances, including credits and held amounts. Balance available for
    trading is calculated as: `available balance = balance + credit - credit_used - hold_trade`

    **API Key Permissions Required:** `Funds permissions - Query`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Balanceex2]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Optional[Balanceex2]:
    """Get Extended Balance

     Retrieve all extended account balances, including credits and held amounts. Balance available for
    trading is calculated as: `available balance = balance + credit - credit_used - hold_trade`

    **API Key Permissions Required:** `Funds permissions - Query`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Balanceex2
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
