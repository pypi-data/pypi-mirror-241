from typing import Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class EditStandardOrderRequestBody:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        txid (Union[int, str]): Original Order ID or User Reference Id (userref) which is user-specified integer id used
            with the original order. If userref is not unique and was used with multiple order, edit request is denied with
            an error.
        pair (str): Asset pair `id` or `altname`
        userref (Union[Unset, int]): User reference id

            `userref` is an optional user-specified integer id associated with edit request.
             >  Note: userref from parent order will not be retained on the new order after edit.
        volume (Union[Unset, str]): Order quantity in terms of the base asset.
        displayvol (Union[Unset, str]): Used to edit an iceberg order, this is the visible order quantity in terms of
            the base asset. The rest of the order will be hidden, although the full `volume` can be filled at any time by
            any order of that size or larger that matches in the order book. `displayvol` can only be used with the `limit`
            order type, must be greater than `0`, and less than `volume`.
        price (Union[Unset, str]): Price

            * Limit price for `limit` orders
            * Trigger price for `stop-loss`, `stop-loss-limit`, `take-profit` and `take-profit-limit` orders
        price2 (Union[Unset, str]): Secondary Price

            * Limit price for `stop-loss-limit` and `take-profit-limit` orders

            >  Note: Either `price` or `price2` can be preceded by `+`, `-`, or `#` to specify the order price as an offset
            relative to the last traded price. `+` adds the amount to, and `-` subtracts the amount from the last traded
            price. `#` will either add or subtract the amount to the last traded price, depending on the direction and order
            type used. Relative prices can be suffixed with a `%` to signify the relative amount as a percentage.
        oflags (Union[Unset, Any]): Comma delimited list of order flags. Only these flags can be changed: - post post-
            only order (available when ordertype = limit). All the flags from the parent order are retained except post-
            only. post-only needs to be explicitly mentioned on edit request.
        deadline (Union[Unset, str]): RFC3339 timestamp (e.g. 2021-04-01T00:18:45Z) after which the matching engine
            should reject the new order request, in presence of latency or order queueing. min now() + 2 seconds, max now()
            + 60 seconds.
        cancel_response (Union[Unset, bool]): Used to interpret if client wants to receive pending replace, before the
            order is completely replaced
        validate (Union[Unset, bool]): Validate inputs only. Do not submit order.
    """

    nonce: int
    txid: Union[int, str]
    pair: str
    userref: Union[Unset, int] = UNSET
    volume: Union[Unset, str] = UNSET
    displayvol: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    price2: Union[Unset, str] = UNSET
    oflags: Union[Unset, Any] = UNSET
    deadline: Union[Unset, str] = UNSET
    cancel_response: Union[Unset, bool] = UNSET
    validate: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        txid: Union[int, str]

        txid = self.txid

        pair = self.pair
        userref = self.userref
        volume = self.volume
        displayvol = self.displayvol
        price = self.price
        price2 = self.price2
        oflags = self.oflags
        deadline = self.deadline
        cancel_response = self.cancel_response
        validate = self.validate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "txid": txid,
                "pair": pair,
            }
        )
        if userref is not UNSET:
            field_dict["userref"] = userref
        if volume is not UNSET:
            field_dict["volume"] = volume
        if displayvol is not UNSET:
            field_dict["displayvol"] = displayvol
        if price is not UNSET:
            field_dict["price"] = price
        if price2 is not UNSET:
            field_dict["price2"] = price2
        if oflags is not UNSET:
            field_dict["oflags"] = oflags
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if cancel_response is not UNSET:
            field_dict["cancel_response"] = cancel_response
        if validate is not UNSET:
            field_dict["validate"] = validate

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        def _parse_txid(data: object) -> Union[int, str]:
            return cast(Union[int, str], data)

        txid = _parse_txid(d.pop("txid"))

        pair = d.pop("pair")

        userref = d.pop("userref", UNSET)

        volume = d.pop("volume", UNSET)

        displayvol = d.pop("displayvol", UNSET)

        price = d.pop("price", UNSET)

        price2 = d.pop("price2", UNSET)

        oflags = d.pop("oflags", UNSET)

        deadline = d.pop("deadline", UNSET)

        cancel_response = d.pop("cancel_response", UNSET)

        validate = d.pop("validate", UNSET)

        edit_standard_order_request_body = cls(
            nonce=nonce,
            txid=txid,
            pair=pair,
            userref=userref,
            volume=volume,
            displayvol=displayvol,
            price=price,
            price2=price2,
            oflags=oflags,
            deadline=deadline,
            cancel_response=cancel_response,
            validate=validate,
        )

        edit_standard_order_request_body.additional_properties = d
        return edit_standard_order_request_body

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
