from typing import TYPE_CHECKING, Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.deposit import Deposit
    from ..schemas.recent_2_result_type_1 import Recent2ResultType1


@_attrs_define
class Recent2:
    """
    Attributes:
        result (Union['Deposit', 'Recent2ResultType1', Unset]):
        error (Union[Unset, List[str]]):
    """

    result: Union["Deposit", "Recent2ResultType1", Unset] = UNSET
    error: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..schemas.deposit import Deposit

        result: Union[Dict[str, Any], Unset]
        if isinstance(self.result, Unset):
            result = UNSET

        elif isinstance(self.result, Deposit):
            result = UNSET
            if not isinstance(self.result, Unset):
                result = self.result.to_dict()

        else:
            result = UNSET
            if not isinstance(self.result, Unset):
                result = self.result.to_dict()

        error: Union[Unset, List[str]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.deposit import Deposit
        from ..schemas.recent_2_result_type_1 import Recent2ResultType1

        d = src_dict.copy()

        def _parse_result(
            data: object,
        ) -> Union["Deposit", "Recent2ResultType1", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _result_type_0 = data
                result_type_0: Union[Unset, Deposit]
                if isinstance(_result_type_0, Unset):
                    result_type_0 = UNSET
                else:
                    result_type_0 = Deposit.from_dict(_result_type_0)

                return result_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _result_type_1 = data
            result_type_1: Union[Unset, Recent2ResultType1]
            if isinstance(_result_type_1, Unset):
                result_type_1 = UNSET
            else:
                result_type_1 = Recent2ResultType1.from_dict(_result_type_1)

            return result_type_1

        result = _parse_result(d.pop("result", UNSET))

        error = cast(List[str], d.pop("error", UNSET))

        recent_2 = cls(
            result=result,
            error=error,
        )

        recent_2.additional_properties = d
        return recent_2

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
