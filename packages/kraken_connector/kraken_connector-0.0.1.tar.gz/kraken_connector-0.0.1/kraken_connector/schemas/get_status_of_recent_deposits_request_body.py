from typing import Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class GetStatusOfRecentDepositsRequestBody:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        asset (Union[Unset, str]): Filter for specific asset being deposited
        method (Union[Unset, str]): Filter for specific name of deposit method
        start (Union[Unset, str]): Start timestamp, deposits created strictly before will not be included in the
            response
        end (Union[Unset, str]): End timestamp, deposits created stricly after will be not be included in the response
        cursor (Union[Unset, bool, str]): true/false to enable/disable paginated response (boolean) or cursor for next
            page of results (string), default false
    """

    nonce: int
    asset: Union[Unset, str] = UNSET
    method: Union[Unset, str] = UNSET
    start: Union[Unset, str] = UNSET
    end: Union[Unset, str] = UNSET
    cursor: Union[Unset, bool, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        asset = self.asset
        method = self.method
        start = self.start
        end = self.end
        cursor: Union[Unset, bool, str]
        cursor = UNSET if isinstance(self.cursor, Unset) else self.cursor

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
            }
        )
        if asset is not UNSET:
            field_dict["asset"] = asset
        if method is not UNSET:
            field_dict["method"] = method
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        asset = d.pop("asset", UNSET)

        method = d.pop("method", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        def _parse_cursor(data: object) -> Union[Unset, bool, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, bool, str], data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        get_status_of_recent_deposits_request_body = cls(
            nonce=nonce,
            asset=asset,
            method=method,
            start=start,
            end=end,
            cursor=cursor,
        )

        get_status_of_recent_deposits_request_body.additional_properties = d
        return get_status_of_recent_deposits_request_body

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
