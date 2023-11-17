from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.get_websockets_token_response_200 import GetWebsocketsTokenResponse200
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/private/GetWebSocketsToken",
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[GetWebsocketsTokenResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetWebsocketsTokenResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[GetWebsocketsTokenResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Response[GetWebsocketsTokenResponse200]:
    """Get Websockets Token

     An authentication token must be requested via this REST API endpoint in order to connect to and
    authenticate with our [Websockets API](https://docs.kraken.com/websockets/#authentication). The
    token should be used within 15 minutes of creation, but it does not expire once a successful
    Websockets connection and private subscription has been made and is maintained.

    **API Key Permissions Required:** `WebSocket interface - On`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[GetWebsocketsTokenResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Optional[GetWebsocketsTokenResponse200]:
    """Get Websockets Token

     An authentication token must be requested via this REST API endpoint in order to connect to and
    authenticate with our [Websockets API](https://docs.kraken.com/websockets/#authentication). The
    token should be used within 15 minutes of creation, but it does not expire once a successful
    Websockets connection and private subscription has been made and is maintained.

    **API Key Permissions Required:** `WebSocket interface - On`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        GetWebsocketsTokenResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Response[GetWebsocketsTokenResponse200]:
    """Get Websockets Token

     An authentication token must be requested via this REST API endpoint in order to connect to and
    authenticate with our [Websockets API](https://docs.kraken.com/websockets/#authentication). The
    token should be used within 15 minutes of creation, but it does not expire once a successful
    Websockets connection and private subscription has been made and is maintained.

    **API Key Permissions Required:** `WebSocket interface - On`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[GetWebsocketsTokenResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
) -> Optional[GetWebsocketsTokenResponse200]:
    """Get Websockets Token

     An authentication token must be requested via this REST API endpoint in order to connect to and
    authenticate with our [Websockets API](https://docs.kraken.com/websockets/#authentication). The
    token should be used within 15 minutes of creation, but it does not expire once a successful
    Websockets connection and private subscription has been made and is maintained.

    **API Key Permissions Required:** `WebSocket interface - On`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        GetWebsocketsTokenResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
