from typing import TYPE_CHECKING, Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.batchadd_2_result_orders_item_descr import (
        Batchadd2ResultOrdersItemDescr,
    )


@_attrs_define
class Batchadd2ResultOrdersItem:
    """
    Attributes:
        descr (Union[Unset, Batchadd2ResultOrdersItemDescr]): Order description info
        error (Union[Unset, str]): Error description from individual order processing
        txid (Union[Unset, str]): Transaction ID for order
            <br><sup><sub>(if order was added successfully)</sup></sub>
    """

    descr: Union[Unset, "Batchadd2ResultOrdersItemDescr"] = UNSET
    error: Union[Unset, str] = UNSET
    txid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        descr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descr, Unset):
            descr = self.descr.to_dict()

        error = self.error
        txid = self.txid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if descr is not UNSET:
            field_dict["descr"] = descr
        if error is not UNSET:
            field_dict["error"] = error
        if txid is not UNSET:
            field_dict["txid"] = txid

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.batchadd_2_result_orders_item_descr import (
            Batchadd2ResultOrdersItemDescr,
        )

        d = src_dict.copy()
        _descr = d.pop("descr", UNSET)
        descr: Union[Unset, Batchadd2ResultOrdersItemDescr]
        if isinstance(_descr, Unset):
            descr = UNSET
        else:
            descr = Batchadd2ResultOrdersItemDescr.from_dict(_descr)

        error = d.pop("error", UNSET)

        txid = d.pop("txid", UNSET)

        batchadd_2_result_orders_item = cls(
            descr=descr,
            error=error,
            txid=txid,
        )

        batchadd_2_result_orders_item.additional_properties = d
        return batchadd_2_result_orders_item

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
