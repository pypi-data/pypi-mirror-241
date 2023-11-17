from typing import TYPE_CHECKING, Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.earn import StrategyLockType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.list_strategies_json_body_nonce import ListStrategiesJsonBodyNonce


@_attrs_define
class ListStrategiesJsonBody:
    """List strategies parameters

    Attributes:
        nonce (ListStrategiesJsonBodyNonce):
        ascending (Union[Unset, None, bool]): `true` to sort ascending, `false` (the default) for descending.
        asset (Union[Unset, None, str]): Filter strategies by asset name
        cursor (Union[Unset, None, str]): None to start at beginning/end, otherwise next page ID
        limit (Union[Unset, None, int]): How many items to return per page. Note that the limit may be cap'd to lower
            value in the application code.
        lock_type (Union[Unset, None, List[StrategyLockType]]): Filter strategies by lock type
        otp (Union[Unset, None, str]): https://docs.kraken.com/rest/#section/Authentication/Nonce-and-2FA
    """

    nonce: "ListStrategiesJsonBodyNonce"
    ascending: Union[Unset, None, bool] = UNSET
    asset: Union[Unset, None, str] = UNSET
    cursor: Union[Unset, None, str] = UNSET
    limit: Union[Unset, None, int] = UNSET
    lock_type: Union[Unset, None, List[StrategyLockType]] = UNSET
    otp: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce.to_dict()

        ascending = self.ascending
        asset = self.asset
        cursor = self.cursor
        limit = self.limit
        lock_type: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.lock_type, Unset):
            if self.lock_type is None:
                lock_type = None
            else:
                lock_type = []
                for lock_type_item_data in self.lock_type:
                    lock_type_item = lock_type_item_data.value

                    lock_type.append(lock_type_item)

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
        if asset is not UNSET:
            field_dict["asset"] = asset
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if limit is not UNSET:
            field_dict["limit"] = limit
        if lock_type is not UNSET:
            field_dict["lock_type"] = lock_type
        if otp is not UNSET:
            field_dict["otp"] = otp

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.list_strategies_json_body_nonce import (
            ListStrategiesJsonBodyNonce,
        )

        d = src_dict.copy()
        nonce = ListStrategiesJsonBodyNonce.from_dict(d.pop("nonce"))

        ascending = d.pop("ascending", UNSET)

        asset = d.pop("asset", UNSET)

        cursor = d.pop("cursor", UNSET)

        limit = d.pop("limit", UNSET)

        lock_type = []
        _lock_type = d.pop("lock_type", UNSET)
        for lock_type_item_data in _lock_type or []:
            lock_type_item = StrategyLockType(lock_type_item_data)

            lock_type.append(lock_type_item)

        otp = d.pop("otp", UNSET)

        list_strategies_json_body = cls(
            nonce=nonce,
            ascending=ascending,
            asset=asset,
            cursor=cursor,
            limit=limit,
            lock_type=lock_type,
            otp=otp,
        )

        list_strategies_json_body.additional_properties = d
        return list_strategies_json_body

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
