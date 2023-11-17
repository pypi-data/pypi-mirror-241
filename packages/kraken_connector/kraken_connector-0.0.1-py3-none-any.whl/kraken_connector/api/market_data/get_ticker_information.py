from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.ticker_2 import Ticker2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pair: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["pair"] = pair

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/public/Ticker",
        "params": params,
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[Ticker2]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Ticker2.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[Ticker2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: Union[Unset, None, str] = UNSET,
) -> Response[Ticker2]:
    """Get Ticker Information

     Note: Today's prices start at midnight UTC. Leaving the pair parameter blank will return tickers for
    all tradable assets on Kraken.

    Args:
        pair (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Ticker2]
    """

    kwargs = _get_kwargs(
        pair=pair,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: Union[Unset, None, str] = UNSET,
) -> Optional[Ticker2]:
    """Get Ticker Information

     Note: Today's prices start at midnight UTC. Leaving the pair parameter blank will return tickers for
    all tradable assets on Kraken.

    Args:
        pair (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Ticker2
    """

    return sync_detailed(
        client=client,
        pair=pair,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: Union[Unset, None, str] = UNSET,
) -> Response[Ticker2]:
    """Get Ticker Information

     Note: Today's prices start at midnight UTC. Leaving the pair parameter blank will return tickers for
    all tradable assets on Kraken.

    Args:
        pair (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Ticker2]
    """

    kwargs = _get_kwargs(
        pair=pair,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: Union[Unset, None, str] = UNSET,
) -> Optional[Ticker2]:
    """Get Ticker Information

     Note: Today's prices start at midnight UTC. Leaving the pair parameter blank will return tickers for
    all tradable assets on Kraken.

    Args:
        pair (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Ticker2
    """

    return (
        await asyncio_detailed(
            client=client,
            pair=pair,
        )
    ).parsed
