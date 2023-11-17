from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.history_2 import History2
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/private/TradesHistory",
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[History2]:
    if response.status_code == HTTPStatus.OK:
        response_200 = History2.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[History2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Response[History2]:
    """Get Trades History

     Retrieve information about trades/fills. 50 results are returned at a time, the most recent by
    default.
    * Unless otherwise stated, costs, fees, prices, and volumes are specified with the precision for the
    asset pair (`pair_decimals` and `lot_decimals`), not the individual assets' precision (`decimals`).

    **API Key Permissions Required:** `Orders and trades - Query closed orders & trades`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[History2]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Optional[History2]:
    """Get Trades History

     Retrieve information about trades/fills. 50 results are returned at a time, the most recent by
    default.
    * Unless otherwise stated, costs, fees, prices, and volumes are specified with the precision for the
    asset pair (`pair_decimals` and `lot_decimals`), not the individual assets' precision (`decimals`).

    **API Key Permissions Required:** `Orders and trades - Query closed orders & trades`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        History2
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Response[History2]:
    """Get Trades History

     Retrieve information about trades/fills. 50 results are returned at a time, the most recent by
    default.
    * Unless otherwise stated, costs, fees, prices, and volumes are specified with the precision for the
    asset pair (`pair_decimals` and `lot_decimals`), not the individual assets' precision (`decimals`).

    **API Key Permissions Required:** `Orders and trades - Query closed orders & trades`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[History2]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Optional[History2]:
    """Get Trades History

     Retrieve information about trades/fills. 50 results are returned at a time, the most recent by
    default.
    * Unless otherwise stated, costs, fees, prices, and volumes are specified with the precision for the
    asset pair (`pair_decimals` and `lot_decimals`), not the individual assets' precision (`decimals`).

    **API Key Permissions Required:** `Orders and trades - Query closed orders & trades`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        History2
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
