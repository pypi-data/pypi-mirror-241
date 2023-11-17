from typing import TYPE_CHECKING, Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.list_allocations_json_body_nonce import ListAllocationsJsonBodyNonce


@_attrs_define
class ListAllocationsJsonBody:
    """Page request

    Attributes:
        nonce (ListAllocationsJsonBodyNonce):
        ascending (Union[Unset, None, bool]): `true` to sort ascending, `false` (the default) for descending.
        converted_asset (Union[Unset, None, str]): A secondary currency to express the value of your allocations (the
            default is USD).
        hide_zero_allocations (Union[Unset, None, bool]): Omit entries for strategies that were used in the past but now
            they don't hold any allocation (the default is `false`)
        otp (Union[Unset, None, str]): https://docs.kraken.com/rest/#section/Authentication/Nonce-and-2FA
    """

    nonce: "ListAllocationsJsonBodyNonce"
    ascending: Union[Unset, None, bool] = UNSET
    converted_asset: Union[Unset, None, str] = UNSET
    hide_zero_allocations: Union[Unset, None, bool] = UNSET
    otp: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce.to_dict()

        ascending = self.ascending
        converted_asset = self.converted_asset
        hide_zero_allocations = self.hide_zero_allocations
        otp = self.otp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
            }
        )
        if ascending is not UNSET:
            field_dict["ascending"] = ascending
        if converted_asset is not UNSET:
            field_dict["converted_asset"] = converted_asset
        if hide_zero_allocations is not UNSET:
            field_dict["hide_zero_allocations"] = hide_zero_allocations
        if otp is not UNSET:
            field_dict["otp"] = otp

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.list_allocations_json_body_nonce import (
            ListAllocationsJsonBodyNonce,
        )

        d = src_dict.copy()
        nonce = ListAllocationsJsonBodyNonce.from_dict(d.pop("nonce"))

        ascending = d.pop("ascending", UNSET)

        converted_asset = d.pop("converted_asset", UNSET)

        hide_zero_allocations = d.pop("hide_zero_allocations", UNSET)

        otp = d.pop("otp", UNSET)

        list_allocations_json_body = cls(
            nonce=nonce,
            ascending=ascending,
            converted_asset=converted_asset,
            hide_zero_allocations=hide_zero_allocations,
            otp=otp,
        )

        list_allocations_json_body.additional_properties = d
        return list_allocations_json_body

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
