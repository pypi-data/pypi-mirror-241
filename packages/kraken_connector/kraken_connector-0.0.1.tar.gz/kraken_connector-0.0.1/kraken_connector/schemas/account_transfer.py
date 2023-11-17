from typing import Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class AccountTransferResponse:
    """
    Attributes:
        result (Union[Unset, AccountTransferResult]):
        error (Union[Unset, List[str]]):
    """

    result: Union[Unset, "AccountTransferResult"] = UNSET
    error: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        error: Union[Unset, List[str]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.account_transfer import AccountTransferResult

        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, AccountTransferResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = AccountTransferResult.from_dict(_result)

        error = cast(List[str], d.pop("error", UNSET))

        account_transfer = cls(
            result=result,
            error=error,
        )

        account_transfer.additional_properties = d
        return account_transfer

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


@_attrs_define
class AccountTransferResult:
    """
    Attributes:
        transfer_id (Union[Unset, str]): Transfer ID
        status (Union[Unset, str]): Transfer status, either `"pending"` or `"complete"`
    """

    transfer_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transfer_id = self.transfer_id
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transfer_id is not UNSET:
            field_dict["transfer_id"] = transfer_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        transfer_id = d.pop("transfer_id", UNSET)

        status = d.pop("status", UNSET)

        account_transfer = cls(
            transfer_id=transfer_id,
            status=status,
        )

        account_transfer.additional_properties = d
        return account_transfer

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


@_attrs_define
class AccountTransferRequest:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        asset (str): Asset being transferred
        amount (str): Amount of asset to transfer
        from_ (str): IIBAN of the source account
        to (str): IIBAN of the destination account
    """

    nonce: int
    asset: str
    amount: str
    from_: str
    to: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        asset = self.asset
        amount = self.amount
        from_ = self.from_
        to = self.to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "asset": asset,
                "amount": amount,
                "from": from_,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        asset = d.pop("asset")

        amount = d.pop("amount")

        from_ = d.pop("from")

        to = d.pop("to")

        account_transfer = cls(
            nonce=nonce,
            asset=asset,
            amount=amount,
            from_=from_,
            to=to,
        )

        account_transfer.additional_properties = d
        return account_transfer

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
