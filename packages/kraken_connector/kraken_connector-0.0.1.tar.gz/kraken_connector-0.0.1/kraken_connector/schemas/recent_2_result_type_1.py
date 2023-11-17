from typing import TYPE_CHECKING, Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.deposit import Deposit


@_attrs_define
class Recent2ResultType1:
    """
    Attributes:
        deposit (Union[Unset, Deposit]): deposit
        next_cursor (Union[Unset, str]): If pagination is set via `cursor` parameter, provides next input to use for
            `cursor` in pagination
    """

    deposit: Union[Unset, "Deposit"] = UNSET
    next_cursor: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deposit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deposit, Unset):
            deposit = self.deposit.to_dict()

        next_cursor = self.next_cursor

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deposit is not UNSET:
            field_dict["deposit"] = deposit
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.deposit import Deposit

        d = src_dict.copy()
        _deposit = d.pop("deposit", UNSET)
        deposit: Union[Unset, Deposit]
        deposit = UNSET if isinstance(_deposit, Unset) else Deposit.from_dict(_deposit)

        next_cursor = d.pop("next_cursor", UNSET)

        recent_2_result_type_1 = cls(
            deposit=deposit,
            next_cursor=next_cursor,
        )

        recent_2_result_type_1.additional_properties = d
        return recent_2_result_type_1

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
