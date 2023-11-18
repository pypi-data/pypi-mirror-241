import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Proceeding")


@_attrs_define
class Proceeding:
    """A proceeding.

    Attributes:
        title (Union[Unset, str]): a title of the proceeding Example: 1. Posiedzenie Sejmu RP w dniach 12, 13, 19 i 21
            listopada 2019 r..
        dates (Union[Unset, List[datetime.date]]): a dates of the proceeding
        number (Union[Unset, int]): a proceeding number Example: 1.
    """

    title: Union[Unset, str] = UNSET
    dates: Union[Unset, List[datetime.date]] = UNSET
    number: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        dates: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = []
            for dates_item_data in self.dates:
                dates_item = dates_item_data.isoformat()
                dates.append(dates_item)

        number = self.number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if dates is not UNSET:
            field_dict["dates"] = dates
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        dates = []
        _dates = d.pop("dates", UNSET)
        for dates_item_data in _dates or []:
            dates_item = isoparse(dates_item_data).date()

            dates.append(dates_item)

        number = d.pop("number", UNSET)

        proceeding = cls(
            title=title,
            dates=dates,
            number=number,
        )

        proceeding.additional_properties = d
        return proceeding

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
