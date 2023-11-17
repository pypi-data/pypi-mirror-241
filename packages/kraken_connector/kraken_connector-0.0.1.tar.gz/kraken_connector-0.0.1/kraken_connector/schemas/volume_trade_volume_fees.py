from typing import TYPE_CHECKING, Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..schemas.fee_tier_info import FeeTierInfo


@_attrs_define
class VolumeTradeVolumeFees:
    """ """

    additional_properties: Dict[str, "FeeTierInfo"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.fee_tier_info import FeeTierInfo

        d = src_dict.copy()
        volume_trade_volume_fees = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = FeeTierInfo.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        volume_trade_volume_fees.additional_properties = additional_properties
        return volume_trade_volume_fees

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "FeeTierInfo":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "FeeTierInfo") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
