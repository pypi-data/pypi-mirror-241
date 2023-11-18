import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ue_status import UEStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessHeader")


@_attrs_define
class ProcessHeader:
    """A legislative process

    Attributes:
        u_e (Union[Unset, UEStatus]):
        term (Union[Unset, int]): A Sejm term Example: 9.
        number (Union[Unset, str]): A number of the process Example: 40.
        title (Union[Unset, str]): A title of the process Example: Obywatelski projekt ustawy o ochronie własności w
            Rzeczypospolitej Polskiej przed roszczeniami dotyczącymi mienia bezdziedzicznego.
        description (Union[Unset, str]): A description of the process Example: projekt dotyczy zawieszenia na okres 6
            miesięcy 2020 r. funkcjonowania ustawy. Przepisy ustawy będą stosowane do przychodów ze sprzedaży detalicznej
            osiągniętych od 1 lipca 2020 r.
        ue (Union[Unset, UEStatus]):
        document_date (Union[Unset, datetime.date]): A date of document Example: 2019-11-28.
        process_start_date (Union[Unset, datetime.date]): A date of start process Example: 2019-11-28.
        change_date (Union[Unset, datetime.datetime]): A date of change process Example: 2020-01-02 15:00:52.
        document_type (Union[Unset, str]): A document type Example: projekt ustawy.
        comments (Union[Unset, str]): Comments Example: Obywatelski projekt ustawy został wniesiony w VIII kadencji
            Sejmu (druk nr 226). Na podstawie art. 4. ust. 3 ustawy o wykonywaniu inicjatywy ustawodawczej przez obywateli -
            projekt ustawy, w stosunku do którego postępowanie ustawodawcze nie zostało zakończone w trakcie kadencji Sejmu,
            w której został wniesiony, jest rozpatrywany przez Sejm następnej kadencji..
        web_generated_date (Union[Unset, datetime.datetime]): A date when a web page with a process was updated Example:
            2020-01-02 15:00:52.
    """

    u_e: Union[Unset, UEStatus] = UNSET
    term: Union[Unset, int] = UNSET
    number: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    ue: Union[Unset, UEStatus] = UNSET
    document_date: Union[Unset, datetime.date] = UNSET
    process_start_date: Union[Unset, datetime.date] = UNSET
    change_date: Union[Unset, datetime.datetime] = UNSET
    document_type: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    web_generated_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        u_e: Union[Unset, str] = UNSET
        if not isinstance(self.u_e, Unset):
            u_e = self.u_e.value

        term = self.term
        number = self.number
        title = self.title
        description = self.description
        ue: Union[Unset, str] = UNSET
        if not isinstance(self.ue, Unset):
            ue = self.ue.value

        document_date: Union[Unset, str] = UNSET
        if not isinstance(self.document_date, Unset):
            document_date = self.document_date.isoformat()

        process_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.process_start_date, Unset):
            process_start_date = self.process_start_date.isoformat()

        change_date: Union[Unset, str] = UNSET
        if not isinstance(self.change_date, Unset):
            change_date = self.change_date.isoformat()

        document_type = self.document_type
        comments = self.comments
        web_generated_date: Union[Unset, str] = UNSET
        if not isinstance(self.web_generated_date, Unset):
            web_generated_date = self.web_generated_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if u_e is not UNSET:
            field_dict["uE"] = u_e
        if term is not UNSET:
            field_dict["term"] = term
        if number is not UNSET:
            field_dict["number"] = number
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if ue is not UNSET:
            field_dict["ue"] = ue
        if document_date is not UNSET:
            field_dict["documentDate"] = document_date
        if process_start_date is not UNSET:
            field_dict["processStartDate"] = process_start_date
        if change_date is not UNSET:
            field_dict["changeDate"] = change_date
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if comments is not UNSET:
            field_dict["comments"] = comments
        if web_generated_date is not UNSET:
            field_dict["webGeneratedDate"] = web_generated_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _u_e = d.pop("uE", UNSET)
        u_e: Union[Unset, UEStatus]
        if isinstance(_u_e, Unset):
            u_e = UNSET
        else:
            u_e = UEStatus(_u_e)

        term = d.pop("term", UNSET)

        number = d.pop("number", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _ue = d.pop("ue", UNSET)
        ue: Union[Unset, UEStatus]
        if isinstance(_ue, Unset):
            ue = UNSET
        else:
            ue = UEStatus(_ue)

        _document_date = d.pop("documentDate", UNSET)
        document_date: Union[Unset, datetime.date]
        if isinstance(_document_date, Unset):
            document_date = UNSET
        else:
            document_date = isoparse(_document_date).date()

        _process_start_date = d.pop("processStartDate", UNSET)
        process_start_date: Union[Unset, datetime.date]
        if isinstance(_process_start_date, Unset):
            process_start_date = UNSET
        else:
            process_start_date = isoparse(_process_start_date).date()

        _change_date = d.pop("changeDate", UNSET)
        change_date: Union[Unset, datetime.datetime]
        if isinstance(_change_date, Unset):
            change_date = UNSET
        else:
            change_date = isoparse(_change_date)

        document_type = d.pop("documentType", UNSET)

        comments = d.pop("comments", UNSET)

        _web_generated_date = d.pop("webGeneratedDate", UNSET)
        web_generated_date: Union[Unset, datetime.datetime]
        if isinstance(_web_generated_date, Unset):
            web_generated_date = UNSET
        else:
            web_generated_date = isoparse(_web_generated_date)

        process_header = cls(
            u_e=u_e,
            term=term,
            number=number,
            title=title,
            description=description,
            ue=ue,
            document_date=document_date,
            process_start_date=process_start_date,
            change_date=change_date,
            document_type=document_type,
            comments=comments,
            web_generated_date=web_generated_date,
        )

        process_header.additional_properties = d
        return process_header

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
