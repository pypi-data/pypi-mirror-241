from typing import TYPE_CHECKING, Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.edit_2_order_edited_descr import Edit2OrderEditedDescr


@_attrs_define
class Edit2OrderEdited:
    """
    Attributes:
        descr (Union[Unset, Edit2OrderEditedDescr]): Order description info
        txid (Union[Unset, str]): New Transaction ID
            <br><sup><sub>(if order was added successfully)</sup></sub>
        newuserref (Union[Unset, str]): Original userref if passed with the request
        olduserref (Union[Unset, str]): Original userref if passed with the request
        orders_cancelled (Union[Unset, int]): Number of orders cancelled (either 0 or 1)
        originaltxid (Union[Unset, str]): Original transaction ID
        status (Union[Unset, str]): Status of the order: Ok or Err
        volume (Union[Unset, str]): Updated volume
        price (Union[Unset, str]): Updated price
        price2 (Union[Unset, str]): Updated price2
        error_message (Union[Unset, str]): Error message if unsuccessful
    """

    descr: Union[Unset, "Edit2OrderEditedDescr"] = UNSET
    txid: Union[Unset, str] = UNSET
    newuserref: Union[Unset, str] = UNSET
    olduserref: Union[Unset, str] = UNSET
    orders_cancelled: Union[Unset, int] = UNSET
    originaltxid: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    volume: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    price2: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        descr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descr, Unset):
            descr = self.descr.to_dict()

        txid = self.txid
        newuserref = self.newuserref
        olduserref = self.olduserref
        orders_cancelled = self.orders_cancelled
        originaltxid = self.originaltxid
        status = self.status
        volume = self.volume
        price = self.price
        price2 = self.price2
        error_message = self.error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if descr is not UNSET:
            field_dict["descr"] = descr
        if txid is not UNSET:
            field_dict["txid"] = txid
        if newuserref is not UNSET:
            field_dict["newuserref"] = newuserref
        if olduserref is not UNSET:
            field_dict["olduserref"] = olduserref
        if orders_cancelled is not UNSET:
            field_dict["orders_cancelled"] = orders_cancelled
        if originaltxid is not UNSET:
            field_dict["originaltxid"] = originaltxid
        if status is not UNSET:
            field_dict["status"] = status
        if volume is not UNSET:
            field_dict["volume"] = volume
        if price is not UNSET:
            field_dict["price"] = price
        if price2 is not UNSET:
            field_dict["price2"] = price2
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.edit_2_order_edited_descr import Edit2OrderEditedDescr

        d = src_dict.copy()
        _descr = d.pop("descr", UNSET)
        descr: Union[Unset, Edit2OrderEditedDescr]
        if isinstance(_descr, Unset):
            descr = UNSET
        else:
            descr = Edit2OrderEditedDescr.from_dict(_descr)

        txid = d.pop("txid", UNSET)

        newuserref = d.pop("newuserref", UNSET)

        olduserref = d.pop("olduserref", UNSET)

        orders_cancelled = d.pop("orders_cancelled", UNSET)

        originaltxid = d.pop("originaltxid", UNSET)

        status = d.pop("status", UNSET)

        volume = d.pop("volume", UNSET)

        price = d.pop("price", UNSET)

        price2 = d.pop("price2", UNSET)

        error_message = d.pop("error_message", UNSET)

        edit_2_order_edited = cls(
            descr=descr,
            txid=txid,
            newuserref=newuserref,
            olduserref=olduserref,
            orders_cancelled=orders_cancelled,
            originaltxid=originaltxid,
            status=status,
            volume=volume,
            price=price,
            price2=price2,
            error_message=error_message,
        )

        edit_2_order_edited.additional_properties = d
        return edit_2_order_edited

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
