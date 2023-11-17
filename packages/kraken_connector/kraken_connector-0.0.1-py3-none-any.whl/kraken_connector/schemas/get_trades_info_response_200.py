from typing import TYPE_CHECKING, Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.get_trades_info_response_200_result import (
        GetTradesInfoResponse200Result,
    )


@_attrs_define
class GetTradesInfoResponse200:
    """
    Example:
        {'error': [], 'result': {'THVRQM-33VKH-UCI7BS': {'ordertxid': 'OQCLML-BW3P3-BUCMWZ', 'postxid':
            'TKH2SE-M7IF5-CFI7LT', 'pair': 'XXBTZUSD', 'time': 1688667796.8802, 'type': 'buy', 'ordertype': 'limit',
            'price': '30010.00000', 'cost': '600.20000', 'fee': '0.00000', 'vol': '0.02000000', 'margin': '0.00000', 'misc':
            ''}, 'TTEUX3-HDAAA-RC2RUO': {'ordertxid': 'OH76VO-UKWAD-PSBDX6', 'postxid': 'TKH2SE-M7IF5-CFI7LT', 'pair':
            'XXBTZEUR', 'time': 1688082549.3138, 'type': 'buy', 'ordertype': 'limit', 'price': '27732.00000', 'cost':
            '0.20020', 'fee': '0.00000', 'vol': '0.00020000', 'margin': '0.00000', 'misc': ''}}}

    Attributes:
        result (Union[Unset, GetTradesInfoResponse200Result]): Trade info
        error (Union[Unset, List[List[str]]]):
    """

    result: Union[Unset, "GetTradesInfoResponse200Result"] = UNSET
    error: Union[Unset, List[List[str]]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        error: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.error, Unset):
            error = []
            for error_item_data in self.error:
                error_item = error_item_data

                error.append(error_item)

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
        from ..schemas.get_trades_info_response_200_result import (
            GetTradesInfoResponse200Result,
        )

        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, GetTradesInfoResponse200Result]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = GetTradesInfoResponse200Result.from_dict(_result)

        error = []
        _error = d.pop("error", UNSET)
        for error_item_data in _error or []:
            error_item = cast(List[str], error_item_data)

            error.append(error_item)

        get_trades_info_response_200 = cls(
            result=result,
            error=error,
        )

        get_trades_info_response_200.additional_properties = d
        return get_trades_info_response_200

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
