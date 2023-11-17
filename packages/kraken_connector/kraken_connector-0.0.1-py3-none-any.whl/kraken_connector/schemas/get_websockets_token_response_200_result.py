from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class GetWebsocketsTokenResponse200Result:
    """
    Attributes:
        token (Union[Unset, str]): Websockets token
        expires (Union[Unset, int]): Time (in seconds) after which the token expires
    """

    token: Union[Unset, str] = UNSET
    expires: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token
        expires = self.expires

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if expires is not UNSET:
            field_dict["expires"] = expires

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        expires = d.pop("expires", UNSET)

        get_websockets_token_response_200_result = cls(
            token=token,
            expires=expires,
        )

        get_websockets_token_response_200_result.additional_properties = d
        return get_websockets_token_response_200_result

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
