import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ue_status import UEStatus
from ..models.urgency_status import UrgencyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_document import ProcessDocument
    from ..models.process_stage import ProcessStage


T = TypeVar("T", bound="ProcessDetails")


@_attrs_define
class ProcessDetails:
    """A details of legislative process

    Attributes:
        term (Union[Unset, int]): a Sejm term Example: 9.
        number (Union[Unset, str]): a number of a print in the specified Sejm term Example: 19.
        title (Union[Unset, str]): a title of a process Example: Rządowy projekt ustawy o zmianie ustawy o transporcie
            kolejowym.
        description (Union[Unset, str]): a description of a process Example: projekt ustawy dotyczy utworzenia nowego
            uniwersytetu medycznego.
        u_e (Union[Unset, UEStatus]):
        document_date (Union[Unset, datetime.date]): a date of a print Example: 2019-11-19.
        change_date (Union[Unset, datetime.datetime]): a date of last change to the process Example: 2019-11-21
            10:01:37.
        web_generated_date (Union[Unset, datetime.datetime]): A date when a web page with a process was updated Example:
            2020-01-02 15:00:52.
        process_start_date (Union[Unset, datetime.date]): a date of the start of the process Example: 2019-11-19.
        document_type (Union[Unset, str]): a type of a document Example: projekt ustawy.
        comments (Union[Unset, str]): comments Example: Obywatelski projekt ustawy został wniesiony w VIII kadencji
            Sejmu (druk nr 226). Na podstawie art. 4. ust. 3 ustawy o wykonywaniu inicjatywy ustawodawczej przez obywateli -
            projekt ustawy, w stosunku do którego postępowanie ustawodawcze nie zostało zakończone w trakcie kadencji Sejmu,
            w której został wniesiony, jest rozpatrywany przez Sejm następnej kadencji..
        other_documents (Union[Unset, List['ProcessDocument']]): other prints, corrections
        rcl_num (Union[Unset, str]): number from goverment part of the process (from RCL website) Example:
            RM-0610-84-21.
        urgency_status (Union[Unset, UrgencyStatus]):
        urgency_withdraw_date (Union[Unset, datetime.date]): date when urgency clause was withdrawn Example: 2022-03-10.
        legislative_committee (Union[Unset, bool]): indicates that for work on this project a members of Legislative
            Committee has been assigned
        principle_of_subsidiarity (Union[Unset, bool]): indicates that the project is inconsistent with the principle of
            subsidiarity
        stages (Union[Unset, List['ProcessStage']]): stages of the process
        prints_considered_jointly (Union[Unset, List[str]]): prints considered jointly
    """

    term: Union[Unset, int] = UNSET
    number: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    u_e: Union[Unset, UEStatus] = UNSET
    document_date: Union[Unset, datetime.date] = UNSET
    change_date: Union[Unset, datetime.datetime] = UNSET
    web_generated_date: Union[Unset, datetime.datetime] = UNSET
    process_start_date: Union[Unset, datetime.date] = UNSET
    document_type: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    other_documents: Union[Unset, List["ProcessDocument"]] = UNSET
    rcl_num: Union[Unset, str] = UNSET
    urgency_status: Union[Unset, UrgencyStatus] = UNSET
    urgency_withdraw_date: Union[Unset, datetime.date] = UNSET
    legislative_committee: Union[Unset, bool] = UNSET
    principle_of_subsidiarity: Union[Unset, bool] = UNSET
    stages: Union[Unset, List["ProcessStage"]] = UNSET
    prints_considered_jointly: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        term = self.term
        number = self.number
        title = self.title
        description = self.description
        u_e: Union[Unset, str] = UNSET
        if not isinstance(self.u_e, Unset):
            u_e = self.u_e.value

        document_date: Union[Unset, str] = UNSET
        if not isinstance(self.document_date, Unset):
            document_date = self.document_date.isoformat()

        change_date: Union[Unset, str] = UNSET
        if not isinstance(self.change_date, Unset):
            change_date = self.change_date.isoformat()

        web_generated_date: Union[Unset, str] = UNSET
        if not isinstance(self.web_generated_date, Unset):
            web_generated_date = self.web_generated_date.isoformat()

        process_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.process_start_date, Unset):
            process_start_date = self.process_start_date.isoformat()

        document_type = self.document_type
        comments = self.comments
        other_documents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.other_documents, Unset):
            other_documents = []
            for other_documents_item_data in self.other_documents:
                other_documents_item = other_documents_item_data.to_dict()

                other_documents.append(other_documents_item)

        rcl_num = self.rcl_num
        urgency_status: Union[Unset, str] = UNSET
        if not isinstance(self.urgency_status, Unset):
            urgency_status = self.urgency_status.value

        urgency_withdraw_date: Union[Unset, str] = UNSET
        if not isinstance(self.urgency_withdraw_date, Unset):
            urgency_withdraw_date = self.urgency_withdraw_date.isoformat()

        legislative_committee = self.legislative_committee
        principle_of_subsidiarity = self.principle_of_subsidiarity
        stages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()

                stages.append(stages_item)

        prints_considered_jointly: Union[Unset, List[str]] = UNSET
        if not isinstance(self.prints_considered_jointly, Unset):
            prints_considered_jointly = self.prints_considered_jointly

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if number is not UNSET:
            field_dict["number"] = number
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if u_e is not UNSET:
            field_dict["uE"] = u_e
        if document_date is not UNSET:
            field_dict["documentDate"] = document_date
        if change_date is not UNSET:
            field_dict["changeDate"] = change_date
        if web_generated_date is not UNSET:
            field_dict["webGeneratedDate"] = web_generated_date
        if process_start_date is not UNSET:
            field_dict["processStartDate"] = process_start_date
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if comments is not UNSET:
            field_dict["comments"] = comments
        if other_documents is not UNSET:
            field_dict["otherDocuments"] = other_documents
        if rcl_num is not UNSET:
            field_dict["rclNum"] = rcl_num
        if urgency_status is not UNSET:
            field_dict["urgencyStatus"] = urgency_status
        if urgency_withdraw_date is not UNSET:
            field_dict["urgencyWithdrawDate"] = urgency_withdraw_date
        if legislative_committee is not UNSET:
            field_dict["legislativeCommittee"] = legislative_committee
        if principle_of_subsidiarity is not UNSET:
            field_dict["principleOfSubsidiarity"] = principle_of_subsidiarity
        if stages is not UNSET:
            field_dict["stages"] = stages
        if prints_considered_jointly is not UNSET:
            field_dict["printsConsideredJointly"] = prints_considered_jointly

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.process_document import ProcessDocument
        from ..models.process_stage import ProcessStage

        d = src_dict.copy()
        term = d.pop("term", UNSET)

        number = d.pop("number", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _u_e = d.pop("uE", UNSET)
        u_e: Union[Unset, UEStatus]
        if isinstance(_u_e, Unset):
            u_e = UNSET
        else:
            u_e = UEStatus(_u_e)

        _document_date = d.pop("documentDate", UNSET)
        document_date: Union[Unset, datetime.date]
        if isinstance(_document_date, Unset):
            document_date = UNSET
        else:
            document_date = isoparse(_document_date).date()

        _change_date = d.pop("changeDate", UNSET)
        change_date: Union[Unset, datetime.datetime]
        if isinstance(_change_date, Unset):
            change_date = UNSET
        else:
            change_date = isoparse(_change_date)

        _web_generated_date = d.pop("webGeneratedDate", UNSET)
        web_generated_date: Union[Unset, datetime.datetime]
        if isinstance(_web_generated_date, Unset):
            web_generated_date = UNSET
        else:
            web_generated_date = isoparse(_web_generated_date)

        _process_start_date = d.pop("processStartDate", UNSET)
        process_start_date: Union[Unset, datetime.date]
        if isinstance(_process_start_date, Unset):
            process_start_date = UNSET
        else:
            process_start_date = isoparse(_process_start_date).date()

        document_type = d.pop("documentType", UNSET)

        comments = d.pop("comments", UNSET)

        other_documents = []
        _other_documents = d.pop("otherDocuments", UNSET)
        for other_documents_item_data in _other_documents or []:
            other_documents_item = ProcessDocument.from_dict(other_documents_item_data)

            other_documents.append(other_documents_item)

        rcl_num = d.pop("rclNum", UNSET)

        _urgency_status = d.pop("urgencyStatus", UNSET)
        urgency_status: Union[Unset, UrgencyStatus]
        if isinstance(_urgency_status, Unset):
            urgency_status = UNSET
        else:
            urgency_status = UrgencyStatus(_urgency_status)

        _urgency_withdraw_date = d.pop("urgencyWithdrawDate", UNSET)
        urgency_withdraw_date: Union[Unset, datetime.date]
        if isinstance(_urgency_withdraw_date, Unset):
            urgency_withdraw_date = UNSET
        else:
            urgency_withdraw_date = isoparse(_urgency_withdraw_date).date()

        legislative_committee = d.pop("legislativeCommittee", UNSET)

        principle_of_subsidiarity = d.pop("principleOfSubsidiarity", UNSET)

        stages = []
        _stages = d.pop("stages", UNSET)
        for stages_item_data in _stages or []:
            stages_item = ProcessStage.from_dict(stages_item_data)

            stages.append(stages_item)

        prints_considered_jointly = cast(List[str], d.pop("printsConsideredJointly", UNSET))

        process_details = cls(
            term=term,
            number=number,
            title=title,
            description=description,
            u_e=u_e,
            document_date=document_date,
            change_date=change_date,
            web_generated_date=web_generated_date,
            process_start_date=process_start_date,
            document_type=document_type,
            comments=comments,
            other_documents=other_documents,
            rcl_num=rcl_num,
            urgency_status=urgency_status,
            urgency_withdraw_date=urgency_withdraw_date,
            legislative_committee=legislative_committee,
            principle_of_subsidiarity=principle_of_subsidiarity,
            stages=stages,
            prints_considered_jointly=prints_considered_jointly,
        )

        process_details.additional_properties = d
        return process_details

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
