from typing import Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class OrderBook:
    """Asset Pair Order Book Entries

    Attributes:
        asks (Union[Unset, List[List[Union[int, str]]]]): Ask side array of entries `[<price>, <volume>, <timestamp>]`
        bids (Union[Unset, List[List[Union[int, str]]]]): Bid side array of entries `[<price>, <volume>, <timestamp>]`
    """

    asks: Union[Unset, List[List[Union[int, str]]]] = UNSET
    bids: Union[Unset, List[List[Union[int, str]]]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asks: Union[Unset, List[List[Union[int, str]]]] = UNSET
        if not isinstance(self.asks, Unset):
            asks = []
            for asks_item_data in self.asks:
                asks_item = []
                for asks_item_item_data in asks_item_data:
                    asks_item_item: Union[int, str]

                    asks_item_item = asks_item_item_data

                    asks_item.append(asks_item_item)

                asks.append(asks_item)

        bids: Union[Unset, List[List[Union[int, str]]]] = UNSET
        if not isinstance(self.bids, Unset):
            bids = []
            for bids_item_data in self.bids:
                bids_item = []
                for bids_item_item_data in bids_item_data:
                    bids_item_item: Union[int, str]

                    bids_item_item = bids_item_item_data

                    bids_item.append(bids_item_item)

                bids.append(bids_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asks is not UNSET:
            field_dict["asks"] = asks
        if bids is not UNSET:
            field_dict["bids"] = bids

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        asks = []
        _asks = d.pop("asks", UNSET)
        for asks_item_data in _asks or []:
            asks_item = []
            _asks_item = asks_item_data
            for asks_item_item_data in _asks_item:

                def _parse_asks_item_item(data: object) -> Union[int, str]:
                    return cast(Union[int, str], data)

                asks_item_item = _parse_asks_item_item(asks_item_item_data)

                asks_item.append(asks_item_item)

            asks.append(asks_item)

        bids = []
        _bids = d.pop("bids", UNSET)
        for bids_item_data in _bids or []:
            bids_item = []
            _bids_item = bids_item_data
            for bids_item_item_data in _bids_item:

                def _parse_bids_item_item(data: object) -> Union[int, str]:
                    return cast(Union[int, str], data)

                bids_item_item = _parse_bids_item_item(bids_item_item_data)

                bids_item.append(bids_item_item)

            bids.append(bids_item)

        order_book = cls(
            asks=asks,
            bids=bids,
        )

        order_book.additional_properties = d
        return order_book

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
