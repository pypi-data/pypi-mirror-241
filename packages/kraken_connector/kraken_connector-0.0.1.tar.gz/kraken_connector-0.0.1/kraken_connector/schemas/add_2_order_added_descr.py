from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class Add2OrderAddedDescr:
    """Order description info

    Attributes:
        order (Union[Unset, str]): Order description
        close (Union[Unset, str]): Conditional close order description, if applicable
    """

    order: Union[Unset, str] = UNSET
    close: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order = self.order
        close = self.close

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if close is not UNSET:
            field_dict["close"] = close

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        order = d.pop("order", UNSET)

        close = d.pop("close", UNSET)

        add_2_order_added_descr = cls(
            order=order,
            close=close,
        )

        add_2_order_added_descr.additional_properties = d
        return add_2_order_added_descr

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
