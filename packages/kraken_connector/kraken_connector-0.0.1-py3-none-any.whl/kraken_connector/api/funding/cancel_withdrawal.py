from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.cancel_withdrawal_response_200 import CancelWithdrawalResponse200
from ...schemas.request_withdrawal_cancelation_request_body import (
    RequestWithdrawalCancelationRequestBody,
)
from ...types import Response


def _get_kwargs(
    form_data: RequestWithdrawalCancelationRequestBody,
) -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/private/WithdrawCancel",
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[CancelWithdrawalResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CancelWithdrawalResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[CancelWithdrawalResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: RequestWithdrawalCancelationRequestBody,
) -> Response[CancelWithdrawalResponse200]:
    """Request Withdrawal Cancelation

     Cancel a recently requested withdrawal, if it has not already been successfully processed.

    **API Key Permissions Required:** `Funds permissions - Withdraw`, unless withdrawal is a
    `WalletTransfer`, then no permissions are required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[CancelWithdrawalResponse200]
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
    form_data: RequestWithdrawalCancelationRequestBody,
) -> Optional[CancelWithdrawalResponse200]:
    """Request Withdrawal Cancelation

     Cancel a recently requested withdrawal, if it has not already been successfully processed.

    **API Key Permissions Required:** `Funds permissions - Withdraw`, unless withdrawal is a
    `WalletTransfer`, then no permissions are required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        CancelWithdrawalResponse200
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: RequestWithdrawalCancelationRequestBody,
) -> Response[CancelWithdrawalResponse200]:
    """Request Withdrawal Cancelation

     Cancel a recently requested withdrawal, if it has not already been successfully processed.

    **API Key Permissions Required:** `Funds permissions - Withdraw`, unless withdrawal is a
    `WalletTransfer`, then no permissions are required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[CancelWithdrawalResponse200]
    """

    kwargs = _get_kwargs(
        form_data=form_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: RequestWithdrawalCancelationRequestBody,
) -> Optional[CancelWithdrawalResponse200]:
    """Request Withdrawal Cancelation

     Cancel a recently requested withdrawal, if it has not already been successfully processed.

    **API Key Permissions Required:** `Funds permissions - Withdraw`, unless withdrawal is a
    `WalletTransfer`, then no permissions are required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        CancelWithdrawalResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
        )
    ).parsed
