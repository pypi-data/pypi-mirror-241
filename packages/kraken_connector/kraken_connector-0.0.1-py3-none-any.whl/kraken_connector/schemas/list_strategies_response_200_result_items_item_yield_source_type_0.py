from typing import Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.earn import (
    YieldSourceType,
)


@_attrs_define
class ListStrategiesResponse200ResultItemsItemYieldSourceType0:
    """Funds are staked on-chain, PoS is the source of yield.

    Attributes:
        type (YieldSourceType.STAKING):
    """

    type: YieldSourceType.STAKING
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        type = YieldSourceType(d.pop("type"))

        list_strategies_response_200_result_items_item_yield_source_type_0 = cls(
            type=type,
        )

        list_strategies_response_200_result_items_item_yield_source_type_0.additional_properties = (
            d
        )
        return list_strategies_response_200_result_items_item_yield_source_type_0

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
