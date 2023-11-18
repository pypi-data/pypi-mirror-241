import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Print")


@_attrs_define
class Print:
    """A print

    Attributes:
        term (Union[Unset, int]): a Sejm term Example: 9.
        number (Union[Unset, str]): a number of a print in the specified Sejm term Example: 19, 1006-A.
        number_associated (Union[Unset, List[str]]): numbers of prints that this print is associated with Example: 609.
        title (Union[Unset, str]): a title of a print Example: Opinia Komisji Sprawiedliwości i Praw Człowieka dotycząca
            wniosków w sprawie wyboru na stanowiska sędziów Trybunału Konstytucyjnego..
        document_date (Union[Unset, datetime.date]): a date of a print Example: 2019-11-20.
        delivery_date (Union[Unset, datetime.date]): a date of delivery of a print Example: 2019-11-20.
        process_print (Union[Unset, List[str]]): a list of prints that started a legislative process that this print is
            connected to Example: ['16', '17'].
        change_date (Union[Unset, datetime.datetime]): a date of of last change to the print Example: 2020-10-02
            12:49:35.
        attachments (Union[Unset, List[str]]): a list of attachments added to the print
        additional_prints (Union[Unset, List['Print']]): a list of additional prints added to the print
    """

    term: Union[Unset, int] = UNSET
    number: Union[Unset, str] = UNSET
    number_associated: Union[Unset, List[str]] = UNSET
    title: Union[Unset, str] = UNSET
    document_date: Union[Unset, datetime.date] = UNSET
    delivery_date: Union[Unset, datetime.date] = UNSET
    process_print: Union[Unset, List[str]] = UNSET
    change_date: Union[Unset, datetime.datetime] = UNSET
    attachments: Union[Unset, List[str]] = UNSET
    additional_prints: Union[Unset, List["Print"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        term = self.term
        number = self.number
        number_associated: Union[Unset, List[str]] = UNSET
        if not isinstance(self.number_associated, Unset):
            number_associated = self.number_associated

        title = self.title
        document_date: Union[Unset, str] = UNSET
        if not isinstance(self.document_date, Unset):
            document_date = self.document_date.isoformat()

        delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_date, Unset):
            delivery_date = self.delivery_date.isoformat()

        process_print: Union[Unset, List[str]] = UNSET
        if not isinstance(self.process_print, Unset):
            process_print = self.process_print

        change_date: Union[Unset, str] = UNSET
        if not isinstance(self.change_date, Unset):
            change_date = self.change_date.isoformat()

        attachments: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments

        additional_prints: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_prints, Unset):
            additional_prints = []
            for additional_prints_item_data in self.additional_prints:
                additional_prints_item = additional_prints_item_data.to_dict()

                additional_prints.append(additional_prints_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if number is not UNSET:
            field_dict["number"] = number
        if number_associated is not UNSET:
            field_dict["numberAssociated"] = number_associated
        if title is not UNSET:
            field_dict["title"] = title
        if document_date is not UNSET:
            field_dict["documentDate"] = document_date
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if process_print is not UNSET:
            field_dict["processPrint"] = process_print
        if change_date is not UNSET:
            field_dict["changeDate"] = change_date
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if additional_prints is not UNSET:
            field_dict["additionalPrints"] = additional_prints

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        term = d.pop("term", UNSET)

        number = d.pop("number", UNSET)

        number_associated = cast(List[str], d.pop("numberAssociated", UNSET))

        title = d.pop("title", UNSET)

        _document_date = d.pop("documentDate", UNSET)
        document_date: Union[Unset, datetime.date]
        if isinstance(_document_date, Unset):
            document_date = UNSET
        else:
            document_date = isoparse(_document_date).date()

        _delivery_date = d.pop("deliveryDate", UNSET)
        delivery_date: Union[Unset, datetime.date]
        if isinstance(_delivery_date, Unset):
            delivery_date = UNSET
        else:
            delivery_date = isoparse(_delivery_date).date()

        process_print = cast(List[str], d.pop("processPrint", UNSET))

        _change_date = d.pop("changeDate", UNSET)
        change_date: Union[Unset, datetime.datetime]
        if isinstance(_change_date, Unset):
            change_date = UNSET
        else:
            change_date = isoparse(_change_date)

        attachments = cast(List[str], d.pop("attachments", UNSET))

        additional_prints = []
        _additional_prints = d.pop("additionalPrints", UNSET)
        for additional_prints_item_data in _additional_prints or []:
            additional_prints_item = Print.from_dict(additional_prints_item_data)

            additional_prints.append(additional_prints_item)

        print_ = cls(
            term=term,
            number=number,
            number_associated=number_associated,
            title=title,
            document_date=document_date,
            delivery_date=delivery_date,
            process_print=process_print,
            change_date=change_date,
            attachments=attachments,
            additional_prints=additional_prints,
        )

        print_.additional_properties = d
        return print_

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
