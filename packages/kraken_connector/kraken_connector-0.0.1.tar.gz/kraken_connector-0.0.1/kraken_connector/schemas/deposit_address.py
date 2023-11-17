from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class DepositAddress:
    """Deposit Address

    Attributes:
        address (Union[Unset, str]): Deposit Address
        expiretm (Union[Unset, str]): Expiration time in unix timestamp, or 0 if not expiring
        new (Union[Unset, bool]): Whether or not address has ever been used
        memo (Union[Unset, str]): Only returned for [STX](https://support.kraken.com/hc/en-
            us/articles/10902306995860-Memo-for-Stacks-STX-deposits), [XLM](https://support.kraken.com/hc/en-
            us/articles/360000184543-Memo-for-Stellar-Lumens-XLM-deposits), and [EOS](https://support.kraken.com/hc/en-
            us/articles/360001099203-Memo-for-EOS-deposits) deposit addresses
        tag (Union[Unset, Any]): Only returned for [XRP](https://support.kraken.com/hc/en-
            us/articles/360000184443-Destination-Tag-for-Ripple-XRP-deposits) deposit addresses
    """

    address: Union[Unset, str] = UNSET
    expiretm: Union[Unset, str] = UNSET
    new: Union[Unset, bool] = UNSET
    memo: Union[Unset, str] = UNSET
    tag: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        expiretm = self.expiretm
        new = self.new
        memo = self.memo
        tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if expiretm is not UNSET:
            field_dict["expiretm"] = expiretm
        if new is not UNSET:
            field_dict["new"] = new
        if memo is not UNSET:
            field_dict["memo"] = memo
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        expiretm = d.pop("expiretm", UNSET)

        new = d.pop("new", UNSET)

        memo = d.pop("memo", UNSET)

        tag = d.pop("tag", UNSET)

        deposit_address = cls(
            address=address,
            expiretm=expiretm,
            new=new,
            memo=memo,
            tag=tag,
        )

        deposit_address.additional_properties = d
        return deposit_address

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
