from typing import TYPE_CHECKING, Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.closed_2_closed_orders_closed import Closed2ClosedOrdersClosed


@_attrs_define
class Closed2ClosedOrders:
    """Closed Orders

    Attributes:
        closed (Union[Unset, Closed2ClosedOrdersClosed]):
        count (Union[Unset, int]): Amount of available order info matching criteria
    """

    closed: Union[Unset, "Closed2ClosedOrdersClosed"] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        closed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.closed, Unset):
            closed = self.closed.to_dict()

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if closed is not UNSET:
            field_dict["closed"] = closed
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.closed_2_closed_orders_closed import Closed2ClosedOrdersClosed

        d = src_dict.copy()
        _closed = d.pop("closed", UNSET)
        closed: Union[Unset, Closed2ClosedOrdersClosed]
        if isinstance(_closed, Unset):
            closed = UNSET
        else:
            closed = Closed2ClosedOrdersClosed.from_dict(_closed)

        count = d.pop("count", UNSET)

        closed_2_closed_orders = cls(
            closed=closed,
            count=count,
        )

        closed_2_closed_orders.additional_properties = d
        return closed_2_closed_orders

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
