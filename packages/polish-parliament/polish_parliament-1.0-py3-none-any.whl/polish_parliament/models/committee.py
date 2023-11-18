import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.comittee_type import ComitteeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.member import Member


T = TypeVar("T", bound="Committee")


@_attrs_define
class Committee:
    """A comittee.

    Attributes:
        code (Union[Unset, str]): Code of committee Example: ENM.
        name (Union[Unset, str]): Name of the committee Example: Komisja Edukacji, Nauki i Młodzieży.
        name_genitive (Union[Unset, str]): Name of the committee in genitive Example: Komisji Edukacji, Nauki i
            Młodzieży.
        type (Union[Unset, ComitteeType]):
        phone (Union[Unset, str]): Phone of the committee Example: (22) 694-12-99, 694-20-85.
        appointment_date (Union[Unset, datetime.date]): Date of appointment Example: 2019-11-13.
        composition_date (Union[Unset, datetime.date]): Date of composition Example: 2019-11-13.
        scope (Union[Unset, str]): Description of the committee Example: Do zakresu działania Komisji należą sprawy
            kształcenia i wychowania przedszkolnego, podstawowego, ogólnokształcącego, zawodowego, pomaturalnego i wyższego,
            ....
        members (Union[Unset, List['Member']]): a list of committee members (current or at the date of closing the
            committee)
    """

    code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    name_genitive: Union[Unset, str] = UNSET
    type: Union[Unset, ComitteeType] = UNSET
    phone: Union[Unset, str] = UNSET
    appointment_date: Union[Unset, datetime.date] = UNSET
    composition_date: Union[Unset, datetime.date] = UNSET
    scope: Union[Unset, str] = UNSET
    members: Union[Unset, List["Member"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        name = self.name
        name_genitive = self.name_genitive
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        phone = self.phone
        appointment_date: Union[Unset, str] = UNSET
        if not isinstance(self.appointment_date, Unset):
            appointment_date = self.appointment_date.isoformat()

        composition_date: Union[Unset, str] = UNSET
        if not isinstance(self.composition_date, Unset):
            composition_date = self.composition_date.isoformat()

        scope = self.scope
        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()

                members.append(members_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if name_genitive is not UNSET:
            field_dict["nameGenitive"] = name_genitive
        if type is not UNSET:
            field_dict["type"] = type
        if phone is not UNSET:
            field_dict["phone"] = phone
        if appointment_date is not UNSET:
            field_dict["appointmentDate"] = appointment_date
        if composition_date is not UNSET:
            field_dict["compositionDate"] = composition_date
        if scope is not UNSET:
            field_dict["scope"] = scope
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.member import Member

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        name_genitive = d.pop("nameGenitive", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ComitteeType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ComitteeType(_type)

        phone = d.pop("phone", UNSET)

        _appointment_date = d.pop("appointmentDate", UNSET)
        appointment_date: Union[Unset, datetime.date]
        if isinstance(_appointment_date, Unset):
            appointment_date = UNSET
        else:
            appointment_date = isoparse(_appointment_date).date()

        _composition_date = d.pop("compositionDate", UNSET)
        composition_date: Union[Unset, datetime.date]
        if isinstance(_composition_date, Unset):
            composition_date = UNSET
        else:
            composition_date = isoparse(_composition_date).date()

        scope = d.pop("scope", UNSET)

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = Member.from_dict(members_item_data)

            members.append(members_item)

        committee = cls(
            code=code,
            name=name,
            name_genitive=name_genitive,
            type=type,
            phone=phone,
            appointment_date=appointment_date,
            composition_date=composition_date,
            scope=scope,
            members=members,
        )

        committee.additional_properties = d
        return committee

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
