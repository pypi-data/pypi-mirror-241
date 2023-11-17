from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class AssetInfo:
    """Asset Info

    Attributes:
        aclass (Union[Unset, str]): Asset Class
        altname (Union[Unset, str]): Alternate name
        decimals (Union[Unset, int]): Scaling decimal places for record keeping
        display_decimals (Union[Unset, int]): Scaling decimal places for output display
        collateral_value (Union[Unset, float]): Valuation as margin collateral (if applicable)
        status (Union[Unset, str]): Status of asset. Possible values: `enabled`, `deposit_only`, `withdrawal_only`,
            `funding_temporarily_disabled`.
    """

    aclass: Union[Unset, str] = UNSET
    altname: Union[Unset, str] = UNSET
    decimals: Union[Unset, int] = UNSET
    display_decimals: Union[Unset, int] = UNSET
    collateral_value: Union[Unset, float] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aclass = self.aclass
        altname = self.altname
        decimals = self.decimals
        display_decimals = self.display_decimals
        collateral_value = self.collateral_value
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aclass is not UNSET:
            field_dict["aclass"] = aclass
        if altname is not UNSET:
            field_dict["altname"] = altname
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if display_decimals is not UNSET:
            field_dict["display_decimals"] = display_decimals
        if collateral_value is not UNSET:
            field_dict["collateral_value"] = collateral_value
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        aclass = d.pop("aclass", UNSET)

        altname = d.pop("altname", UNSET)

        decimals = d.pop("decimals", UNSET)

        display_decimals = d.pop("display_decimals", UNSET)

        collateral_value = d.pop("collateral_value", UNSET)

        status = d.pop("status", UNSET)

        asset_info = cls(
            aclass=aclass,
            altname=altname,
            decimals=decimals,
            display_decimals=display_decimals,
            collateral_value=collateral_value,
            status=status,
        )

        asset_info.additional_properties = d
        return asset_info

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
