from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.trading import OrderType, TypeOrder
from ..types import UNSET, Unset


@_attrs_define
class OpenOrderOrderDescription:
    """Order description info

    Attributes:
        pair (Union[Unset, str]): Asset pair
        type (Union[Unset, TypeOrder]): Type of order (buy/sell)
        ordertype (Union[Unset, OrderType]): Order type
        price (Union[Unset, str]): primary price
        price2 (Union[Unset, str]): Secondary price
        leverage (Union[Unset, str]): Amount of leverage
        order (Union[Unset, str]): Order description
        close (Union[Unset, str]): Conditional close order description (if conditional close set)
    """

    pair: Union[Unset, str] = UNSET
    type: Union[Unset, TypeOrder] = UNSET
    ordertype: Union[Unset, OrderType] = UNSET
    price: Union[Unset, str] = UNSET
    price2: Union[Unset, str] = UNSET
    leverage: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    close: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pair = self.pair
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        ordertype: Union[Unset, str] = UNSET
        if not isinstance(self.ordertype, Unset):
            ordertype = self.ordertype.value

        price = self.price
        price2 = self.price2
        leverage = self.leverage
        order = self.order
        close = self.close

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pair is not UNSET:
            field_dict["pair"] = pair
        if type is not UNSET:
            field_dict["type"] = type
        if ordertype is not UNSET:
            field_dict["ordertype"] = ordertype
        if price is not UNSET:
            field_dict["price"] = price
        if price2 is not UNSET:
            field_dict["price2"] = price2
        if leverage is not UNSET:
            field_dict["leverage"] = leverage
        if order is not UNSET:
            field_dict["order"] = order
        if close is not UNSET:
            field_dict["close"] = close

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        pair = d.pop("pair", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, TypeOrder]
        type = UNSET if isinstance(_type, Unset) else TypeOrder(_type)

        _ordertype = d.pop("ordertype", UNSET)
        ordertype: Union[Unset, OrderType]
        ordertype = UNSET if isinstance(_ordertype, Unset) else OrderType(_ordertype)

        price = d.pop("price", UNSET)

        price2 = d.pop("price2", UNSET)

        leverage = d.pop("leverage", UNSET)

        order = d.pop("order", UNSET)

        close = d.pop("close", UNSET)

        open_order_order_description = cls(
            pair=pair,
            type=type,
            ordertype=ordertype,
            price=price,
            price2=price2,
            leverage=leverage,
            order=order,
            close=close,
        )

        open_order_order_description.additional_properties = d
        return open_order_order_description

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
