from typing import TYPE_CHECKING, Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.trade_history_trades import TradeHistoryTrades


@_attrs_define
class TradeHistory:
    """Trade History

    Attributes:
        count (Union[Unset, int]): Amount of available trades matching criteria
        trades (Union[Unset, TradeHistoryTrades]): Trade info
    """

    count: Union[Unset, int] = UNSET
    trades: Union[Unset, "TradeHistoryTrades"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        trades: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trades, Unset):
            trades = self.trades.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if trades is not UNSET:
            field_dict["trades"] = trades

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.trade_history_trades import TradeHistoryTrades

        d = src_dict.copy()
        count = d.pop("count", UNSET)

        _trades = d.pop("trades", UNSET)
        trades: Union[Unset, TradeHistoryTrades]
        if isinstance(_trades, Unset):
            trades = UNSET
        else:
            trades = TradeHistoryTrades.from_dict(_trades)

        trade_history = cls(
            count=count,
            trades=trades,
        )

        trade_history.additional_properties = d
        return trade_history

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
