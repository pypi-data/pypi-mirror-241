from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.account_data import ReportFileFormat, ReportType
from ..types import UNSET, Unset


@_attrs_define
class AddExportData:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        report (ReportType): Type of data to export
        description (str): Description for the export
        format_ (Union[Unset, ReportFileFormat]): File format to export Default: ReportFileFormat.CSV.
        fields (Union[Unset, str]): Comma-delimited list of fields to include

            * `trades`: ordertxid, time, ordertype, price, cost, fee, vol, margin, misc, ledgers
            * `ledgers`: refid, time, type, aclass, asset, amount, fee, balance
             Default: 'all'.
        starttm (Union[Unset, int]): UNIX timestamp for report start time (default 1st of the current month)
        endtm (Union[Unset, int]): UNIX timestamp for report end time (default now)
    """

    nonce: int
    report: ReportType
    description: str
    format_: Union[Unset, ReportFileFormat] = ReportFileFormat.CSV
    fields: Union[Unset, str] = "all"
    starttm: Union[Unset, int] = UNSET
    endtm: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        report = self.report.value

        description = self.description
        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        fields = self.fields
        starttm = self.starttm
        endtm = self.endtm

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "report": report,
                "description": description,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_
        if fields is not UNSET:
            field_dict["fields"] = fields
        if starttm is not UNSET:
            field_dict["starttm"] = starttm
        if endtm is not UNSET:
            field_dict["endtm"] = endtm

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        report = ReportType(d.pop("report"))

        description = d.pop("description")

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, ReportFileFormat]
        format_ = UNSET if isinstance(_format_, Unset) else ReportFileFormat(_format_)

        fields = d.pop("fields", UNSET)

        starttm = d.pop("starttm", UNSET)

        endtm = d.pop("endtm", UNSET)

        add_export_data = cls(
            nonce=nonce,
            report=report,
            description=description,
            format_=format_,
            fields=fields,
            starttm=starttm,
            endtm=endtm,
        )

        add_export_data.additional_properties = d
        return add_export_data

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
