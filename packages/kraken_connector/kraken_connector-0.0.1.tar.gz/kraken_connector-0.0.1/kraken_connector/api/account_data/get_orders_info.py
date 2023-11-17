from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.query_2 import Query2
from ...schemas.query_orders_info_request_body import QueryOrdersInfoRequestBody
from ...types import Response


def _get_kwargs(
    form_data: QueryOrdersInfoRequestBody,
) -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/private/QueryOrders",
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[Query2]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Query2.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[Query2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: QueryOrdersInfoRequestBody,
) -> Response[Query2]:
    """Query Orders Info

     Retrieve information about specific orders.

    **API Key Permissions Required:** `Orders and trades - Query open orders & trades` or `Orders and
    trades - Query closed orders & trades`, depending on status of order

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Query2]
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
    form_data: QueryOrdersInfoRequestBody,
) -> Optional[Query2]:
    """Query Orders Info

     Retrieve information about specific orders.

    **API Key Permissions Required:** `Orders and trades - Query open orders & trades` or `Orders and
    trades - Query closed orders & trades`, depending on status of order

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Query2
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: QueryOrdersInfoRequestBody,
) -> Response[Query2]:
    """Query Orders Info

     Retrieve information about specific orders.

    **API Key Permissions Required:** `Orders and trades - Query open orders & trades` or `Orders and
    trades - Query closed orders & trades`, depending on status of order

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Query2]
    """

    kwargs = _get_kwargs(
        form_data=form_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: QueryOrdersInfoRequestBody,
) -> Optional[Query2]:
    """Query Orders Info

     Retrieve information about specific orders.

    **API Key Permissions Required:** `Orders and trades - Query open orders & trades` or `Orders and
    trades - Query closed orders & trades`, depending on status of order

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Query2
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
        )
    ).parsed
