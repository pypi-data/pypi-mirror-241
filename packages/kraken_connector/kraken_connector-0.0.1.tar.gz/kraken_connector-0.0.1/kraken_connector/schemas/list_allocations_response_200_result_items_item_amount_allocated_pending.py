from typing import Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field


@_attrs_define
class ListAllocationsResponse200ResultItemsItemAmountAllocatedPending:
    """Pending allocation amount - can be negative if the pending operation is deallocation

    Attributes:
        converted (str): Amount converted into the requested asset
        native (str): Amount in the native asset
    """

    converted: str
    native: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        converted = self.converted
        native = self.native

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "converted": converted,
                "native": native,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        converted = d.pop("converted")

        native = d.pop("native")

        list_allocations_response_200_result_items_item_amount_allocated_pending = cls(
            converted=converted,
            native=native,
        )

        list_allocations_response_200_result_items_item_amount_allocated_pending.additional_properties = (
            d
        )
        return list_allocations_response_200_result_items_item_amount_allocated_pending

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
