from typing import Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class AssetPair:
    """Trading Asset Pair

    Attributes:
        altname (Union[Unset, str]): Alternate pair name
        wsname (Union[Unset, str]): WebSocket pair name (if available)
        aclass_base (Union[Unset, str]): Asset class of base component
        base (Union[Unset, str]): Asset ID of base component
        aclass_quote (Union[Unset, str]): Asset class of quote component
        quote (Union[Unset, str]): Asset ID of quote component
        lot (Union[Unset, str]): Volume lot size
        pair_decimals (Union[Unset, int]): Scaling decimal places for pair
        cost_decimals (Union[Unset, int]): Scaling decimal places for cost
        lot_decimals (Union[Unset, int]): Scaling decimal places for volume
        lot_multiplier (Union[Unset, int]): Amount to multiply lot volume by to get currency volume
        leverage_buy (Union[Unset, List[int]]): Array of leverage amounts available when buying
        leverage_sell (Union[Unset, List[int]]): Array of leverage amounts available when selling
        fees (Union[Unset, List[List[float]]]): Fee schedule array in `[<volume>, <percent fee>]` tuples
        fees_maker (Union[Unset, List[List[float]]]): Maker fee schedule array in `[<volume>, <percent fee>]`  tuples
            (if on maker/taker)
        fee_volume_currency (Union[Unset, str]): Volume discount currency
        margin_call (Union[Unset, int]): Margin call level
        margin_stop (Union[Unset, int]): Stop-out/liquidation margin level
        ordermin (Union[Unset, str]): Minimum order size (in terms of base currency)
        costmin (Union[Unset, str]): Minimum order cost (in terms of quote currency)
        tick_size (Union[Unset, str]): Minimum increment between valid price levels
        status (Union[Unset, str]): Status of asset. Possible values: `online`, `cancel_only`, `post_only`,
            `limit_only`, `reduce_only`.
        long_position_limit (Union[Unset, int]): Maximum long margin position size (in terms of base currency)
        short_position_limit (Union[Unset, int]): Maximum short margin position size (in terms of base currency)
    """

    altname: Union[Unset, str] = UNSET
    wsname: Union[Unset, str] = UNSET
    aclass_base: Union[Unset, str] = UNSET
    base: Union[Unset, str] = UNSET
    aclass_quote: Union[Unset, str] = UNSET
    quote: Union[Unset, str] = UNSET
    lot: Union[Unset, str] = UNSET
    pair_decimals: Union[Unset, int] = UNSET
    cost_decimals: Union[Unset, int] = UNSET
    lot_decimals: Union[Unset, int] = UNSET
    lot_multiplier: Union[Unset, int] = UNSET
    leverage_buy: Union[Unset, List[int]] = UNSET
    leverage_sell: Union[Unset, List[int]] = UNSET
    fees: Union[Unset, List[List[float]]] = UNSET
    fees_maker: Union[Unset, List[List[float]]] = UNSET
    fee_volume_currency: Union[Unset, str] = UNSET
    margin_call: Union[Unset, int] = UNSET
    margin_stop: Union[Unset, int] = UNSET
    ordermin: Union[Unset, str] = UNSET
    costmin: Union[Unset, str] = UNSET
    tick_size: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    long_position_limit: Union[Unset, int] = UNSET
    short_position_limit: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        altname = self.altname
        wsname = self.wsname
        aclass_base = self.aclass_base
        base = self.base
        aclass_quote = self.aclass_quote
        quote = self.quote
        lot = self.lot
        pair_decimals = self.pair_decimals
        cost_decimals = self.cost_decimals
        lot_decimals = self.lot_decimals
        lot_multiplier = self.lot_multiplier
        leverage_buy: Union[Unset, List[int]] = UNSET
        if not isinstance(self.leverage_buy, Unset):
            leverage_buy = self.leverage_buy

        leverage_sell: Union[Unset, List[int]] = UNSET
        if not isinstance(self.leverage_sell, Unset):
            leverage_sell = self.leverage_sell

        fees: Union[Unset, List[List[float]]] = UNSET
        if not isinstance(self.fees, Unset):
            fees = []
            for fees_item_data in self.fees:
                fees_item = fees_item_data

                fees.append(fees_item)

        fees_maker: Union[Unset, List[List[float]]] = UNSET
        if not isinstance(self.fees_maker, Unset):
            fees_maker = []
            for fees_maker_item_data in self.fees_maker:
                fees_maker_item = fees_maker_item_data

                fees_maker.append(fees_maker_item)

        fee_volume_currency = self.fee_volume_currency
        margin_call = self.margin_call
        margin_stop = self.margin_stop
        ordermin = self.ordermin
        costmin = self.costmin
        tick_size = self.tick_size
        status = self.status
        long_position_limit = self.long_position_limit
        short_position_limit = self.short_position_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if altname is not UNSET:
            field_dict["altname"] = altname
        if wsname is not UNSET:
            field_dict["wsname"] = wsname
        if aclass_base is not UNSET:
            field_dict["aclass_base"] = aclass_base
        if base is not UNSET:
            field_dict["base"] = base
        if aclass_quote is not UNSET:
            field_dict["aclass_quote"] = aclass_quote
        if quote is not UNSET:
            field_dict["quote"] = quote
        if lot is not UNSET:
            field_dict["lot"] = lot
        if pair_decimals is not UNSET:
            field_dict["pair_decimals"] = pair_decimals
        if cost_decimals is not UNSET:
            field_dict["cost_decimals"] = cost_decimals
        if lot_decimals is not UNSET:
            field_dict["lot_decimals"] = lot_decimals
        if lot_multiplier is not UNSET:
            field_dict["lot_multiplier"] = lot_multiplier
        if leverage_buy is not UNSET:
            field_dict["leverage_buy"] = leverage_buy
        if leverage_sell is not UNSET:
            field_dict["leverage_sell"] = leverage_sell
        if fees is not UNSET:
            field_dict["fees"] = fees
        if fees_maker is not UNSET:
            field_dict["fees_maker"] = fees_maker
        if fee_volume_currency is not UNSET:
            field_dict["fee_volume_currency"] = fee_volume_currency
        if margin_call is not UNSET:
            field_dict["margin_call"] = margin_call
        if margin_stop is not UNSET:
            field_dict["margin_stop"] = margin_stop
        if ordermin is not UNSET:
            field_dict["ordermin"] = ordermin
        if costmin is not UNSET:
            field_dict["costmin"] = costmin
        if tick_size is not UNSET:
            field_dict["tick_size"] = tick_size
        if status is not UNSET:
            field_dict["status"] = status
        if long_position_limit is not UNSET:
            field_dict["long_position_limit"] = long_position_limit
        if short_position_limit is not UNSET:
            field_dict["short_position_limit"] = short_position_limit

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        altname = d.pop("altname", UNSET)

        wsname = d.pop("wsname", UNSET)

        aclass_base = d.pop("aclass_base", UNSET)

        base = d.pop("base", UNSET)

        aclass_quote = d.pop("aclass_quote", UNSET)

        quote = d.pop("quote", UNSET)

        lot = d.pop("lot", UNSET)

        pair_decimals = d.pop("pair_decimals", UNSET)

        cost_decimals = d.pop("cost_decimals", UNSET)

        lot_decimals = d.pop("lot_decimals", UNSET)

        lot_multiplier = d.pop("lot_multiplier", UNSET)

        leverage_buy = cast(List[int], d.pop("leverage_buy", UNSET))

        leverage_sell = cast(List[int], d.pop("leverage_sell", UNSET))

        fees = []
        _fees = d.pop("fees", UNSET)
        for fees_item_data in _fees or []:
            fees_item = cast(List[float], fees_item_data)

            fees.append(fees_item)

        fees_maker = []
        _fees_maker = d.pop("fees_maker", UNSET)
        for fees_maker_item_data in _fees_maker or []:
            fees_maker_item = cast(List[float], fees_maker_item_data)

            fees_maker.append(fees_maker_item)

        fee_volume_currency = d.pop("fee_volume_currency", UNSET)

        margin_call = d.pop("margin_call", UNSET)

        margin_stop = d.pop("margin_stop", UNSET)

        ordermin = d.pop("ordermin", UNSET)

        costmin = d.pop("costmin", UNSET)

        tick_size = d.pop("tick_size", UNSET)

        status = d.pop("status", UNSET)

        long_position_limit = d.pop("long_position_limit", UNSET)

        short_position_limit = d.pop("short_position_limit", UNSET)

        asset_pair = cls(
            altname=altname,
            wsname=wsname,
            aclass_base=aclass_base,
            base=base,
            aclass_quote=aclass_quote,
            quote=quote,
            lot=lot,
            pair_decimals=pair_decimals,
            cost_decimals=cost_decimals,
            lot_decimals=lot_decimals,
            lot_multiplier=lot_multiplier,
            leverage_buy=leverage_buy,
            leverage_sell=leverage_sell,
            fees=fees,
            fees_maker=fees_maker,
            fee_volume_currency=fee_volume_currency,
            margin_call=margin_call,
            margin_stop=margin_stop,
            ordermin=ordermin,
            costmin=costmin,
            tick_size=tick_size,
            status=status,
            long_position_limit=long_position_limit,
            short_position_limit=short_position_limit,
        )

        asset_pair.additional_properties = d
        return asset_pair

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
