from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...constants.market_data import TradableAssetPairInfo
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.get_tradable_asset_pairs_response_200 import (
    GetTradableAssetPairsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pair: Union[Unset, None, str] = UNSET,
    info: Union[Unset, None, TradableAssetPairInfo] = TradableAssetPairInfo.INFO,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["pair"] = pair

    json_info: Union[Unset, None, str] = UNSET
    if not isinstance(info, Unset):
        json_info = info.value if info else None

    params["info"] = json_info

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/public/AssetPairs",
        "params": params,
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[GetTradableAssetPairsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetTradableAssetPairsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[GetTradableAssetPairsResponse200]:
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
    info: Union[Unset, None, TradableAssetPairInfo] = TradableAssetPairInfo.INFO,
) -> Response[GetTradableAssetPairsResponse200]:
    """Get Tradable Asset Pairs

     Get tradable asset pairs

    Args:
        pair (Union[Unset, None, str]):
        info (Union[Unset, None, TradableAssetPairInfo]):  Default:
            TradableAssetPairInfo.INFO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[GetTradableAssetPairsResponse200]
    """

    kwargs = _get_kwargs(
        pair=pair,
        info=info,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: Union[Unset, None, str] = UNSET,
    info: Union[Unset, None, TradableAssetPairInfo] = TradableAssetPairInfo.INFO,
) -> Optional[GetTradableAssetPairsResponse200]:
    """Get Tradable Asset Pairs

     Get tradable asset pairs

    Args:
        pair (Union[Unset, None, str]):
        info (Union[Unset, None, TradableAssetPairInfo]):  Default:
            TradableAssetPairInfo.INFO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        GetTradableAssetPairsResponse200
    """

    return sync_detailed(
        client=client,
        pair=pair,
        info=info,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: Union[Unset, None, str] = UNSET,
    info: Union[Unset, None, TradableAssetPairInfo] = TradableAssetPairInfo.INFO,
) -> Response[GetTradableAssetPairsResponse200]:
    """Get Tradable Asset Pairs

     Get tradable asset pairs

    Args:
        pair (Union[Unset, None, str]):
        info (Union[Unset, None, TradableAssetPairInfo]):  Default:
            TradableAssetPairInfo.INFO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[GetTradableAssetPairsResponse200]
    """

    kwargs = _get_kwargs(
        pair=pair,
        info=info,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: Union[Unset, None, str] = UNSET,
    info: Union[Unset, None, TradableAssetPairInfo] = TradableAssetPairInfo.INFO,
) -> Optional[GetTradableAssetPairsResponse200]:
    """Get Tradable Asset Pairs

     Get tradable asset pairs

    Args:
        pair (Union[Unset, None, str]):
        info (Union[Unset, None, TradableAssetPairInfo]):  Default:
            TradableAssetPairInfo.INFO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        GetTradableAssetPairsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            pair=pair,
            info=info,
        )
    ).parsed
