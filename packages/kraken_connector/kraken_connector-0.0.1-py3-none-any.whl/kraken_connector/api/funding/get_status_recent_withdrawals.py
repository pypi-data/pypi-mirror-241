from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.get_status_of_recent_withdrawals_request_body import (
    GetStatusOfRecentWithdrawalsRequestBody,
)
from ...types import Response


def _get_kwargs(
    form_data: GetStatusOfRecentWithdrawalsRequestBody,
) -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/private/WithdrawStatus",
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: GetStatusOfRecentWithdrawalsRequestBody,
) -> Response[Any]:
    """Get Status of Recent Withdrawals

     Retrieve information about recent withdrawals. Any withdrawals initiated in the past 90 days will be
    included in the response, up to a maximum of 500 results, sorted by recency.

    **API Key Permissions Required:** `Funds permissions - Withdraw` or `Data - Query ledger entries`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        form_data=form_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: GetStatusOfRecentWithdrawalsRequestBody,
) -> Response[Any]:
    """Get Status of Recent Withdrawals

     Retrieve information about recent withdrawals. Any withdrawals initiated in the past 90 days will be
    included in the response, up to a maximum of 500 results, sorted by recency.

    **API Key Permissions Required:** `Funds permissions - Withdraw` or `Data - Query ledger entries`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        form_data=form_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
