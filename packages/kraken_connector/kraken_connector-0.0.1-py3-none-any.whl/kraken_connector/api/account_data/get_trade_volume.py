from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.volume import Volume
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/private/TradeVolume",
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[Volume]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Volume.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[Volume]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Response[Volume]:
    """Get Trade Volume

     Returns 30 day USD trading volume and resulting fee schedule for any asset pair(s) provided.
    Note: If an asset pair is on a maker/taker fee schedule, the taker side is given in `fees` and maker
    side in `fees_maker`. For pairs not on maker/taker, they will only be given in `fees`.

    **API Key Permissions Required:** `Funds permissions - Query`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Volume]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Optional[Volume]:
    """Get Trade Volume

     Returns 30 day USD trading volume and resulting fee schedule for any asset pair(s) provided.
    Note: If an asset pair is on a maker/taker fee schedule, the taker side is given in `fees` and maker
    side in `fees_maker`. For pairs not on maker/taker, they will only be given in `fees`.

    **API Key Permissions Required:** `Funds permissions - Query`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Volume
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Response[Volume]:
    """Get Trade Volume

     Returns 30 day USD trading volume and resulting fee schedule for any asset pair(s) provided.
    Note: If an asset pair is on a maker/taker fee schedule, the taker side is given in `fees` and maker
    side in `fees_maker`. For pairs not on maker/taker, they will only be given in `fees`.

    **API Key Permissions Required:** `Funds permissions - Query`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Volume]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Optional[Volume]:
    """Get Trade Volume

     Returns 30 day USD trading volume and resulting fee schedule for any asset pair(s) provided.
    Note: If an asset pair is on a maker/taker fee schedule, the taker side is given in `fees` and maker
    side in `fees_maker`. For pairs not on maker/taker, they will only be given in `fees`.

    **API Key Permissions Required:** `Funds permissions - Query`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Volume
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
