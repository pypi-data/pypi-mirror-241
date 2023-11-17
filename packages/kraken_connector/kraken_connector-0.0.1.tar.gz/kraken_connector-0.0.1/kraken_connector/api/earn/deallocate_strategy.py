from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.deallocate_strategy_json_body import DeallocateStrategyJsonBody
from ...schemas.deallocate_strategy_response_200 import DeallocateStrategyResponse200
from ...types import Response


def _get_kwargs(
    *,
    json_body: DeallocateStrategyJsonBody,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/private/Earn/Deallocate",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[DeallocateStrategyResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeallocateStrategyResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[DeallocateStrategyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: HTTPAuthenticatedClient,
    json_body: DeallocateStrategyJsonBody,
) -> Response[DeallocateStrategyResponse200]:
    """Deallocate Earn Funds

     Deallocate funds from a strategy.

    Requires the `Earn Funds` API key permission.
    The amount must always be defined.

    This method is asynchronous. A couple of preflight checks are
    performed synchronously on behalf of the method before it is dispatched
    further. If the method returns HTTP 202 code, the client is required to poll
    the result using the `/Earn/DeallocateStatus` endpoint.

    There can be only one (de)allocation request in progress for given user and
    strategy.  While the operation is in progress:

    1. `pending` attribute in `Allocations` response for the strategy will hold
       the amount that is being deallocated (negative amount)
    2. `pending` attribute in `DeallocateStatus` response will be true.

    Following specific errors within `Earnings` class can be returned by this
    method:
    - Minimum allocation: `EEarnings:Below min:(De)allocation operation amount less than minimum`
      allowed
    - Allocation in progress: `EEarnings:Busy:Another (de)allocation for the same strategy is in
    progress`
    - Strategy not found: `EGeneral:Invalid arguments:Invalid strategy ID`

    Args:
        json_body (DeallocateStrategyJsonBody): Allocation amount in asset specified in the
            strategy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[DeallocateStrategyResponse200]
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
    json_body: DeallocateStrategyJsonBody,
) -> Optional[DeallocateStrategyResponse200]:
    """Deallocate Earn Funds

     Deallocate funds from a strategy.

    Requires the `Earn Funds` API key permission.
    The amount must always be defined.

    This method is asynchronous. A couple of preflight checks are
    performed synchronously on behalf of the method before it is dispatched
    further. If the method returns HTTP 202 code, the client is required to poll
    the result using the `/Earn/DeallocateStatus` endpoint.

    There can be only one (de)allocation request in progress for given user and
    strategy.  While the operation is in progress:

    1. `pending` attribute in `Allocations` response for the strategy will hold
       the amount that is being deallocated (negative amount)
    2. `pending` attribute in `DeallocateStatus` response will be true.

    Following specific errors within `Earnings` class can be returned by this
    method:
    - Minimum allocation: `EEarnings:Below min:(De)allocation operation amount less than minimum`
      allowed
    - Allocation in progress: `EEarnings:Busy:Another (de)allocation for the same strategy is in
    progress`
    - Strategy not found: `EGeneral:Invalid arguments:Invalid strategy ID`

    Args:
        json_body (DeallocateStrategyJsonBody): Allocation amount in asset specified in the
            strategy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        DeallocateStrategyResponse200
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: HTTPAuthenticatedClient,
    json_body: DeallocateStrategyJsonBody,
) -> Response[DeallocateStrategyResponse200]:
    """Deallocate Earn Funds

     Deallocate funds from a strategy.

    Requires the `Earn Funds` API key permission.
    The amount must always be defined.

    This method is asynchronous. A couple of preflight checks are
    performed synchronously on behalf of the method before it is dispatched
    further. If the method returns HTTP 202 code, the client is required to poll
    the result using the `/Earn/DeallocateStatus` endpoint.

    There can be only one (de)allocation request in progress for given user and
    strategy.  While the operation is in progress:

    1. `pending` attribute in `Allocations` response for the strategy will hold
       the amount that is being deallocated (negative amount)
    2. `pending` attribute in `DeallocateStatus` response will be true.

    Following specific errors within `Earnings` class can be returned by this
    method:
    - Minimum allocation: `EEarnings:Below min:(De)allocation operation amount less than minimum`
      allowed
    - Allocation in progress: `EEarnings:Busy:Another (de)allocation for the same strategy is in
    progress`
    - Strategy not found: `EGeneral:Invalid arguments:Invalid strategy ID`

    Args:
        json_body (DeallocateStrategyJsonBody): Allocation amount in asset specified in the
            strategy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[DeallocateStrategyResponse200]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: HTTPAuthenticatedClient,
    json_body: DeallocateStrategyJsonBody,
) -> Optional[DeallocateStrategyResponse200]:
    """Deallocate Earn Funds

     Deallocate funds from a strategy.

    Requires the `Earn Funds` API key permission.
    The amount must always be defined.

    This method is asynchronous. A couple of preflight checks are
    performed synchronously on behalf of the method before it is dispatched
    further. If the method returns HTTP 202 code, the client is required to poll
    the result using the `/Earn/DeallocateStatus` endpoint.

    There can be only one (de)allocation request in progress for given user and
    strategy.  While the operation is in progress:

    1. `pending` attribute in `Allocations` response for the strategy will hold
       the amount that is being deallocated (negative amount)
    2. `pending` attribute in `DeallocateStatus` response will be true.

    Following specific errors within `Earnings` class can be returned by this
    method:
    - Minimum allocation: `EEarnings:Below min:(De)allocation operation amount less than minimum`
      allowed
    - Allocation in progress: `EEarnings:Busy:Another (de)allocation for the same strategy is in
    progress`
    - Strategy not found: `EGeneral:Invalid arguments:Invalid strategy ID`

    Args:
        json_body (DeallocateStrategyJsonBody): Allocation amount in asset specified in the
            strategy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        DeallocateStrategyResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
