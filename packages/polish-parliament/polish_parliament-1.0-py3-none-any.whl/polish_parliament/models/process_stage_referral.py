import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.referral_type import ReferralType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_stage import ProcessStage


T = TypeVar("T", bound="ProcessStageReferral")


@_attrs_define
class ProcessStageReferral:
    """referral

    Attributes:
        stage_name (Union[Unset, str]): a name of a stage Example: I czytanie na posiedzeniu Sejmu.
        date (Union[Unset, datetime.date]): a stage date Example: 2019-11-28.
        children (Union[Unset, List['ProcessStage']]): child stages
        type (Union[Unset, ReferralType]):
        committee_code (Union[Unset, str]): a committee code or null for Sejm reading Example: ENM.
        report_date (Union[Unset, datetime.date]): recommended date of report Example: 2019-11-12.
        remarks (Union[Unset, str]): remarks
    """

    stage_name: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    children: Union[Unset, List["ProcessStage"]] = UNSET
    type: Union[Unset, ReferralType] = UNSET
    committee_code: Union[Unset, str] = UNSET
    report_date: Union[Unset, datetime.date] = UNSET
    remarks: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stage_name = self.stage_name
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        children: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()

                children.append(children_item)

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        committee_code = self.committee_code
        report_date: Union[Unset, str] = UNSET
        if not isinstance(self.report_date, Unset):
            report_date = self.report_date.isoformat()

        remarks = self.remarks

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stage_name is not UNSET:
            field_dict["stageName"] = stage_name
        if date is not UNSET:
            field_dict["date"] = date
        if children is not UNSET:
            field_dict["children"] = children
        if type is not UNSET:
            field_dict["type"] = type
        if committee_code is not UNSET:
            field_dict["committeeCode"] = committee_code
        if report_date is not UNSET:
            field_dict["reportDate"] = report_date
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.process_stage import ProcessStage

        d = src_dict.copy()
        stage_name = d.pop("stageName", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = ProcessStage.from_dict(children_item_data)

            children.append(children_item)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ReferralType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ReferralType(_type)

        committee_code = d.pop("committeeCode", UNSET)

        _report_date = d.pop("reportDate", UNSET)
        report_date: Union[Unset, datetime.date]
        if isinstance(_report_date, Unset):
            report_date = UNSET
        else:
            report_date = isoparse(_report_date).date()

        remarks = d.pop("remarks", UNSET)

        process_stage_referral = cls(
            stage_name=stage_name,
            date=date,
            children=children,
            type=type,
            committee_code=committee_code,
            report_date=report_date,
            remarks=remarks,
        )

        process_stage_referral.additional_properties = d
        return process_stage_referral

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
