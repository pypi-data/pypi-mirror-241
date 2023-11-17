from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class Info5WithdrawalInfo:
    """Withdrawal Info

    Attributes:
        method (Union[Unset, str]): Name of the withdrawal method that will be used
        limit (Union[Unset, str]): Maximum net amount that can be withdrawn right now
        amount (Union[Unset, str]): Net amount that will be sent, after fees
        fee (Union[Unset, str]): Amount of fees that will be paid
    """

    method: Union[Unset, str] = UNSET
    limit: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    fee: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method = self.method
        limit = self.limit
        amount = self.amount
        fee = self.fee

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if limit is not UNSET:
            field_dict["limit"] = limit
        if amount is not UNSET:
            field_dict["amount"] = amount
        if fee is not UNSET:
            field_dict["fee"] = fee

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        method = d.pop("method", UNSET)

        limit = d.pop("limit", UNSET)

        amount = d.pop("amount", UNSET)

        fee = d.pop("fee", UNSET)

        info_5_withdrawal_info = cls(
            method=method,
            limit=limit,
            amount=amount,
            fee=fee,
        )

        info_5_withdrawal_info.additional_properties = d
        return info_5_withdrawal_info

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
