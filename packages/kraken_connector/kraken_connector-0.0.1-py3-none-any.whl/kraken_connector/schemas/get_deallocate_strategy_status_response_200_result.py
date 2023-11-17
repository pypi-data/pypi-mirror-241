from typing import Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field


@_attrs_define
class GetDeallocateStrategyStatusResponse200Result:
    """Status of async earn operation

    Attributes:
        pending (bool): `true` if an operation is still in progress on the same strategy.
    """

    pending: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pending = self.pending

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pending": pending,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        pending = d.pop("pending")

        get_deallocate_strategy_status_response_200_result = cls(
            pending=pending,
        )

        get_deallocate_strategy_status_response_200_result.additional_properties = d
        return get_deallocate_strategy_status_response_200_result

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
