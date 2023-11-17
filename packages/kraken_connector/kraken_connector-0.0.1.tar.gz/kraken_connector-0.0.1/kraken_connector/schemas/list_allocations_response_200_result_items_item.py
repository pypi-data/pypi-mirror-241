from typing import TYPE_CHECKING, Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.list_allocations_response_200_result_items_item_amount_allocated import (
        ListAllocationsResponse200ResultItemsItemAmountAllocated,
    )
    from ..schemas.list_allocations_response_200_result_items_item_payout import (
        ListAllocationsResponse200ResultItemsItemPayout,
    )
    from ..schemas.list_allocations_response_200_result_items_item_total_rewarded import (
        ListAllocationsResponse200ResultItemsItemTotalRewarded,
    )


@_attrs_define
class ListAllocationsResponse200ResultItemsItem:
    """
    Attributes:
        amount_allocated (ListAllocationsResponse200ResultItemsItemAmountAllocated): Amounts allocated to this Earn
            strategy
        native_asset (str): The asset of the native currency of this allocation
        strategy_id (str): Unique ID for Earn Strategy
        total_rewarded (ListAllocationsResponse200ResultItemsItemTotalRewarded): Amount earned using the strategy during
            the whole lifetime of user account
        payout (Union[Unset, None, ListAllocationsResponse200ResultItemsItemPayout]): Information about the current
            payout period (if any)
    """

    amount_allocated: "ListAllocationsResponse200ResultItemsItemAmountAllocated"
    native_asset: str
    strategy_id: str
    total_rewarded: "ListAllocationsResponse200ResultItemsItemTotalRewarded"
    payout: Union[
        Unset, None, "ListAllocationsResponse200ResultItemsItemPayout"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount_allocated = self.amount_allocated.to_dict()

        native_asset = self.native_asset
        strategy_id = self.strategy_id
        total_rewarded = self.total_rewarded.to_dict()

        payout: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.payout, Unset):
            payout = self.payout.to_dict() if self.payout else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount_allocated": amount_allocated,
                "native_asset": native_asset,
                "strategy_id": strategy_id,
                "total_rewarded": total_rewarded,
            }
        )
        if payout is not UNSET:
            field_dict["payout"] = payout

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.list_allocations_response_200_result_items_item_amount_allocated import (
            ListAllocationsResponse200ResultItemsItemAmountAllocated,
        )
        from ..schemas.list_allocations_response_200_result_items_item_payout import (
            ListAllocationsResponse200ResultItemsItemPayout,
        )
        from ..schemas.list_allocations_response_200_result_items_item_total_rewarded import (
            ListAllocationsResponse200ResultItemsItemTotalRewarded,
        )

        d = src_dict.copy()
        amount_allocated = (
            ListAllocationsResponse200ResultItemsItemAmountAllocated.from_dict(
                d.pop("amount_allocated")
            )
        )

        native_asset = d.pop("native_asset")

        strategy_id = d.pop("strategy_id")

        total_rewarded = (
            ListAllocationsResponse200ResultItemsItemTotalRewarded.from_dict(
                d.pop("total_rewarded")
            )
        )

        _payout = d.pop("payout", UNSET)
        payout: Union[Unset, None, ListAllocationsResponse200ResultItemsItemPayout]
        if _payout is None:
            payout = None
        elif isinstance(_payout, Unset):
            payout = UNSET
        else:
            payout = ListAllocationsResponse200ResultItemsItemPayout.from_dict(_payout)

        list_allocations_response_200_result_items_item = cls(
            amount_allocated=amount_allocated,
            native_asset=native_asset,
            strategy_id=strategy_id,
            total_rewarded=total_rewarded,
            payout=payout,
        )

        list_allocations_response_200_result_items_item.additional_properties = d
        return list_allocations_response_200_result_items_item

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
