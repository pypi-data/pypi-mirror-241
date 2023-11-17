from typing import TYPE_CHECKING, Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..schemas.closed_order import ClosedOrder


@_attrs_define
class Closed2ClosedOrdersClosed:
    """ """

    additional_properties: Dict[str, "ClosedOrder"] = _attrs_field(
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
        from ..schemas.closed_order import ClosedOrder

        d = src_dict.copy()
        closed_2_closed_orders_closed = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ClosedOrder.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        closed_2_closed_orders_closed.additional_properties = additional_properties
        return closed_2_closed_orders_closed

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ClosedOrder":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ClosedOrder") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
