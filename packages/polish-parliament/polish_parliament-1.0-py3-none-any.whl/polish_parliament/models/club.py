from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Club")


@_attrs_define
class Club:
    """A club.

    Attributes:
        id (Union[Unset, str]): an id of the club
        name (Union[Unset, str]): Name of the club Example: KO.
        phone (Union[Unset, str]): Phone to the club Example: (22) 694-25-92.
        fax (Union[Unset, str]): FAX to the club Example: (22) 694-25-92.
        email (Union[Unset, str]): Email to the club Example: kp-ko@kluby.sejm.pl.
        members_count (Union[Unset, int]): Number of club members Example: 126.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    fax: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    members_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        phone = self.phone
        fax = self.fax
        email = self.email
        members_count = self.members_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if fax is not UNSET:
            field_dict["fax"] = fax
        if email is not UNSET:
            field_dict["email"] = email
        if members_count is not UNSET:
            field_dict["membersCount"] = members_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        fax = d.pop("fax", UNSET)

        email = d.pop("email", UNSET)

        members_count = d.pop("membersCount", UNSET)

        club = cls(
            id=id,
            name=name,
            phone=phone,
            fax=fax,
            email=email,
            members_count=members_count,
        )

        club.additional_properties = d
        return club

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
