from typing import TYPE_CHECKING, Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.add_2_order_added_descr import Add2OrderAddedDescr


@_attrs_define
class Add2OrderAdded:
    """
    Attributes:
        descr (Union[Unset, Add2OrderAddedDescr]): Order description info
        txid (Union[Unset, List[str]]): Transaction IDs for order
            <br><sup><sub>(if order was added successfully)</sup></sub>
    """

    descr: Union[Unset, "Add2OrderAddedDescr"] = UNSET
    txid: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        descr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descr, Unset):
            descr = self.descr.to_dict()

        txid: Union[Unset, List[str]] = UNSET
        if not isinstance(self.txid, Unset):
            txid = self.txid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if descr is not UNSET:
            field_dict["descr"] = descr
        if txid is not UNSET:
            field_dict["txid"] = txid

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.add_2_order_added_descr import Add2OrderAddedDescr

        d = src_dict.copy()
        _descr = d.pop("descr", UNSET)
        descr: Union[Unset, Add2OrderAddedDescr]
        if isinstance(_descr, Unset):
            descr = UNSET
        else:
            descr = Add2OrderAddedDescr.from_dict(_descr)

        txid = cast(List[str], d.pop("txid", UNSET))

        add_2_order_added = cls(
            descr=descr,
            txid=txid,
        )

        add_2_order_added.additional_properties = d
        return add_2_order_added

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
