from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class AllocateStrategyJsonBodyNonce:
    """
    Attributes:
        nonce (Union[Unset, int]): Nonce used in construction of `API-Sign` header
    """

    nonce: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nonce is not UNSET:
            field_dict["nonce"] = nonce

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        nonce = d.pop("nonce", UNSET)

        allocate_strategy_json_body_nonce = cls(
            nonce=nonce,
        )

        allocate_strategy_json_body_nonce.additional_properties = d
        return allocate_strategy_json_body_nonce

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
