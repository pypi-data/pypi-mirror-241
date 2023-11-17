from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.list_allocations_json_body import ListAllocationsJsonBody
from ...schemas.list_allocations_response_200 import ListAllocationsResponse200
from ...types import Response


def _get_kwargs(
    *,
    json_body: ListAllocationsJsonBody,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/private/Earn/Allocations",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[ListAllocationsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListAllocationsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[ListAllocationsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: HTTPAuthenticatedClient,
    json_body: ListAllocationsJsonBody,
) -> Response[ListAllocationsResponse200]:
    """List Earn Allocations

     List all allocations for the user.

    Requires the `Query Funds` API key permission.

    By default all allocations are returned, even for strategies that have been
    used in the past and have zero balance now. That is so that the user can see
    how much was earned with given strategy in the past.
    `hide_zero_allocations` parameter can be used to remove zero balance entries
    from the output.  Paging hasn't been implemented for this method as we don't
    expect the result for a particular user to be overwhelmingly large.

    All amounts in the output can be denominated in a currency of user's choice
    (the `converted_asset` parameter).

    Information about when the next reward will be paid to the client is also
    provided in the output.

    Allocated funds can be in up to 4 states:
    - bonding
    - allocated
    - exit_queue (ETH only)
    - unbonding

    Any funds in `total` not in `bonding`/`unbonding` are simply allocated and
    earning rewards. Depending on the strategy funds in the other 3 states can
    also be earning rewards. Consult the output of `/Earn/Strategies` to know
    whether `bonding`/`unbonding` earn rewards. `ETH` in `exit_queue` still
    earns rewards.

    Note that for `ETH`, when the funds are in the `exit_queue` state, the
    `expires` time given is the time when the funds will have finished
    unbonding, not when they go from exit queue to unbonding.

    (Un)bonding time estimate can be inaccurate right after having (de)allocated the
    funds. Wait 1-2 minutes after (de)allocating to get an accurate result.

    Args:
        json_body (ListAllocationsJsonBody): Page request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[ListAllocationsResponse200]
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
    json_body: ListAllocationsJsonBody,
) -> Optional[ListAllocationsResponse200]:
    """List Earn Allocations

     List all allocations for the user.

    Requires the `Query Funds` API key permission.

    By default all allocations are returned, even for strategies that have been
    used in the past and have zero balance now. That is so that the user can see
    how much was earned with given strategy in the past.
    `hide_zero_allocations` parameter can be used to remove zero balance entries
    from the output.  Paging hasn't been implemented for this method as we don't
    expect the result for a particular user to be overwhelmingly large.

    All amounts in the output can be denominated in a currency of user's choice
    (the `converted_asset` parameter).

    Information about when the next reward will be paid to the client is also
    provided in the output.

    Allocated funds can be in up to 4 states:
    - bonding
    - allocated
    - exit_queue (ETH only)
    - unbonding

    Any funds in `total` not in `bonding`/`unbonding` are simply allocated and
    earning rewards. Depending on the strategy funds in the other 3 states can
    also be earning rewards. Consult the output of `/Earn/Strategies` to know
    whether `bonding`/`unbonding` earn rewards. `ETH` in `exit_queue` still
    earns rewards.

    Note that for `ETH`, when the funds are in the `exit_queue` state, the
    `expires` time given is the time when the funds will have finished
    unbonding, not when they go from exit queue to unbonding.

    (Un)bonding time estimate can be inaccurate right after having (de)allocated the
    funds. Wait 1-2 minutes after (de)allocating to get an accurate result.

    Args:
        json_body (ListAllocationsJsonBody): Page request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        ListAllocationsResponse200
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: HTTPAuthenticatedClient,
    json_body: ListAllocationsJsonBody,
) -> Response[ListAllocationsResponse200]:
    """List Earn Allocations

     List all allocations for the user.

    Requires the `Query Funds` API key permission.

    By default all allocations are returned, even for strategies that have been
    used in the past and have zero balance now. That is so that the user can see
    how much was earned with given strategy in the past.
    `hide_zero_allocations` parameter can be used to remove zero balance entries
    from the output.  Paging hasn't been implemented for this method as we don't
    expect the result for a particular user to be overwhelmingly large.

    All amounts in the output can be denominated in a currency of user's choice
    (the `converted_asset` parameter).

    Information about when the next reward will be paid to the client is also
    provided in the output.

    Allocated funds can be in up to 4 states:
    - bonding
    - allocated
    - exit_queue (ETH only)
    - unbonding

    Any funds in `total` not in `bonding`/`unbonding` are simply allocated and
    earning rewards. Depending on the strategy funds in the other 3 states can
    also be earning rewards. Consult the output of `/Earn/Strategies` to know
    whether `bonding`/`unbonding` earn rewards. `ETH` in `exit_queue` still
    earns rewards.

    Note that for `ETH`, when the funds are in the `exit_queue` state, the
    `expires` time given is the time when the funds will have finished
    unbonding, not when they go from exit queue to unbonding.

    (Un)bonding time estimate can be inaccurate right after having (de)allocated the
    funds. Wait 1-2 minutes after (de)allocating to get an accurate result.

    Args:
        json_body (ListAllocationsJsonBody): Page request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[ListAllocationsResponse200]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: HTTPAuthenticatedClient,
    json_body: ListAllocationsJsonBody,
) -> Optional[ListAllocationsResponse200]:
    """List Earn Allocations

     List all allocations for the user.

    Requires the `Query Funds` API key permission.

    By default all allocations are returned, even for strategies that have been
    used in the past and have zero balance now. That is so that the user can see
    how much was earned with given strategy in the past.
    `hide_zero_allocations` parameter can be used to remove zero balance entries
    from the output.  Paging hasn't been implemented for this method as we don't
    expect the result for a particular user to be overwhelmingly large.

    All amounts in the output can be denominated in a currency of user's choice
    (the `converted_asset` parameter).

    Information about when the next reward will be paid to the client is also
    provided in the output.

    Allocated funds can be in up to 4 states:
    - bonding
    - allocated
    - exit_queue (ETH only)
    - unbonding

    Any funds in `total` not in `bonding`/`unbonding` are simply allocated and
    earning rewards. Depending on the strategy funds in the other 3 states can
    also be earning rewards. Consult the output of `/Earn/Strategies` to know
    whether `bonding`/`unbonding` earn rewards. `ETH` in `exit_queue` still
    earns rewards.

    Note that for `ETH`, when the funds are in the `exit_queue` state, the
    `expires` time given is the time when the funds will have finished
    unbonding, not when they go from exit queue to unbonding.

    (Un)bonding time estimate can be inaccurate right after having (de)allocated the
    funds. Wait 1-2 minutes after (de)allocating to get an accurate result.

    Args:
        json_body (ListAllocationsJsonBody): Page request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        ListAllocationsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
