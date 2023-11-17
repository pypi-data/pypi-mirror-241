from typing import Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class TradesResult:
    """
    Attributes:
        last (Union[Unset, str]): ID to be used as since when polling for new trade data
    """

    last: Union[Unset, str] = UNSET
    additional_properties: Dict[str, List[List[Union[float, str]]]] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        last = self.last

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for componentsschemastrade_item_data in prop:
                componentsschemastrade_item = []
                for (
                    componentsschemastrade_item_item_data
                ) in componentsschemastrade_item_data:
                    componentsschemastrade_item_item: Union[float, str]

                    componentsschemastrade_item_item = (
                        componentsschemastrade_item_item_data
                    )

                    componentsschemastrade_item.append(componentsschemastrade_item_item)

                field_dict[prop_name].append(componentsschemastrade_item)

        field_dict.update({})
        if last is not UNSET:
            field_dict["last"] = last

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        last = d.pop("last", UNSET)

        trades_result = cls(
            last=last,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for componentsschemastrade_item_data in _additional_property:
                componentsschemastrade_item = []
                _componentsschemastrade_item = componentsschemastrade_item_data
                for (
                    componentsschemastrade_item_item_data
                ) in _componentsschemastrade_item:

                    def _parse_componentsschemastrade_item_item(
                        data: object,
                    ) -> Union[float, str]:
                        return cast(Union[float, str], data)

                    componentsschemastrade_item_item = (
                        _parse_componentsschemastrade_item_item(
                            componentsschemastrade_item_item_data
                        )
                    )

                    componentsschemastrade_item.append(componentsschemastrade_item_item)

                additional_property.append(componentsschemastrade_item)

            additional_properties[prop_name] = additional_property

        trades_result.additional_properties = additional_properties
        return trades_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List[List[Union[float, str]]]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List[List[Union[float, str]]]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
