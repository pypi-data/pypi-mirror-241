from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...constants.market_data import OHLCDataInterval
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.ohlc import Ohlc
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pair: str,
    interval: Union[Unset, None, OHLCDataInterval] = OHLCDataInterval.ONE_MINUTE,
    since: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["pair"] = pair

    json_interval: Union[Unset, None, int] = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval.value if interval else None

    params["interval"] = json_interval

    params["since"] = since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/public/OHLC",
        "params": params,
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[Ohlc]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Ohlc.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[Ohlc]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: str,
    interval: Union[Unset, None, OHLCDataInterval] = OHLCDataInterval.ONE_MINUTE,
    since: Union[Unset, None, int] = UNSET,
) -> Response[Ohlc]:
    """Get OHLC Data

     Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always
    be present, regardless of the value of `since`.

    Args:
        pair (str):
        interval (Union[Unset, None, OHLCDataInterval]):  Default: OHLCDataInterval.ONE_MINUTE.
        since (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Ohlc]
    """

    kwargs = _get_kwargs(
        pair=pair,
        interval=interval,
        since=since,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: str,
    interval: Union[Unset, None, OHLCDataInterval] = OHLCDataInterval.ONE_MINUTE,
    since: Union[Unset, None, int] = UNSET,
) -> Optional[Ohlc]:
    """Get OHLC Data

     Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always
    be present, regardless of the value of `since`.

    Args:
        pair (str):
        interval (Union[Unset, None, OHLCDataInterval]):  Default: OHLCDataInterval.ONE_MINUTE.
        since (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Ohlc
    """

    return sync_detailed(
        client=client,
        pair=pair,
        interval=interval,
        since=since,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: str,
    interval: Union[Unset, None, OHLCDataInterval] = OHLCDataInterval.ONE_MINUTE,
    since: Union[Unset, None, int] = UNSET,
) -> Response[Ohlc]:
    """Get OHLC Data

     Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always
    be present, regardless of the value of `since`.

    Args:
        pair (str):
        interval (Union[Unset, None, OHLCDataInterval]):  Default: OHLCDataInterval.ONE_MINUTE.
        since (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Ohlc]
    """

    kwargs = _get_kwargs(
        pair=pair,
        interval=interval,
        since=since,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: str,
    interval: Union[Unset, None, OHLCDataInterval] = OHLCDataInterval.ONE_MINUTE,
    since: Union[Unset, None, int] = UNSET,
) -> Optional[Ohlc]:
    """Get OHLC Data

     Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always
    be present, regardless of the value of `since`.

    Args:
        pair (str):
        interval (Union[Unset, None, OHLCDataInterval]):  Default: OHLCDataInterval.ONE_MINUTE.
        since (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Ohlc
    """

    return (
        await asyncio_detailed(
            client=client,
            pair=pair,
            interval=interval,
            since=since,
        )
    ).parsed
