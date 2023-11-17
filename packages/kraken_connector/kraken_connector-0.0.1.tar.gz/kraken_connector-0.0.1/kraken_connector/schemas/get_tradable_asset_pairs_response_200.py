from typing import TYPE_CHECKING, Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.get_tradable_asset_pairs_response_200_result import (
        GetTradableAssetPairsResponse200Result,
    )


@_attrs_define
class GetTradableAssetPairsResponse200:
    """
    Example:
        {'error': [], 'result': {'XETHXXBT': {'altname': 'ETHXBT', 'wsname': 'ETH/XBT', 'aclass_base': 'currency',
            'base': 'XETH', 'aclass_quote': 'currency', 'quote': 'XXBT', 'lot': 'unit', 'cost_decimals': 6, 'pair_decimals':
            5, 'lot_decimals': 8, 'lot_multiplier': 1, 'leverage_buy': [2, 3, 4, 5], 'leverage_sell': [2, 3, 4, 5], 'fees':
            [[0, 0.26], [50000, 0.24], [100000, 0.22], [250000, 0.2], [500000, 0.18], [1000000, 0.16], [2500000, 0.14],
            [5000000, 0.12], [10000000, 0.1]], 'fees_maker': [[0, 0.16], [50000, 0.14], [100000, 0.12], [250000, 0.1],
            [500000, 0.08], [1000000, 0.06], [2500000, 0.04], [5000000, 0.02], [10000000, 0]], 'fee_volume_currency':
            'ZUSD', 'margin_call': 80, 'margin_stop': 40, 'ordermin': '0.01', 'costmin': '0.00002', 'tick_size': '0.00001',
            'status': 'online', 'long_position_limit': 1100, 'short_position_limit': 400}, 'XXBTZUSD': {'altname': 'XBTUSD',
            'wsname': 'XBT/USD', 'aclass_base': 'currency', 'base': 'XXBT', 'aclass_quote': 'currency', 'quote': 'ZUSD',
            'lot': 'unit', 'cost_decimals': 5, 'pair_decimals': 1, 'lot_decimals': 8, 'lot_multiplier': 1, 'leverage_buy':
            [2, 3, 4, 5], 'leverage_sell': [2, 3, 4, 5], 'fees': [[0, 0.26], [50000, 0.24], [100000, 0.22], [250000, 0.2],
            [500000, 0.18], [1000000, 0.16], [2500000, 0.14], [5000000, 0.12], [10000000, 0.1]], 'fees_maker': [[0, 0.16],
            [50000, 0.14], [100000, 0.12], [250000, 0.1], [500000, 0.08], [1000000, 0.06], [2500000, 0.04], [5000000, 0.02],
            [10000000, 0]], 'fee_volume_currency': 'ZUSD', 'margin_call': 80, 'margin_stop': 40, 'ordermin': '0.0001',
            'costmin': '0.5', 'tick_size': '0.1', 'status': 'online', 'long_position_limit': 250, 'short_position_limit':
            200}}}

    Attributes:
        result (Union[Unset, GetTradableAssetPairsResponse200Result]): Pair names and their info
        error (Union[Unset, List[str]]):
    """

    result: Union[Unset, "GetTradableAssetPairsResponse200Result"] = UNSET
    error: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, Dict[str, Any]] = UNSET
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
        from ..schemas.get_tradable_asset_pairs_response_200_result import (
            GetTradableAssetPairsResponse200Result,
        )

        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, GetTradableAssetPairsResponse200Result]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = GetTradableAssetPairsResponse200Result.from_dict(_result)

        error = cast(List[str], d.pop("error", UNSET))

        get_tradable_asset_pairs_response_200 = cls(
            result=result,
            error=error,
        )

        get_tradable_asset_pairs_response_200.additional_properties = d
        return get_tradable_asset_pairs_response_200

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
