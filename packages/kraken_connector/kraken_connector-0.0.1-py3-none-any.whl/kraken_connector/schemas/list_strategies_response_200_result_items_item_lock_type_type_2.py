from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.earn import (
    StrategyLockType,
)
from ..types import UNSET, Unset


@_attrs_define
class ListStrategiesResponse200ResultItemsItemLockTypeType2:
    """Timed earn strategies that lock funds and release them back to spot account after specified time (not required for
    MVP)

        Attributes:
            duration (int): Funds are locked for this duration, in seconds
            type (StrategyLockType.TIMED):
            payout_frequency (Union[Unset, None, int]): At what intervals are rewards distributed and credited to the user`s
                ledger If None, then the payout happens at the end of lock duration, in seconds
    """

    duration: int
    type: StrategyLockType.TIMED
    payout_frequency: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duration = self.duration
        type = self.type.value

        payout_frequency = self.payout_frequency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration": duration,
                "type": type,
            }
        )
        if payout_frequency is not UNSET:
            field_dict["payout_frequency"] = payout_frequency

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        duration = d.pop("duration")

        type = StrategyLockType(d.pop("type"))

        payout_frequency = d.pop("payout_frequency", UNSET)

        list_strategies_response_200_result_items_item_lock_type_type_2 = cls(
            duration=duration,
            type=type,
            payout_frequency=payout_frequency,
        )

        list_strategies_response_200_result_items_item_lock_type_type_2.additional_properties = (
            d
        )
        return list_strategies_response_200_result_items_item_lock_type_type_2

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
