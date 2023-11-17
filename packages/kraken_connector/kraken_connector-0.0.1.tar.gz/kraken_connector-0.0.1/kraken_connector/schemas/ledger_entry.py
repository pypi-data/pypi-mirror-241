from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.account_data import LedgerEntryType
from ..types import UNSET, Unset


@_attrs_define
class LedgerEntry:
    """Ledger Entry

    Attributes:
        refid (Union[Unset, str]): Reference Id
        time (Union[Unset, float]): Unix timestamp of ledger
        type (Union[Unset, LedgerEntryType]): Type of ledger entry
        subtype (Union[Unset, str]): Additional info relating to the ledger entry type, where applicable
        aclass (Union[Unset, str]): Asset class
        asset (Union[Unset, str]): Asset
        amount (Union[Unset, str]): Transaction amount
        fee (Union[Unset, str]): Transaction fee
        balance (Union[Unset, str]): Resulting balance
    """

    refid: Union[Unset, str] = UNSET
    time: Union[Unset, float] = UNSET
    type: Union[Unset, LedgerEntryType] = UNSET
    subtype: Union[Unset, str] = UNSET
    aclass: Union[Unset, str] = UNSET
    asset: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    fee: Union[Unset, str] = UNSET
    balance: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refid = self.refid
        time = self.time
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        subtype = self.subtype
        aclass = self.aclass
        asset = self.asset
        amount = self.amount
        fee = self.fee
        balance = self.balance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refid is not UNSET:
            field_dict["refid"] = refid
        if time is not UNSET:
            field_dict["time"] = time
        if type is not UNSET:
            field_dict["type"] = type
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if aclass is not UNSET:
            field_dict["aclass"] = aclass
        if asset is not UNSET:
            field_dict["asset"] = asset
        if amount is not UNSET:
            field_dict["amount"] = amount
        if fee is not UNSET:
            field_dict["fee"] = fee
        if balance is not UNSET:
            field_dict["balance"] = balance

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        refid = d.pop("refid", UNSET)

        time = d.pop("time", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, LedgerEntryType]
        type = UNSET if isinstance(_type, Unset) else LedgerEntryType(_type)

        subtype = d.pop("subtype", UNSET)

        aclass = d.pop("aclass", UNSET)

        asset = d.pop("asset", UNSET)

        amount = d.pop("amount", UNSET)

        fee = d.pop("fee", UNSET)

        balance = d.pop("balance", UNSET)

        ledger_entry = cls(
            refid=refid,
            time=time,
            type=type,
            subtype=subtype,
            aclass=aclass,
            asset=asset,
            amount=amount,
            fee=fee,
            balance=balance,
        )

        ledger_entry.additional_properties = d
        return ledger_entry

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
