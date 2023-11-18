import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Member")


@_attrs_define
class Member:
    """A member of a committee or a parliamentary team.

    Attributes:
        id (Union[Unset, int]): A number of the identity card of the MP.
        last_first_name (Union[Unset, str]): The last and first name of the MP.
        function (Union[Unset, str]): A function in the committee.
        mandate_expired (Union[Unset, datetime.date]): A function in the committee. Example: 2022-03-10.
        club (Union[Unset, str]): A club to where MP is belonging
    """

    id: Union[Unset, int] = UNSET
    last_first_name: Union[Unset, str] = UNSET
    function: Union[Unset, str] = UNSET
    mandate_expired: Union[Unset, datetime.date] = UNSET
    club: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        last_first_name = self.last_first_name
        function = self.function
        mandate_expired: Union[Unset, str] = UNSET
        if not isinstance(self.mandate_expired, Unset):
            mandate_expired = self.mandate_expired.isoformat()

        club = self.club

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if last_first_name is not UNSET:
            field_dict["lastFirstName"] = last_first_name
        if function is not UNSET:
            field_dict["function"] = function
        if mandate_expired is not UNSET:
            field_dict["mandateExpired"] = mandate_expired
        if club is not UNSET:
            field_dict["club"] = club

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        last_first_name = d.pop("lastFirstName", UNSET)

        function = d.pop("function", UNSET)

        _mandate_expired = d.pop("mandateExpired", UNSET)
        mandate_expired: Union[Unset, datetime.date]
        if isinstance(_mandate_expired, Unset):
            mandate_expired = UNSET
        else:
            mandate_expired = isoparse(_mandate_expired).date()

        club = d.pop("club", UNSET)

        member = cls(
            id=id,
            last_first_name=last_first_name,
            function=function,
            mandate_expired=mandate_expired,
            club=club,
        )

        member.additional_properties = d
        return member

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
