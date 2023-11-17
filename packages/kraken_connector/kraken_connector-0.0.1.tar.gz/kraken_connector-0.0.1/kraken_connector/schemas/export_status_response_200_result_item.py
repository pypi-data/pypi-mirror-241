from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.account_data import ReportRequestStatus
from ..types import UNSET, Unset


@_attrs_define
class ExportStatusResponse200ResultItem:
    """
    Attributes:
        id (Union[Unset, str]): Report ID
        descr (Union[Unset, str]):
        format_ (Union[Unset, str]):
        report (Union[Unset, str]):
        subtype (Union[Unset, str]):
        status (Union[Unset, ReportRequestStatus]): Status of the report
        flags (Union[Unset, str]):
        fields (Union[Unset, str]):
        createdtm (Union[Unset, str]): UNIX timestamp of report request
        expiretm (Union[Unset, str]):
        starttm (Union[Unset, str]): UNIX timestamp report processing began
        completedtm (Union[Unset, str]): UNIX timestamp report processing finished
        datastarttm (Union[Unset, str]): UNIX timestamp of the report data start time
        dataendtm (Union[Unset, str]): UNIX timestamp of the report data end time
        aclass (Union[Unset, str]):
        asset (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    format_: Union[Unset, str] = UNSET
    report: Union[Unset, str] = UNSET
    subtype: Union[Unset, str] = UNSET
    status: Union[Unset, ReportRequestStatus] = UNSET
    flags: Union[Unset, str] = UNSET
    fields: Union[Unset, str] = UNSET
    createdtm: Union[Unset, str] = UNSET
    expiretm: Union[Unset, str] = UNSET
    starttm: Union[Unset, str] = UNSET
    completedtm: Union[Unset, str] = UNSET
    datastarttm: Union[Unset, str] = UNSET
    dataendtm: Union[Unset, str] = UNSET
    aclass: Union[Unset, str] = UNSET
    asset: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        descr = self.descr
        format_ = self.format_
        report = self.report
        subtype = self.subtype
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        flags = self.flags
        fields = self.fields
        createdtm = self.createdtm
        expiretm = self.expiretm
        starttm = self.starttm
        completedtm = self.completedtm
        datastarttm = self.datastarttm
        dataendtm = self.dataendtm
        aclass = self.aclass
        asset = self.asset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if descr is not UNSET:
            field_dict["descr"] = descr
        if format_ is not UNSET:
            field_dict["format"] = format_
        if report is not UNSET:
            field_dict["report"] = report
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if status is not UNSET:
            field_dict["status"] = status
        if flags is not UNSET:
            field_dict["flags"] = flags
        if fields is not UNSET:
            field_dict["fields"] = fields
        if createdtm is not UNSET:
            field_dict["createdtm"] = createdtm
        if expiretm is not UNSET:
            field_dict["expiretm"] = expiretm
        if starttm is not UNSET:
            field_dict["starttm"] = starttm
        if completedtm is not UNSET:
            field_dict["completedtm"] = completedtm
        if datastarttm is not UNSET:
            field_dict["datastarttm"] = datastarttm
        if dataendtm is not UNSET:
            field_dict["dataendtm"] = dataendtm
        if aclass is not UNSET:
            field_dict["aclass"] = aclass
        if asset is not UNSET:
            field_dict["asset"] = asset

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        descr = d.pop("descr", UNSET)

        format_ = d.pop("format", UNSET)

        report = d.pop("report", UNSET)

        subtype = d.pop("subtype", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ReportRequestStatus]
        status = UNSET if isinstance(_status, Unset) else ReportRequestStatus(_status)

        flags = d.pop("flags", UNSET)

        fields = d.pop("fields", UNSET)

        createdtm = d.pop("createdtm", UNSET)

        expiretm = d.pop("expiretm", UNSET)

        starttm = d.pop("starttm", UNSET)

        completedtm = d.pop("completedtm", UNSET)

        datastarttm = d.pop("datastarttm", UNSET)

        dataendtm = d.pop("dataendtm", UNSET)

        aclass = d.pop("aclass", UNSET)

        asset = d.pop("asset", UNSET)

        export_status_response_200_result_item = cls(
            id=id,
            descr=descr,
            format_=format_,
            report=report,
            subtype=subtype,
            status=status,
            flags=flags,
            fields=fields,
            createdtm=createdtm,
            expiretm=expiretm,
            starttm=starttm,
            completedtm=completedtm,
            datastarttm=datastarttm,
            dataendtm=dataendtm,
            aclass=aclass,
            asset=asset,
        )

        export_status_response_200_result_item.additional_properties = d
        return export_status_response_200_result_item

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
