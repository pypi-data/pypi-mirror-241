from typing import TYPE_CHECKING, Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.edit_2_order_edited import Edit2OrderEdited


@_attrs_define
class Edit2:
    """
    Attributes:
        result (Union[Unset, Edit2OrderEdited]):
        error (Union[Unset, List[List[str]]]):
    """

    result: Union[Unset, "Edit2OrderEdited"] = UNSET
    error: Union[Unset, List[List[str]]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        error: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.error, Unset):
            error = []
            for error_item_data in self.error:
                error_item = error_item_data

                error.append(error_item)

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
        from ..schemas.edit_2_order_edited import Edit2OrderEdited

        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, Edit2OrderEdited]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = Edit2OrderEdited.from_dict(_result)

        error = []
        _error = d.pop("error", UNSET)
        for error_item_data in _error or []:
            error_item = cast(List[str], error_item_data)

            error.append(error_item)

        edit_2 = cls(
            result=result,
            error=error,
        )

        edit_2.additional_properties = d
        return edit_2

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
