from typing import TYPE_CHECKING, Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..schemas.list_allocations_response_200_result_items_item_amount_allocated_bonding_allocations_item import (
        ListAllocationsResponse200ResultItemsItemAmountAllocatedBondingAllocationsItem,
    )


@_attrs_define
class ListAllocationsResponse200ResultItemsItemAmountAllocatedBonding:
    """Amount allocated in bonding status

    Attributes:
        allocation_count (int): The total number of allocations in this state for this asset
        allocations (List['ListAllocationsResponse200ResultItemsItemAmountAllocatedBondingAllocationsItem']): Details
            about when each allocation will expire and move to the next state
        converted (str): Amount converted into the requested asset
        native (str): Amount in the native asset
    """

    allocation_count: int
    allocations: List[
        "ListAllocationsResponse200ResultItemsItemAmountAllocatedBondingAllocationsItem"
    ]
    converted: str
    native: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allocation_count = self.allocation_count
        allocations = []
        for allocations_item_data in self.allocations:
            allocations_item = allocations_item_data.to_dict()

            allocations.append(allocations_item)

        converted = self.converted
        native = self.native

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allocation_count": allocation_count,
                "allocations": allocations,
                "converted": converted,
                "native": native,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.list_allocations_response_200_result_items_item_amount_allocated_bonding_allocations_item import (
            ListAllocationsResponse200ResultItemsItemAmountAllocatedBondingAllocationsItem,
        )

        d = src_dict.copy()
        allocation_count = d.pop("allocation_count")

        allocations = []
        _allocations = d.pop("allocations")
        for allocations_item_data in _allocations:
            allocations_item = ListAllocationsResponse200ResultItemsItemAmountAllocatedBondingAllocationsItem.from_dict(
                allocations_item_data
            )

            allocations.append(allocations_item)

        converted = d.pop("converted")

        native = d.pop("native")

        list_allocations_response_200_result_items_item_amount_allocated_bonding = cls(
            allocation_count=allocation_count,
            allocations=allocations,
            converted=converted,
            native=native,
        )

        list_allocations_response_200_result_items_item_amount_allocated_bonding.additional_properties = (
            d
        )
        return list_allocations_response_200_result_items_item_amount_allocated_bonding

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
