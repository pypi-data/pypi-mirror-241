from typing import TYPE_CHECKING, Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.extended_balance import ExtendedBalance


@_attrs_define
class Balanceex2ExtendedBalance:
    """Extended Balance

    Attributes:
        asset (Union[Unset, ExtendedBalance]): Extended Balance
    """

    asset: Union[Unset, "ExtendedBalance"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.asset, Unset):
            asset = self.asset.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset is not UNSET:
            field_dict["asset"] = asset

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.extended_balance import ExtendedBalance

        d = src_dict.copy()
        _asset = d.pop("asset", UNSET)
        asset: Union[Unset, ExtendedBalance]
        if isinstance(_asset, Unset):
            asset = UNSET
        else:
            asset = ExtendedBalance.from_dict(_asset)

        balanceex_2_extended_balance = cls(
            asset=asset,
        )

        balanceex_2_extended_balance.additional_properties = d
        return balanceex_2_extended_balance

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
