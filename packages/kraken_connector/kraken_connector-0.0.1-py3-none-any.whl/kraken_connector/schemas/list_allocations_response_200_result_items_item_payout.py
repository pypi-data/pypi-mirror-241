import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..schemas.list_allocations_response_200_result_items_item_payout_accumulated_reward import (
        ListAllocationsResponse200ResultItemsItemPayoutAccumulatedReward,
    )
    from ..schemas.list_allocations_response_200_result_items_item_payout_estimated_reward import (
        ListAllocationsResponse200ResultItemsItemPayoutEstimatedReward,
    )


@_attrs_define
class ListAllocationsResponse200ResultItemsItemPayout:
    """Information about the current payout period (if any)

    Attributes:
        accumulated_reward (ListAllocationsResponse200ResultItemsItemPayoutAccumulatedReward): Reward accumulated in the
            payout period until now
        estimated_reward (ListAllocationsResponse200ResultItemsItemPayoutEstimatedReward): Estimated reward from now
            until the payout
        period_end (datetime.datetime): Tentative date of the next reward payout.
        period_start (datetime.datetime): When the current payout period started. Either the date of the last payout or
            when it was enabled.
    """

    accumulated_reward: "ListAllocationsResponse200ResultItemsItemPayoutAccumulatedReward"
    estimated_reward: "ListAllocationsResponse200ResultItemsItemPayoutEstimatedReward"
    period_end: datetime.datetime
    period_start: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accumulated_reward = self.accumulated_reward.to_dict()

        estimated_reward = self.estimated_reward.to_dict()

        period_end = self.period_end.isoformat()

        period_start = self.period_start.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accumulated_reward": accumulated_reward,
                "estimated_reward": estimated_reward,
                "period_end": period_end,
                "period_start": period_start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.list_allocations_response_200_result_items_item_payout_accumulated_reward import (
            ListAllocationsResponse200ResultItemsItemPayoutAccumulatedReward,
        )
        from ..schemas.list_allocations_response_200_result_items_item_payout_estimated_reward import (
            ListAllocationsResponse200ResultItemsItemPayoutEstimatedReward,
        )

        d = src_dict.copy()
        accumulated_reward = (
            ListAllocationsResponse200ResultItemsItemPayoutAccumulatedReward.from_dict(
                d.pop("accumulated_reward")
            )
        )

        estimated_reward = (
            ListAllocationsResponse200ResultItemsItemPayoutEstimatedReward.from_dict(
                d.pop("estimated_reward")
            )
        )

        period_end = isoparse(d.pop("period_end"))

        period_start = isoparse(d.pop("period_start"))

        list_allocations_response_200_result_items_item_payout = cls(
            accumulated_reward=accumulated_reward,
            estimated_reward=estimated_reward,
            period_end=period_end,
            period_start=period_start,
        )

        list_allocations_response_200_result_items_item_payout.additional_properties = d
        return list_allocations_response_200_result_items_item_payout

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
