from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.allocate_strategy_json_body import AllocateStrategyJsonBody
from ...schemas.allocate_strategy_response_200 import AllocateStrategyResponse200
from ...types import Response


def _get_kwargs(
    *,
    json_body: AllocateStrategyJsonBody,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/private/Earn/Allocate",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[AllocateStrategyResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AllocateStrategyResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[AllocateStrategyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: HTTPAuthenticatedClient,
    json_body: AllocateStrategyJsonBody,
) -> Response[AllocateStrategyResponse200]:
    """Allocate Earn Funds

     Allocate funds to the Strategy.

    Requires the `Earn Funds` API key permission.
    The amount must always be defined.

    This method is asynchronous. A couple of preflight checks are
    performed synchronously on behalf of the method before it is dispatched
    further. The client is required to poll
    the result using the `/0/private/Earn/AllocateStatus` endpoint.

    There can be only one (de)allocation request in progress for given user and
    strategy at any time. While the operation is in progress:

    1. `pending` attribute in `/Earn/Allocations` response for the strategy
      indicates that funds are being allocated,
    2. `pending` attribute in `/Earn/AllocateStatus` response will be true.

    Following specific errors within `Earnings` class can be returned by this
    method:
    - Minimum allocation: `EEarnings:Below min:(De)allocation operation amount less than minimum`
    - Allocation in progress: `EEarnings:Busy:Another (de)allocation for the same strategy is in
    progress`
    - Service temporarily unavailable: `EEarnings:Busy`. Try again in a few minutes.
    - User tier verification: `EEarnings:Permission denied:The user's tier is not high enough`
    - Strategy not found: `EGeneral:Invalid arguments:Invalid strategy ID`

    Args:
        json_body (AllocateStrategyJsonBody): Allocation amount in asset specified in the strategy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[AllocateStrategyResponse200]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: HTTPAuthenticatedClient,
    json_body: AllocateStrategyJsonBody,
) -> Optional[AllocateStrategyResponse200]:
    """Allocate Earn Funds

     Allocate funds to the Strategy.

    Requires the `Earn Funds` API key permission.
    The amount must always be defined.

    This method is asynchronous. A couple of preflight checks are
    performed synchronously on behalf of the method before it is dispatched
    further. The client is required to poll
    the result using the `/0/private/Earn/AllocateStatus` endpoint.

    There can be only one (de)allocation request in progress for given user and
    strategy at any time. While the operation is in progress:

    1. `pending` attribute in `/Earn/Allocations` response for the strategy
      indicates that funds are being allocated,
    2. `pending` attribute in `/Earn/AllocateStatus` response will be true.

    Following specific errors within `Earnings` class can be returned by this
    method:
    - Minimum allocation: `EEarnings:Below min:(De)allocation operation amount less than minimum`
    - Allocation in progress: `EEarnings:Busy:Another (de)allocation for the same strategy is in
    progress`
    - Service temporarily unavailable: `EEarnings:Busy`. Try again in a few minutes.
    - User tier verification: `EEarnings:Permission denied:The user's tier is not high enough`
    - Strategy not found: `EGeneral:Invalid arguments:Invalid strategy ID`

    Args:
        json_body (AllocateStrategyJsonBody): Allocation amount in asset specified in the strategy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        AllocateStrategyResponse200
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: HTTPAuthenticatedClient,
    json_body: AllocateStrategyJsonBody,
) -> Response[AllocateStrategyResponse200]:
    """Allocate Earn Funds

     Allocate funds to the Strategy.

    Requires the `Earn Funds` API key permission.
    The amount must always be defined.

    This method is asynchronous. A couple of preflight checks are
    performed synchronously on behalf of the method before it is dispatched
    further. The client is required to poll
    the result using the `/0/private/Earn/AllocateStatus` endpoint.

    There can be only one (de)allocation request in progress for given user and
    strategy at any time. While the operation is in progress:

    1. `pending` attribute in `/Earn/Allocations` response for the strategy
      indicates that funds are being allocated,
    2. `pending` attribute in `/Earn/AllocateStatus` response will be true.

    Following specific errors within `Earnings` class can be returned by this
    method:
    - Minimum allocation: `EEarnings:Below min:(De)allocation operation amount less than minimum`
    - Allocation in progress: `EEarnings:Busy:Another (de)allocation for the same strategy is in
    progress`
    - Service temporarily unavailable: `EEarnings:Busy`. Try again in a few minutes.
    - User tier verification: `EEarnings:Permission denied:The user's tier is not high enough`
    - Strategy not found: `EGeneral:Invalid arguments:Invalid strategy ID`

    Args:
        json_body (AllocateStrategyJsonBody): Allocation amount in asset specified in the strategy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[AllocateStrategyResponse200]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: HTTPAuthenticatedClient,
    json_body: AllocateStrategyJsonBody,
) -> Optional[AllocateStrategyResponse200]:
    """Allocate Earn Funds

     Allocate funds to the Strategy.

    Requires the `Earn Funds` API key permission.
    The amount must always be defined.

    This method is asynchronous. A couple of preflight checks are
    performed synchronously on behalf of the method before it is dispatched
    further. The client is required to poll
    the result using the `/0/private/Earn/AllocateStatus` endpoint.

    There can be only one (de)allocation request in progress for given user and
    strategy at any time. While the operation is in progress:

    1. `pending` attribute in `/Earn/Allocations` response for the strategy
      indicates that funds are being allocated,
    2. `pending` attribute in `/Earn/AllocateStatus` response will be true.

    Following specific errors within `Earnings` class can be returned by this
    method:
    - Minimum allocation: `EEarnings:Below min:(De)allocation operation amount less than minimum`
    - Allocation in progress: `EEarnings:Busy:Another (de)allocation for the same strategy is in
    progress`
    - Service temporarily unavailable: `EEarnings:Busy`. Try again in a few minutes.
    - User tier verification: `EEarnings:Permission denied:The user's tier is not high enough`
    - Strategy not found: `EGeneral:Invalid arguments:Invalid strategy ID`

    Args:
        json_body (AllocateStrategyJsonBody): Allocation amount in asset specified in the strategy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        AllocateStrategyResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
