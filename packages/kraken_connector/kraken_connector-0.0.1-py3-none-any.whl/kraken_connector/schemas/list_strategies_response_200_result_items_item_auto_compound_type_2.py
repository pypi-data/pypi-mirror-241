from typing import Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.earn import (
    AutoCompoundType,
)


@_attrs_define
class ListStrategiesResponse200ResultItemsItemAutoCompoundType2:
    """Auto compound depends on user's preference and it comes with default value

    Attributes:
        default (bool):
        type (AutoCompoundType):
    """

    default: bool
    type: AutoCompoundType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default = self.default
        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default": default,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        default = d.pop("default")

        type = AutoCompoundType(d.pop("type"))

        list_strategies_response_200_result_items_item_auto_compound_type_2 = cls(
            default=default,
            type=type,
        )

        list_strategies_response_200_result_items_item_auto_compound_type_2.additional_properties = (
            d
        )
        return list_strategies_response_200_result_items_item_auto_compound_type_2

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
