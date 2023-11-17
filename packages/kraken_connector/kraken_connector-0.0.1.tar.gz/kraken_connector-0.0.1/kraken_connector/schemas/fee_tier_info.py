from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class FeeTierInfo:
    """Fee Tier Info

    Attributes:
        fee (Union[Unset, str]): Current fee (in percent)
        min_fee (Union[Unset, str]): minimum fee for pair (if not fixed fee)
        max_fee (Union[Unset, str]): maximum fee for pair (if not fixed fee)
        next_fee (Union[Unset, None, str]): next tier's fee for pair (if not fixed fee,  null if at lowest fee tier)
        tier_volume (Union[Unset, None, str]): volume level of current tier (if not fixed fee. null if at lowest fee
            tier)
        next_volume (Union[Unset, None, str]): volume level of next tier (if not fixed fee. null if at lowest fee tier)
    """

    fee: Union[Unset, str] = UNSET
    min_fee: Union[Unset, str] = UNSET
    max_fee: Union[Unset, str] = UNSET
    next_fee: Union[Unset, None, str] = UNSET
    tier_volume: Union[Unset, None, str] = UNSET
    next_volume: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fee = self.fee
        min_fee = self.min_fee
        max_fee = self.max_fee
        next_fee = self.next_fee
        tier_volume = self.tier_volume
        next_volume = self.next_volume

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fee is not UNSET:
            field_dict["fee"] = fee
        if min_fee is not UNSET:
            field_dict["min_fee"] = min_fee
        if max_fee is not UNSET:
            field_dict["max_fee"] = max_fee
        if next_fee is not UNSET:
            field_dict["next_fee"] = next_fee
        if tier_volume is not UNSET:
            field_dict["tier_volume"] = tier_volume
        if next_volume is not UNSET:
            field_dict["next_volume"] = next_volume

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        fee = d.pop("fee", UNSET)

        min_fee = d.pop("min_fee", UNSET)

        max_fee = d.pop("max_fee", UNSET)

        next_fee = d.pop("next_fee", UNSET)

        tier_volume = d.pop("tier_volume", UNSET)

        next_volume = d.pop("next_volume", UNSET)

        fee_tier_info = cls(
            fee=fee,
            min_fee=min_fee,
            max_fee=max_fee,
            next_fee=next_fee,
            tier_volume=tier_volume,
            next_volume=next_volume,
        )

        fee_tier_info.additional_properties = d
        return fee_tier_info

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
