from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import exceptions
from ...http import HTTPAuthenticatedClient, HTTPClient
from ...schemas.get_desposit_methods_request_body import GetDespositMethodsRequestBody
from ...schemas.methods_2 import Methods2
from ...types import Response


def _get_kwargs(
    form_data: GetDespositMethodsRequestBody,
) -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/private/DepositMethods",
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Optional[Methods2]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Methods2.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise exceptions.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[HTTPAuthenticatedClient, HTTPClient], response: httpx.Response
) -> Response[Methods2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: GetDespositMethodsRequestBody,
) -> Response[Methods2]:
    """Get Deposit Methods

     Retrieve methods available for depositing a particular asset.

    **API Key Permissions Required:** `Funds permissions - Query` and `Funds permissions - Deposit`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Methods2]
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
    form_data: GetDespositMethodsRequestBody,
) -> Optional[Methods2]:
    """Get Deposit Methods

     Retrieve methods available for depositing a particular asset.

    **API Key Permissions Required:** `Funds permissions - Query` and `Funds permissions - Deposit`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Methods2
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: GetDespositMethodsRequestBody,
) -> Response[Methods2]:
    """Get Deposit Methods

     Retrieve methods available for depositing a particular asset.

    **API Key Permissions Required:** `Funds permissions - Query` and `Funds permissions - Deposit`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Response[Methods2]
    """

    kwargs = _get_kwargs(
        form_data=form_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[HTTPAuthenticatedClient, HTTPClient],
    form_data: GetDespositMethodsRequestBody,
) -> Optional[Methods2]:
    """Get Deposit Methods

     Retrieve methods available for depositing a particular asset.

    **API Key Permissions Required:** `Funds permissions - Query` and `Funds permissions - Deposit`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and HTTPClient.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than HTTPClient.timeout.

    Returns:
        Methods2
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
        )
    ).parsed
