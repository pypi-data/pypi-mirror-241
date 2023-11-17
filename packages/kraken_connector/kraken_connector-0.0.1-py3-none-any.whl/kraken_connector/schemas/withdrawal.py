from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class Withdrawal:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        asset (str): Asset being withdrawn
        key (str): Withdrawal key name, as set up on your account
        amount (str): Amount to be withdrawn
        address (Union[Unset, str]): Optional, crypto address that can be used to confirm address matches key (will
            return `Invalid withdrawal address` error if different)
        max_fee (Union[Unset, str]): Optional, if the processed withdrawal fee is higher than `max_fee`, withdrawal will
            fail with `EFunding:Max fee exceeded`
    """

    nonce: int
    asset: str
    key: str
    amount: str
    address: Union[Unset, str] = UNSET
    max_fee: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        asset = self.asset
        key = self.key
        amount = self.amount
        address = self.address
        max_fee = self.max_fee

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "asset": asset,
                "key": key,
                "amount": amount,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if max_fee is not UNSET:
            field_dict["max_fee"] = max_fee

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        asset = d.pop("asset")

        key = d.pop("key")

        amount = d.pop("amount")

        address = d.pop("address", UNSET)

        max_fee = d.pop("max_fee", UNSET)

        withdrawal = cls(
            nonce=nonce,
            asset=asset,
            key=key,
            amount=amount,
            address=address,
            max_fee=max_fee,
        )

        withdrawal.additional_properties = d
        return withdrawal

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
