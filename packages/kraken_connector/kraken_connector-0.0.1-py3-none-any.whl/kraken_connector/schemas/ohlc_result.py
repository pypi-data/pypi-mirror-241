from typing import Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class OhlcResult:
    """
    Attributes:
        last (Union[Unset, int]): ID to be used as since when polling for new, committed OHLC data
    """

    last: Union[Unset, int] = UNSET
    additional_properties: Dict[str, List[List[Union[int, str]]]] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        last = self.last

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for componentsschemastick_data_item_data in prop:
                componentsschemastick_data_item = []
                for (
                    componentsschemastick_data_item_item_data
                ) in componentsschemastick_data_item_data:
                    componentsschemastick_data_item_item: Union[int, str]

                    componentsschemastick_data_item_item = (
                        componentsschemastick_data_item_item_data
                    )

                    componentsschemastick_data_item.append(
                        componentsschemastick_data_item_item
                    )

                field_dict[prop_name].append(componentsschemastick_data_item)

        field_dict.update({})
        if last is not UNSET:
            field_dict["last"] = last

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        last = d.pop("last", UNSET)

        ohlc_result = cls(
            last=last,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for componentsschemastick_data_item_data in _additional_property:
                componentsschemastick_data_item = []
                _componentsschemastick_data_item = componentsschemastick_data_item_data
                for (
                    componentsschemastick_data_item_item_data
                ) in _componentsschemastick_data_item:

                    def _parse_componentsschemastick_data_item_item(
                        data: object,
                    ) -> Union[int, str]:
                        return cast(Union[int, str], data)

                    componentsschemastick_data_item_item = (
                        _parse_componentsschemastick_data_item_item(
                            componentsschemastick_data_item_item_data
                        )
                    )

                    componentsschemastick_data_item.append(
                        componentsschemastick_data_item_item
                    )

                additional_property.append(componentsschemastick_data_item)

            additional_properties[prop_name] = additional_property

        ohlc_result.additional_properties = additional_properties
        return ohlc_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List[List[Union[int, str]]]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List[List[Union[int, str]]]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
