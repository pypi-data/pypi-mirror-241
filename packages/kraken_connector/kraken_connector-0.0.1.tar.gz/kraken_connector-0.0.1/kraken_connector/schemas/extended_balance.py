from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class ExtendedBalance:
    """Extended Balance

    Attributes:
        balance (Union[Unset, str]): Total balance amount for an asset Example: 3.46840030.
        credit (Union[Unset, str]): Total credit amount (only applicable if account has a credit line) Example:
            1.26844502.
        credit_used (Union[Unset, str]): Used credit amount (only applicable if account has a credit line) Example:
            0.10002300.
        hold_trade (Union[Unset, str]): Total held amount for an asset Example: 2.14560458.
    """

    balance: Union[Unset, str] = UNSET
    credit: Union[Unset, str] = UNSET
    credit_used: Union[Unset, str] = UNSET
    hold_trade: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        balance = self.balance
        credit = self.credit
        credit_used = self.credit_used
        hold_trade = self.hold_trade

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if balance is not UNSET:
            field_dict["balance"] = balance
        if credit is not UNSET:
            field_dict["credit"] = credit
        if credit_used is not UNSET:
            field_dict["credit_used"] = credit_used
        if hold_trade is not UNSET:
            field_dict["hold_trade"] = hold_trade

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        balance = d.pop("balance", UNSET)

        credit = d.pop("credit", UNSET)

        credit_used = d.pop("credit_used", UNSET)

        hold_trade = d.pop("hold_trade", UNSET)

        extended_balance = cls(
            balance=balance,
            credit=credit,
            credit_used=credit_used,
            hold_trade=hold_trade,
        )

        extended_balance.additional_properties = d
        return extended_balance

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
