from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.depth import Depth
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pair: str,
    count: Union[Unset, None, int] = 100,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["pair"] = pair

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/public/Depth",
        "params": params,
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[Depth]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Depth.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[Depth]:
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
    count: Union[Unset, None, int] = 100,
) -> Response[Depth]:
    """Get Order Book

    Args:
        pair (str):
        count (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Depth]
    """

    kwargs = _get_kwargs(
        pair=pair,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: str,
    count: Union[Unset, None, int] = 100,
) -> Optional[Depth]:
    """Get Order Book

    Args:
        pair (str):
        count (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Depth
    """

    return sync_detailed(
        client=client,
        pair=pair,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: str,
    count: Union[Unset, None, int] = 100,
) -> Response[Depth]:
    """Get Order Book

    Args:
        pair (str):
        count (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Depth]
    """

    kwargs = _get_kwargs(
        pair=pair,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    pair: str,
    count: Union[Unset, None, int] = 100,
) -> Optional[Depth]:
    """Get Order Book

    Args:
        pair (str):
        count (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Depth
    """

    return (
        await asyncio_detailed(
            client=client,
            pair=pair,
            count=count,
        )
    ).parsed
