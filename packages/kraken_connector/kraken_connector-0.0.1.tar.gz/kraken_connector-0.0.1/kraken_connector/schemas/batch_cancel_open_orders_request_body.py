from typing import TYPE_CHECKING, Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..schemas.batch_cancel_open_orders_request_body_orders_item import (
        BatchCancelOpenOrdersRequestBodyOrdersItem,
    )


@_attrs_define
class BatchCancelOpenOrdersRequestBody:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        orders (List['BatchCancelOpenOrdersRequestBodyOrdersItem']):
    """

    nonce: int
    orders: List["BatchCancelOpenOrdersRequestBodyOrdersItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        orders = []
        for orders_item_data in self.orders:
            orders_item = orders_item_data.to_dict()

            orders.append(orders_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "orders": orders,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.batch_cancel_open_orders_request_body_orders_item import (
            BatchCancelOpenOrdersRequestBodyOrdersItem,
        )

        d = src_dict.copy()
        nonce = d.pop("nonce")

        orders = []
        _orders = d.pop("orders")
        for orders_item_data in _orders:
            orders_item = BatchCancelOpenOrdersRequestBodyOrdersItem.from_dict(
                orders_item_data
            )

            orders.append(orders_item)

        batch_cancel_open_orders_request_body = cls(
            nonce=nonce,
            orders=orders,
        )

        batch_cancel_open_orders_request_body.additional_properties = d
        return batch_cancel_open_orders_request_body

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
