from typing import Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.earn import (
    StrategyLockType,
)


@_attrs_define
class ListStrategiesResponse200ResultItemsItemLockTypeType0:
    """Either the whole asset balance or part of it is allocated to earn strategy and users are free to deallocate it
    anytime and most importantly the deallocation can be implicit (triggered by a trade, withdrawal from exchange,
    etc.).

        Attributes:
            type (StrategyLockType.FLEX):
    """

    type: StrategyLockType.FLEX
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
        type = StrategyLockType(d.pop("type"))

        list_strategies_response_200_result_items_item_lock_type_type_0 = cls(
            type=type,
        )

        list_strategies_response_200_result_items_item_lock_type_type_0.additional_properties = (
            d
        )
        return list_strategies_response_200_result_items_item_lock_type_type_0

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
