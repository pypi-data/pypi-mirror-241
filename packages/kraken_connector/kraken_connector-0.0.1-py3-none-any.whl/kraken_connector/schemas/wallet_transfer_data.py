from typing import Any, Dict, List, Self

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.funding import TypeWallet
from ..types import UNSET, Unset


@_attrs_define
class WalletTransferData:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        asset (str): Asset to transfer (asset ID or `altname`) Example: XBT.
        from_ (TypeWallet.SPOT_WALLET): Source wallet, must be "Spot Wallet"
        to (TypeWallet.FUTURES_WALLET): Destination wallet, must be "Futures Wallet"
        amount (str): Amount to transfer
    """

    nonce: int
    asset: str
    from_: TypeWallet.SPOT_WALLET
    to: TypeWallet.FUTURES_WALLET
    amount: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        asset = self.asset
        from_ = self.from_.value

        to = self.to.value

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "asset": asset,
                "from": from_,
                "to": to,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        asset = d.pop("asset")
        from_wallet = d.pop("from", UNSET)
        if not (
            isinstance(from_wallet, Unset)
            or from_wallet == TypeWallet.SPOT_WALLET.value
        ):
            raise ValueError(
                "The wallet from which a transfer may be made is restricted to the Spot"
                " Wallet for this endpoint."
            )
        from_ = TypeWallet.SPOT_WALLET
        to_wallet = d.pop("to", UNSET)
        if not (
            isinstance(to_wallet, Unset) or to_wallet == TypeWallet.FUTURES_WALLET.value
        ):
            raise ValueError(
                "The wallet to which a transfer may be made is restricted to the"
                " Futures Wallet for this endpoint."
            )
        to = TypeWallet.FUTURES_WALLET

        amount = d.pop("amount")

        wallet_transfer_data = cls(
            nonce=nonce,
            asset=asset,
            from_=from_,
            to=to,
            amount=amount,
        )

        wallet_transfer_data.additional_properties = d
        return wallet_transfer_data

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
