from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.info_2 import Info2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset: Union[Unset, None, str] = UNSET,
    aclass: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["asset"] = asset

    params["aclass"] = aclass

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/public/Assets",
        "params": params,
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[Info2]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Info2.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[Info2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    asset: Union[Unset, None, str] = UNSET,
    aclass: Union[Unset, None, str] = UNSET,
) -> Response[Info2]:
    """Get Asset Info

     Get information about the assets that are available for deposit, withdrawal, trading and staking.

    Args:
        asset (Union[Unset, None, str]):
        aclass (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Info2]
    """

    kwargs = _get_kwargs(
        asset=asset,
        aclass=aclass,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    asset: Union[Unset, None, str] = UNSET,
    aclass: Union[Unset, None, str] = UNSET,
) -> Optional[Info2]:
    """Get Asset Info

     Get information about the assets that are available for deposit, withdrawal, trading and staking.

    Args:
        asset (Union[Unset, None, str]):
        aclass (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Info2
    """

    return sync_detailed(
        client=client,
        asset=asset,
        aclass=aclass,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    asset: Union[Unset, None, str] = UNSET,
    aclass: Union[Unset, None, str] = UNSET,
) -> Response[Info2]:
    """Get Asset Info

     Get information about the assets that are available for deposit, withdrawal, trading and staking.

    Args:
        asset (Union[Unset, None, str]):
        aclass (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Info2]
    """

    kwargs = _get_kwargs(
        asset=asset,
        aclass=aclass,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    asset: Union[Unset, None, str] = UNSET,
    aclass: Union[Unset, None, str] = UNSET,
) -> Optional[Info2]:
    """Get Asset Info

     Get information about the assets that are available for deposit, withdrawal, trading and staking.

    Args:
        asset (Union[Unset, None, str]):
        aclass (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Info2
    """

    return (
        await asyncio_detailed(
            client=client,
            asset=asset,
            aclass=aclass,
        )
    ).parsed
