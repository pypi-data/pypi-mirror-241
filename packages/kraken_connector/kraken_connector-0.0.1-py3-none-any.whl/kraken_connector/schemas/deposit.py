from typing import Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.funding import DepositStatus
from ..types import UNSET, Unset


@_attrs_define
class Deposit:
    """deposit

    Attributes:
        method (Union[Unset, str]): Name of deposit method
        aclass (Union[Unset, str]): Asset class
        asset (Union[Unset, str]): Asset
        refid (Union[Unset, str]): Reference ID
        txid (Union[Unset, str]): Method transaction ID
        info (Union[Unset, str]): Method transaction information
        amount (Union[Unset, str]): Amount deposited
        fee (Union[Unset, Any]): Fees paid
        time (Union[Unset, int]): Unix timestamp when request was made
        status (Union[Unset, Any]): Status of deposit<br>
            <sup><sub>For information about the status, please refer to the [IFEX financial transaction
            states](https://github.com/globalcitizen/ifex-protocol/blob/master/draft-ifex-00.txt#L837).</sup></sub>
        status_prop (Union[Unset, DepositStatus]): Addition status properties <sup><sub>(if
            available)</sup></sub><br>
              * `return` A return transaction initiated by Kraken
              * `onhold` Deposit is on hold pending review
        originators (Union[Unset, List[str]]): HTTPClient sending transaction id(s) for deposits that credit with a sweeping
            transaction
    """

    method: Union[Unset, str] = UNSET
    aclass: Union[Unset, str] = UNSET
    asset: Union[Unset, str] = UNSET
    refid: Union[Unset, str] = UNSET
    txid: Union[Unset, str] = UNSET
    info: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    fee: Union[Unset, Any] = UNSET
    time: Union[Unset, int] = UNSET
    status: Union[Unset, Any] = UNSET
    status_prop: Union[Unset, DepositStatus] = UNSET
    originators: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method = self.method
        aclass = self.aclass
        asset = self.asset
        refid = self.refid
        txid = self.txid
        info = self.info
        amount = self.amount
        fee = self.fee
        time = self.time
        status = self.status
        status_prop: Union[Unset, str] = UNSET
        if not isinstance(self.status_prop, Unset):
            status_prop = self.status_prop.value

        originators: Union[Unset, List[str]] = UNSET
        if not isinstance(self.originators, Unset):
            originators = self.originators

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if aclass is not UNSET:
            field_dict["aclass"] = aclass
        if asset is not UNSET:
            field_dict["asset"] = asset
        if refid is not UNSET:
            field_dict["refid"] = refid
        if txid is not UNSET:
            field_dict["txid"] = txid
        if info is not UNSET:
            field_dict["info"] = info
        if amount is not UNSET:
            field_dict["amount"] = amount
        if fee is not UNSET:
            field_dict["fee"] = fee
        if time is not UNSET:
            field_dict["time"] = time
        if status is not UNSET:
            field_dict["status"] = status
        if status_prop is not UNSET:
            field_dict["status-prop"] = status_prop
        if originators is not UNSET:
            field_dict["originators"] = originators

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        method = d.pop("method", UNSET)

        aclass = d.pop("aclass", UNSET)

        asset = d.pop("asset", UNSET)

        refid = d.pop("refid", UNSET)

        txid = d.pop("txid", UNSET)

        info = d.pop("info", UNSET)

        amount = d.pop("amount", UNSET)

        fee = d.pop("fee", UNSET)

        time = d.pop("time", UNSET)

        status = d.pop("status", UNSET)

        _status_prop = d.pop("status-prop", UNSET)
        status_prop: Union[Unset, DepositStatus]
        if isinstance(_status_prop, Unset):
            status_prop = UNSET
        else:
            status_prop = DepositStatus(_status_prop)

        originators = cast(List[str], d.pop("originators", UNSET))

        deposit = cls(
            method=method,
            aclass=aclass,
            asset=asset,
            refid=refid,
            txid=txid,
            info=info,
            amount=amount,
            fee=fee,
            time=time,
            status=status,
            status_prop=status_prop,
            originators=originators,
        )

        deposit.additional_properties = d
        return deposit

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
