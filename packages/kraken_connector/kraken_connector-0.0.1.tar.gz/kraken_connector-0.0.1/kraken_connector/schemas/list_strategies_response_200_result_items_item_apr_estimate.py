from typing import Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field


@_attrs_define
class ListStrategiesResponse200ResultItemsItemAprEstimate:
    """The estimate is based on previous revenues from the strategy.

    Attributes:
        high (str): Maximal yield percentage for one year
        low (str): Minimal yield percentage for one year
    """

    high: str
    low: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        high = self.high
        low = self.low

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "high": high,
                "low": low,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        high = d.pop("high")

        low = d.pop("low")

        list_strategies_response_200_result_items_item_apr_estimate = cls(
            high=high,
            low=low,
        )

        list_strategies_response_200_result_items_item_apr_estimate.additional_properties = (
            d
        )
        return list_strategies_response_200_result_items_item_apr_estimate

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
