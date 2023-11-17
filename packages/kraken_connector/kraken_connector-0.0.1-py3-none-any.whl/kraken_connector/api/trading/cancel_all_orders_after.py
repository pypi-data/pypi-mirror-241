from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.cancel_all_orders_after_data import CancelAllOrdersAfterData
from ...schemas.cancel_all_orders_after_response_200 import (
    CancelAllOrdersAfterResponse200,
)
from ...types import Response


def _get_kwargs(
    form_data: CancelAllOrdersAfterData,
) -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/private/CancelAllOrdersAfter",
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[CancelAllOrdersAfterResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CancelAllOrdersAfterResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[CancelAllOrdersAfterResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: CancelAllOrdersAfterData,
) -> Response[CancelAllOrdersAfterResponse200]:
    r"""Cancel All Orders After X

     CancelAllOrdersAfter provides a \"Dead Man's Switch\" mechanism to protect the client from network
    malfunction, extreme latency or unexpected matching engine downtime. The client can send a request
    with a timeout (in seconds), that will start a countdown timer which will cancel *all* client orders
    when the timer expires. The client has to keep sending new requests to push back the trigger time,
    or deactivate the mechanism by specifying a timeout of 0. If the timer expires, all orders are
    cancelled and then the timer remains disabled until the client provides a new (non-zero) timeout.

    The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds.
    This allows the client to keep the orders in place in case of a brief disconnection or transient
    delay, while keeping them safe in case of a network breakdown. It is also recommended to disable the
    timer ahead of regularly scheduled trading engine maintenance (if the timer is enabled, all orders
    will be cancelled when the trading engine comes back from downtime - planned or otherwise).

    **API Key Permissions Required:** `Orders and trades - Create & modify orders` and `Orders and
    trades - Cancel & close orders`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[CancelAllOrdersAfterResponse200]
    """

    kwargs = _get_kwargs(
        form_data=form_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: CancelAllOrdersAfterData,
) -> Optional[CancelAllOrdersAfterResponse200]:
    r"""Cancel All Orders After X

     CancelAllOrdersAfter provides a \"Dead Man's Switch\" mechanism to protect the client from network
    malfunction, extreme latency or unexpected matching engine downtime. The client can send a request
    with a timeout (in seconds), that will start a countdown timer which will cancel *all* client orders
    when the timer expires. The client has to keep sending new requests to push back the trigger time,
    or deactivate the mechanism by specifying a timeout of 0. If the timer expires, all orders are
    cancelled and then the timer remains disabled until the client provides a new (non-zero) timeout.

    The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds.
    This allows the client to keep the orders in place in case of a brief disconnection or transient
    delay, while keeping them safe in case of a network breakdown. It is also recommended to disable the
    timer ahead of regularly scheduled trading engine maintenance (if the timer is enabled, all orders
    will be cancelled when the trading engine comes back from downtime - planned or otherwise).

    **API Key Permissions Required:** `Orders and trades - Create & modify orders` and `Orders and
    trades - Cancel & close orders`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        CancelAllOrdersAfterResponse200
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: CancelAllOrdersAfterData,
) -> Response[CancelAllOrdersAfterResponse200]:
    r"""Cancel All Orders After X

     CancelAllOrdersAfter provides a \"Dead Man's Switch\" mechanism to protect the client from network
    malfunction, extreme latency or unexpected matching engine downtime. The client can send a request
    with a timeout (in seconds), that will start a countdown timer which will cancel *all* client orders
    when the timer expires. The client has to keep sending new requests to push back the trigger time,
    or deactivate the mechanism by specifying a timeout of 0. If the timer expires, all orders are
    cancelled and then the timer remains disabled until the client provides a new (non-zero) timeout.

    The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds.
    This allows the client to keep the orders in place in case of a brief disconnection or transient
    delay, while keeping them safe in case of a network breakdown. It is also recommended to disable the
    timer ahead of regularly scheduled trading engine maintenance (if the timer is enabled, all orders
    will be cancelled when the trading engine comes back from downtime - planned or otherwise).

    **API Key Permissions Required:** `Orders and trades - Create & modify orders` and `Orders and
    trades - Cancel & close orders`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[CancelAllOrdersAfterResponse200]
    """

    kwargs = _get_kwargs(
        form_data=form_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: CancelAllOrdersAfterData,
) -> Optional[CancelAllOrdersAfterResponse200]:
    r"""Cancel All Orders After X

     CancelAllOrdersAfter provides a \"Dead Man's Switch\" mechanism to protect the client from network
    malfunction, extreme latency or unexpected matching engine downtime. The client can send a request
    with a timeout (in seconds), that will start a countdown timer which will cancel *all* client orders
    when the timer expires. The client has to keep sending new requests to push back the trigger time,
    or deactivate the mechanism by specifying a timeout of 0. If the timer expires, all orders are
    cancelled and then the timer remains disabled until the client provides a new (non-zero) timeout.

    The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds.
    This allows the client to keep the orders in place in case of a brief disconnection or transient
    delay, while keeping them safe in case of a network breakdown. It is also recommended to disable the
    timer ahead of regularly scheduled trading engine maintenance (if the timer is enabled, all orders
    will be cancelled when the trading engine comes back from downtime - planned or otherwise).

    **API Key Permissions Required:** `Orders and trades - Create & modify orders` and `Orders and
    trades - Cancel & close orders`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        CancelAllOrdersAfterResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
        )
    ).parsed
