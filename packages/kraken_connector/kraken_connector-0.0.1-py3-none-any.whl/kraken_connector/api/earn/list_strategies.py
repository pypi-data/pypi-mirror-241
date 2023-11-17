from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.list_strategies_json_body import ListStrategiesJsonBody
from ...schemas.list_strategies_response_200 import ListStrategiesResponse200
from ...types import Response


def _get_kwargs(
    *,
    json_body: ListStrategiesJsonBody,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/private/Earn/Strategies",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[ListStrategiesResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListStrategiesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[ListStrategiesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: HTTPAuthenticatedClient,
    json_body: ListStrategiesJsonBody,
) -> Response[ListStrategiesResponse200]:
    """List Earn Strategies

     List earn strategies along with their parameters.

    Requires a valid API key but not specific permission is required.

    Returns only strategies that are available to the user
    based on geographic region.

    When the user does not meet the tier restriction, `can_allocate` will be
    false and `allocation_restriction_info` indicates `Tier` as the restriction
    reason. Earn products generally require Intermediate tier. Get your account verified
    to access earn.

    Paging isn't yet implemented, so it the endpoint always returns all
    data in the first page.

    Args:
        json_body (ListStrategiesJsonBody): List strategies parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[ListStrategiesResponse200]
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
    json_body: ListStrategiesJsonBody,
) -> Optional[ListStrategiesResponse200]:
    """List Earn Strategies

     List earn strategies along with their parameters.

    Requires a valid API key but not specific permission is required.

    Returns only strategies that are available to the user
    based on geographic region.

    When the user does not meet the tier restriction, `can_allocate` will be
    false and `allocation_restriction_info` indicates `Tier` as the restriction
    reason. Earn products generally require Intermediate tier. Get your account verified
    to access earn.

    Paging isn't yet implemented, so it the endpoint always returns all
    data in the first page.

    Args:
        json_body (ListStrategiesJsonBody): List strategies parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        ListStrategiesResponse200
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: HTTPAuthenticatedClient,
    json_body: ListStrategiesJsonBody,
) -> Response[ListStrategiesResponse200]:
    """List Earn Strategies

     List earn strategies along with their parameters.

    Requires a valid API key but not specific permission is required.

    Returns only strategies that are available to the user
    based on geographic region.

    When the user does not meet the tier restriction, `can_allocate` will be
    false and `allocation_restriction_info` indicates `Tier` as the restriction
    reason. Earn products generally require Intermediate tier. Get your account verified
    to access earn.

    Paging isn't yet implemented, so it the endpoint always returns all
    data in the first page.

    Args:
        json_body (ListStrategiesJsonBody): List strategies parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[ListStrategiesResponse200]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: HTTPAuthenticatedClient,
    json_body: ListStrategiesJsonBody,
) -> Optional[ListStrategiesResponse200]:
    """List Earn Strategies

     List earn strategies along with their parameters.

    Requires a valid API key but not specific permission is required.

    Returns only strategies that are available to the user
    based on geographic region.

    When the user does not meet the tier restriction, `can_allocate` will be
    false and `allocation_restriction_info` indicates `Tier` as the restriction
    reason. Earn products generally require Intermediate tier. Get your account verified
    to access earn.

    Paging isn't yet implemented, so it the endpoint always returns all
    data in the first page.

    Args:
        json_body (ListStrategiesJsonBody): List strategies parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        ListStrategiesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
