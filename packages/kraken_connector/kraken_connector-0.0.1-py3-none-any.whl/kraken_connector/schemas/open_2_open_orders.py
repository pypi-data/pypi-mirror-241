from typing import TYPE_CHECKING, Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.open_2_open_orders_open import Open2OpenOrdersOpen


@_attrs_define
class Open2OpenOrders:
    """Open Orders

    Attributes:
        open_ (Union[Unset, Open2OpenOrdersOpen]):
    """

    open_: Union[Unset, "Open2OpenOrdersOpen"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        open_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.open_, Unset):
            open_ = self.open_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_ is not UNSET:
            field_dict["open"] = open_

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.open_2_open_orders_open import Open2OpenOrdersOpen

        d = src_dict.copy()
        _open_ = d.pop("open", UNSET)
        open_: Union[Unset, Open2OpenOrdersOpen]
        if isinstance(_open_, Unset):
            open_ = UNSET
        else:
            open_ = Open2OpenOrdersOpen.from_dict(_open_)

        open_2_open_orders = cls(
            open_=open_,
        )

        open_2_open_orders.additional_properties = d
        return open_2_open_orders

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
