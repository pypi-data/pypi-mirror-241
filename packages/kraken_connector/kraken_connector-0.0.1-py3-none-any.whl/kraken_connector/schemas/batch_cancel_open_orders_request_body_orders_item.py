from typing import Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class BatchCancelOpenOrdersRequestBodyOrdersItem:
    """
    Attributes:
        txid (Union[Unset, int, str]): Open order transaction IDs (txid) or user references (userref), up to a maximum
            of 50 total unique IDs/references.
    """

    txid: Union[Unset, int, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        txid: Union[Unset, int, str]
        txid = UNSET if isinstance(self.txid, Unset) else self.txid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if txid is not UNSET:
            field_dict["txid"] = txid

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()

        def _parse_txid(data: object) -> Union[Unset, int, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, int, str], data)

        txid = _parse_txid(d.pop("txid", UNSET))

        batch_cancel_open_orders_request_body_orders_item = cls(
            txid=txid,
        )

        batch_cancel_open_orders_request_body_orders_item.additional_properties = d
        return batch_cancel_open_orders_request_body_orders_item

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
