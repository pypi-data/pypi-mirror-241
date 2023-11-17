from typing import TYPE_CHECKING, Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..schemas.list_allocations_response_200_result_items_item import (
        ListAllocationsResponse200ResultItemsItem,
    )


@_attrs_define
class ListAllocationsResponse200Result:
    """Page response

    Attributes:
        converted_asset (str): A secondary asset to show the value of allocations. (Eg. you also want to
            see the value of your allocations in USD). Choose this in the request
            parameters.
        items (List['ListAllocationsResponse200ResultItemsItem']):
        total_allocated (str): The total amount allocated across all strategies, denominated in the `converted_asset`
            currency
        total_rewarded (str): Amount earned across all strategies during the whole lifetime of user account, denominated
            in `converted_asset` currency
    """

    converted_asset: str
    items: List["ListAllocationsResponse200ResultItemsItem"]
    total_allocated: str
    total_rewarded: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        converted_asset = self.converted_asset
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        total_allocated = self.total_allocated
        total_rewarded = self.total_rewarded

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "converted_asset": converted_asset,
                "items": items,
                "total_allocated": total_allocated,
                "total_rewarded": total_rewarded,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.list_allocations_response_200_result_items_item import (
            ListAllocationsResponse200ResultItemsItem,
        )

        d = src_dict.copy()
        converted_asset = d.pop("converted_asset")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ListAllocationsResponse200ResultItemsItem.from_dict(
                items_item_data
            )

            items.append(items_item)

        total_allocated = d.pop("total_allocated")

        total_rewarded = d.pop("total_rewarded")

        list_allocations_response_200_result = cls(
            converted_asset=converted_asset,
            items=items,
            total_allocated=total_allocated,
            total_rewarded=total_rewarded,
        )

        list_allocations_response_200_result.additional_properties = d
        return list_allocations_response_200_result

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
