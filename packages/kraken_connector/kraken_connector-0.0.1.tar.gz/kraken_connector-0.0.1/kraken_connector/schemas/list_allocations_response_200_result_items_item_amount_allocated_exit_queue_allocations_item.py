import datetime
from typing import Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse


@_attrs_define
class ListAllocationsResponse200ResultItemsItemAmountAllocatedExitQueueAllocationsItem:
    """Additional information about the allocation describing the amount contained within the allocation and when it will
    transition to the next state

        Attributes:
            converted (str): Amount converted into the requested asset
            created_at (datetime.datetime): The date and time which a request to deallocate was received and processed.
                For a deallocation request to a strategy with an `exit-queue`, this will be the time the funds joined the exit
                queue.
            expires (datetime.datetime): The date/time when the funds will be unbonded.
            native (str): Amount in the native asset
    """

    converted: str
    created_at: datetime.datetime
    expires: datetime.datetime
    native: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        converted = self.converted
        created_at = self.created_at.isoformat()

        expires = self.expires.isoformat()

        native = self.native

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "converted": converted,
                "created_at": created_at,
                "expires": expires,
                "native": native,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        converted = d.pop("converted")

        created_at = isoparse(d.pop("created_at"))

        expires = isoparse(d.pop("expires"))

        native = d.pop("native")

        list_allocations_response_200_result_items_item_amount_allocated_exit_queue_allocations_item = cls(
            converted=converted,
            created_at=created_at,
            expires=expires,
            native=native,
        )

        list_allocations_response_200_result_items_item_amount_allocated_exit_queue_allocations_item.additional_properties = (
            d
        )
        return list_allocations_response_200_result_items_item_amount_allocated_exit_queue_allocations_item

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
