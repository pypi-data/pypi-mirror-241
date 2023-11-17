from typing import TYPE_CHECKING, Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.trading import OrderStatus, OrderTrigger
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.open_order_order_description import OpenOrderOrderDescription


@_attrs_define
class OpenOrder:
    """Open Order

    Attributes:
        refid (Union[Unset, None, str]): Referral order transaction ID that created this order
        userref (Union[Unset, None, int]): User reference id
        status (Union[Unset, OrderStatus]): Status of order
              * pending = order pending book entry
              * open = open order
              * closed = closed order
              * canceled = order canceled
              * expired = order expired
        opentm (Union[Unset, float]): Unix timestamp of when order was placed
        starttm (Union[Unset, float]): Unix timestamp of order start time (or 0 if not set)
        expiretm (Union[Unset, float]): Unix timestamp of order end time (or 0 if not set)
        descr (Union[Unset, OpenOrderOrderDescription]): Order description info
        vol (Union[Unset, str]): Volume of order (base currency)
        vol_exec (Union[Unset, str]): Volume executed (base currency)
        cost (Union[Unset, str]): Total cost (quote currency unless)
        fee (Union[Unset, str]): Total fee (quote currency)
        price (Union[Unset, str]): Average price (quote currency)
        stopprice (Union[Unset, str]): Stop price (quote currency)
        limitprice (Union[Unset, str]): Triggered limit price (quote currency, when limit based order type triggered)
        trigger (Union[Unset, OrderTrigger]): Price signal used to trigger "stop-loss" "take-profit" "stop-loss-
            limit" "take-profit-limit" orders.
              * `last` is the implied trigger if this field is not set.
             Default: OrderTrigger.LAST.
        misc (Union[Unset, str]): Comma delimited list of miscellaneous info

              * `stopped` triggered by stop price
              * `touched` triggered by touch price
              * `liquidated` liquidation
              * `partial` partial fill
        oflags (Union[Unset, str]): Comma delimited list of order flags

              * `post` post-only order (available when ordertype = limit)
              * `fcib` prefer fee in base currency (default if selling)
              * `fciq` prefer fee in quote currency (default if buying, mutually exclusive with `fcib`)
              * `nompp` disable [market price protection](https://support.kraken.com/hc/en-us/articles/201648183-Market-
            Price-Protection) for market orders
              * `viqc`  order volume expressed in quote currency. This is supported only for market orders.
        trades (Union[Unset, List[str]]): List of trade IDs related to order (if trades info requested and data
            available)
    """

    refid: Union[Unset, None, str] = UNSET
    userref: Union[Unset, None, int] = UNSET
    status: Union[Unset, OrderStatus] = UNSET
    opentm: Union[Unset, float] = UNSET
    starttm: Union[Unset, float] = UNSET
    expiretm: Union[Unset, float] = UNSET
    descr: Union[Unset, "OpenOrderOrderDescription"] = UNSET
    vol: Union[Unset, str] = UNSET
    vol_exec: Union[Unset, str] = UNSET
    cost: Union[Unset, str] = UNSET
    fee: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    stopprice: Union[Unset, str] = UNSET
    limitprice: Union[Unset, str] = UNSET
    trigger: Union[Unset, OrderTrigger] = OrderTrigger.LAST
    misc: Union[Unset, str] = UNSET
    oflags: Union[Unset, str] = UNSET
    trades: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refid = self.refid
        userref = self.userref
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        opentm = self.opentm
        starttm = self.starttm
        expiretm = self.expiretm
        descr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descr, Unset):
            descr = self.descr.to_dict()

        vol = self.vol
        vol_exec = self.vol_exec
        cost = self.cost
        fee = self.fee
        price = self.price
        stopprice = self.stopprice
        limitprice = self.limitprice
        trigger: Union[Unset, str] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        misc = self.misc
        oflags = self.oflags
        trades: Union[Unset, List[str]] = UNSET
        if not isinstance(self.trades, Unset):
            trades = self.trades

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refid is not UNSET:
            field_dict["refid"] = refid
        if userref is not UNSET:
            field_dict["userref"] = userref
        if status is not UNSET:
            field_dict["status"] = status
        if opentm is not UNSET:
            field_dict["opentm"] = opentm
        if starttm is not UNSET:
            field_dict["starttm"] = starttm
        if expiretm is not UNSET:
            field_dict["expiretm"] = expiretm
        if descr is not UNSET:
            field_dict["descr"] = descr
        if vol is not UNSET:
            field_dict["vol"] = vol
        if vol_exec is not UNSET:
            field_dict["vol_exec"] = vol_exec
        if cost is not UNSET:
            field_dict["cost"] = cost
        if fee is not UNSET:
            field_dict["fee"] = fee
        if price is not UNSET:
            field_dict["price"] = price
        if stopprice is not UNSET:
            field_dict["stopprice"] = stopprice
        if limitprice is not UNSET:
            field_dict["limitprice"] = limitprice
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if misc is not UNSET:
            field_dict["misc"] = misc
        if oflags is not UNSET:
            field_dict["oflags"] = oflags
        if trades is not UNSET:
            field_dict["trades"] = trades

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.open_order_order_description import OpenOrderOrderDescription

        d = src_dict.copy()
        refid = d.pop("refid", UNSET)

        userref = d.pop("userref", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, OrderStatus]
        status = UNSET if isinstance(_status, Unset) else OrderStatus(_status)

        opentm = d.pop("opentm", UNSET)

        starttm = d.pop("starttm", UNSET)

        expiretm = d.pop("expiretm", UNSET)

        _descr = d.pop("descr", UNSET)
        descr: Union[Unset, OpenOrderOrderDescription]
        if isinstance(_descr, Unset):
            descr = UNSET
        else:
            descr = OpenOrderOrderDescription.from_dict(_descr)

        vol = d.pop("vol", UNSET)

        vol_exec = d.pop("vol_exec", UNSET)

        cost = d.pop("cost", UNSET)

        fee = d.pop("fee", UNSET)

        price = d.pop("price", UNSET)

        stopprice = d.pop("stopprice", UNSET)

        limitprice = d.pop("limitprice", UNSET)

        _trigger = d.pop("trigger", UNSET)
        trigger: Union[Unset, OrderTrigger]
        trigger = UNSET if isinstance(_trigger, Unset) else OrderTrigger(_trigger)

        misc = d.pop("misc", UNSET)

        oflags = d.pop("oflags", UNSET)

        trades = cast(List[str], d.pop("trades", UNSET))

        open_order = cls(
            refid=refid,
            userref=userref,
            status=status,
            opentm=opentm,
            starttm=starttm,
            expiretm=expiretm,
            descr=descr,
            vol=vol,
            vol_exec=vol_exec,
            cost=cost,
            fee=fee,
            price=price,
            stopprice=stopprice,
            limitprice=limitprice,
            trigger=trigger,
            misc=misc,
            oflags=oflags,
            trades=trades,
        )

        open_order.additional_properties = d
        return open_order

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
