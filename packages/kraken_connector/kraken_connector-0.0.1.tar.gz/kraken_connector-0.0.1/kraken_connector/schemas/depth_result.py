from typing import TYPE_CHECKING, Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..schemas.order_book import OrderBook


@_attrs_define
class DepthResult:
    """ """

    additional_properties: Dict[str, "OrderBook"] = _attrs_field(
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
        from ..schemas.order_book import OrderBook

        d = src_dict.copy()
        depth_result = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = OrderBook.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        depth_result.additional_properties = additional_properties
        return depth_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "OrderBook":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "OrderBook") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
