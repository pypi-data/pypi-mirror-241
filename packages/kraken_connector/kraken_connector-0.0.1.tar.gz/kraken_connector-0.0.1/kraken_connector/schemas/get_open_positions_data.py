from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.account_data import OpenPositionsDataConsolidation
from ..types import UNSET, Unset


@_attrs_define
class GetOpenPositionsData:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        txid (Union[Unset, str]): Comma delimited list of txids to limit output to
        docalcs (Union[Unset, bool]): Whether to include P&L calculations
        consolidation (Union[Unset, OpenPositionsDataConsolidation]): Consolidate positions by market/pair
    """

    nonce: int
    txid: Union[Unset, str] = UNSET
    docalcs: Union[Unset, bool] = False
    consolidation: Union[Unset, OpenPositionsDataConsolidation] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        txid = self.txid
        docalcs = self.docalcs
        consolidation: Union[Unset, str] = UNSET
        if not isinstance(self.consolidation, Unset):
            consolidation = self.consolidation.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
            }
        )
        if txid is not UNSET:
            field_dict["txid"] = txid
        if docalcs is not UNSET:
            field_dict["docalcs"] = docalcs
        if consolidation is not UNSET:
            field_dict["consolidation"] = consolidation

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        txid = d.pop("txid", UNSET)

        docalcs = d.pop("docalcs", UNSET)

        _consolidation = d.pop("consolidation", UNSET)
        consolidation: Union[Unset, OpenPositionsDataConsolidation]
        if isinstance(_consolidation, Unset):
            consolidation = UNSET
        else:
            consolidation = OpenPositionsDataConsolidation(_consolidation)

        get_open_positions_data = cls(
            nonce=nonce,
            txid=txid,
            docalcs=docalcs,
            consolidation=consolidation,
        )

        get_open_positions_data.additional_properties = d
        return get_open_positions_data

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
