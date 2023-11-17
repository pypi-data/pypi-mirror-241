from typing import TYPE_CHECKING, Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.list_strategies_response_200_result import (
        ListStrategiesResponse200Result,
    )


@_attrs_define
class ListStrategiesResponse200:
    """
    Attributes:
        error (List[str]):
        result (Union[Unset, None, ListStrategiesResponse200Result]):
    """

    error: List[str]
    result: Union[Unset, None, "ListStrategiesResponse200Result"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error

        result: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict() if self.result else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.list_strategies_response_200_result import (
            ListStrategiesResponse200Result,
        )

        d = src_dict.copy()
        error = cast(List[str], d.pop("error"))

        _result = d.pop("result", UNSET)
        result: Union[Unset, None, ListStrategiesResponse200Result]
        if _result is None:
            result = None
        elif isinstance(_result, Unset):
            result = UNSET
        else:
            result = ListStrategiesResponse200Result.from_dict(_result)

        list_strategies_response_200 = cls(
            error=error,
            result=result,
        )

        list_strategies_response_200.additional_properties = d
        return list_strategies_response_200

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
