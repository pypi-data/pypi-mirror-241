import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessDocument")


@_attrs_define
class ProcessDocument:
    """A document in the legislative process.

    Attributes:
        number (Union[Unset, str]): a print number Example: 13-A.
        registered_date (Union[Unset, datetime.date]): a date when a document was registered Example: 2019-11-28.
    """

    number: Union[Unset, str] = UNSET
    registered_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        registered_date: Union[Unset, str] = UNSET
        if not isinstance(self.registered_date, Unset):
            registered_date = self.registered_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if registered_date is not UNSET:
            field_dict["registeredDate"] = registered_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number", UNSET)

        _registered_date = d.pop("registeredDate", UNSET)
        registered_date: Union[Unset, datetime.date]
        if isinstance(_registered_date, Unset):
            registered_date = UNSET
        else:
            registered_date = isoparse(_registered_date).date()

        process_document = cls(
            number=number,
            registered_date=registered_date,
        )

        process_document.additional_properties = d
        return process_document

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
