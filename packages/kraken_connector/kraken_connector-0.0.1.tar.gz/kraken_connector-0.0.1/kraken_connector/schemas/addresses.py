from typing import Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class Addresses:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        asset (str): Asset being deposited
        method (str): Name of the deposit method
        new (Union[Unset, bool]): Whether or not to generate a new address
        amount (Union[Unset, float, int, str]): Amount you wish to deposit (only required for `method=Bitcoin
            Lightning`)
    """

    nonce: int
    asset: str
    method: str
    new: Union[Unset, bool] = False
    amount: Union[Unset, float, int, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        asset = self.asset
        method = self.method
        new = self.new
        amount: Union[Unset, float, int, str]
        amount = UNSET if isinstance(self.amount, Unset) else self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "asset": asset,
                "method": method,
            }
        )
        if new is not UNSET:
            field_dict["new"] = new
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        asset = d.pop("asset")

        method = d.pop("method")

        new = d.pop("new", UNSET)

        def _parse_amount(data: object) -> Union[Unset, float, int, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, int, str], data)

        amount = _parse_amount(d.pop("amount", UNSET))

        addresses = cls(
            nonce=nonce,
            asset=asset,
            method=method,
            new=new,
            amount=amount,
        )

        addresses.additional_properties = d
        return addresses

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
