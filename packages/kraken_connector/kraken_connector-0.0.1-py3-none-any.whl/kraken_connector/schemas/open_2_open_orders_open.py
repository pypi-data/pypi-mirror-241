from typing import TYPE_CHECKING, Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..schemas.open_order import OpenOrder


@_attrs_define
class Open2OpenOrdersOpen:
    """ """

    additional_properties: Dict[str, "OpenOrder"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.open_order import OpenOrder

        d = src_dict.copy()
        open_2_open_orders_open = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = OpenOrder.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        open_2_open_orders_open.additional_properties = additional_properties
        return open_2_open_orders_open

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "OpenOrder":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "OpenOrder") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
