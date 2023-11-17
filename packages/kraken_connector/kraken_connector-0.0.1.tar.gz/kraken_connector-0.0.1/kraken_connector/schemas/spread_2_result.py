from typing import Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class Spread2Result:
    """
    Attributes:
        last (Union[Unset, int]): ID to be used as since when polling for new spread data
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
            for componentsschemasspread_item_data in prop:
                componentsschemasspread_item = []
                for (
                    componentsschemasspread_item_item_data
                ) in componentsschemasspread_item_data:
                    componentsschemasspread_item_item: Union[int, str]

                    componentsschemasspread_item_item = (
                        componentsschemasspread_item_item_data
                    )

                    componentsschemasspread_item.append(
                        componentsschemasspread_item_item
                    )

                field_dict[prop_name].append(componentsschemasspread_item)

        field_dict.update({})
        if last is not UNSET:
            field_dict["last"] = last

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        last = d.pop("last", UNSET)

        spread_2_result = cls(
            last=last,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for componentsschemasspread_item_data in _additional_property:
                componentsschemasspread_item = []
                _componentsschemasspread_item = componentsschemasspread_item_data
                for (
                    componentsschemasspread_item_item_data
                ) in _componentsschemasspread_item:

                    def _parse_componentsschemasspread_item_item(
                        data: object,
                    ) -> Union[int, str]:
                        return cast(Union[int, str], data)

                    componentsschemasspread_item_item = (
                        _parse_componentsschemasspread_item_item(
                            componentsschemasspread_item_item_data
                        )
                    )

                    componentsschemasspread_item.append(
                        componentsschemasspread_item_item
                    )

                additional_property.append(componentsschemasspread_item)

            additional_properties[prop_name] = additional_property

        spread_2_result.additional_properties = additional_properties
        return spread_2_result

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
