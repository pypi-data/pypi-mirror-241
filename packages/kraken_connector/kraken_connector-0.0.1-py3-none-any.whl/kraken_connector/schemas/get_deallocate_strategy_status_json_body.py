from typing import TYPE_CHECKING, Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.get_deallocate_strategy_status_json_body_nonce import (
        GetDeallocateStrategyStatusJsonBodyNonce,
    )


@_attrs_define
class GetDeallocateStrategyStatusJsonBody:
    """
    Attributes:
        nonce (GetDeallocateStrategyStatusJsonBodyNonce):
        strategy_id (str): ID of the earn strategy, call `Earn/Strategies` to list availble strategies
        otp (Union[Unset, None, str]): https://docs.kraken.com/rest/#section/Authentication/Nonce-and-2FA
    """

    nonce: "GetDeallocateStrategyStatusJsonBodyNonce"
    strategy_id: str
    otp: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce.to_dict()

        strategy_id = self.strategy_id
        otp = self.otp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "strategy_id": strategy_id,
            }
        )
        if otp is not UNSET:
            field_dict["otp"] = otp

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.get_deallocate_strategy_status_json_body_nonce import (
            GetDeallocateStrategyStatusJsonBodyNonce,
        )

        d = src_dict.copy()
        nonce = GetDeallocateStrategyStatusJsonBodyNonce.from_dict(d.pop("nonce"))

        strategy_id = d.pop("strategy_id")

        otp = d.pop("otp", UNSET)

        get_deallocate_strategy_status_json_body = cls(
            nonce=nonce,
            strategy_id=strategy_id,
            otp=otp,
        )

        get_deallocate_strategy_status_json_body.additional_properties = d
        return get_deallocate_strategy_status_json_body

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
