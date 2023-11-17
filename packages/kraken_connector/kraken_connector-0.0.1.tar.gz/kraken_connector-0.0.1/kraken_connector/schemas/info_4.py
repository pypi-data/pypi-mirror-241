from typing import Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field


@_attrs_define
class Info4:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        asset (str): Asset being withdrawn
        key (str): Withdrawal key name, as set up on your account
        amount (str): Amount to be withdrawn
    """

    nonce: int
    asset: str
    key: str
    amount: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        asset = self.asset
        key = self.key
        amount = self.amount

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

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        asset = d.pop("asset")

        key = d.pop("key")

        amount = d.pop("amount")

        info_4 = cls(
            nonce=nonce,
            asset=asset,
            key=key,
            amount=amount,
        )

        info_4.additional_properties = d
        return info_4

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
