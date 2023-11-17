from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.market_data import SystemStatus
from ..types import UNSET, Unset


@_attrs_define
class GetSystemStatusResponse200Result:
    """
    Attributes:
        status (Union[Unset, SystemStatus]): Current system status:
            * `online`  Kraken is operating normally. All order types may be submitted and trades can occur.
            * `maintenance`  The exchange is offline. No new orders or cancellations may be submitted.
            * `cancel_only`  Resting (open) orders can be cancelled but no new orders may be submitted. No trades will
            occur.
            * `post_only`  Only post-only limit orders can be submitted. Existing orders may still be cancelled. No trades
            will occur.
        timestamp (Union[Unset, str]): Current timestamp (RFC3339)
    """

    status: Union[Unset, SystemStatus] = UNSET
    timestamp: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, SystemStatus]
        status = UNSET if isinstance(_status, Unset) else SystemStatus(_status)

        timestamp = d.pop("timestamp", UNSET)

        get_system_status_response_200_result = cls(
            status=status,
            timestamp=timestamp,
        )

        get_system_status_response_200_result.additional_properties = d
        return get_system_status_response_200_result

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
