from typing import TYPE_CHECKING, Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.ohlc_result import OhlcResult


@_attrs_define
class Ohlc:
    """
    Attributes:
        result (Union[Unset, OhlcResult]):
        error (Union[Unset, List[str]]):
    """

    result: Union[Unset, "OhlcResult"] = UNSET
    error: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        error: Union[Unset, List[str]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.ohlc_result import OhlcResult

        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, OhlcResult]
        result = UNSET if isinstance(_result, Unset) else OhlcResult.from_dict(_result)

        error = cast(List[str], d.pop("error", UNSET))

        ohlc = cls(
            result=result,
            error=error,
        )

        ohlc.additional_properties = d
        return ohlc

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
