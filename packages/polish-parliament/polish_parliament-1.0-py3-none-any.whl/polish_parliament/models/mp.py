import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MP")


@_attrs_define
class MP:
    """A MP.

    Attributes:
        id (Union[Unset, int]): A number of the identity card of the MP. Example: 1.
        first_last_name (Union[Unset, str]): The first and last name of the MP. Example: Andrzej Adamczyk.
        last_first_name (Union[Unset, str]): The last and first name of the MP. Example: Adamczyk Andrzej.
        first_name (Union[Unset, str]): The first name of the MP. Example: Andrzej.
        second_name (Union[Unset, str]): The second name of the MP. Example: Mieczysław.
        last_name (Union[Unset, str]): The last name of the MP. Example: Adamczyk.
        email (Union[Unset, str]): The email of the MP. Example: Andrzej.Adamczyk@sejm.pl.
        active (Union[Unset, bool]): Is the MP active? Example: True.
        inactive_cause (Union[Unset, str]): The cause of inactivity Example: Zrzeczenie.
        waiver_desc (Union[Unset, str]): ?
        district_num (Union[Unset, int]): A district id where MP was elected Example: 13.
        district_name (Union[Unset, str]): A district name where MP was elected Example: Kraków.
        voivodeship (Union[Unset, str]): A voivodeship where MP was elected Example: małopolskie.
        club (Union[Unset, str]): A club to where MP is belonging Example: PiS.
        birth_date (Union[Unset, datetime.date]): a date of birth Example: 1959-01-04.
        birth_location (Union[Unset, str]): a place of birth Example: Krzeszowice.
        profession (Union[Unset, str]): a profession Example: parlamentarzysta.
        education_level (Union[Unset, str]): an education level Example: wyższe.
        number_of_votes (Union[Unset, int]): a number of votes Example: 29686.
    """

    id: Union[Unset, int] = UNSET
    first_last_name: Union[Unset, str] = UNSET
    last_first_name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    second_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    inactive_cause: Union[Unset, str] = UNSET
    waiver_desc: Union[Unset, str] = UNSET
    district_num: Union[Unset, int] = UNSET
    district_name: Union[Unset, str] = UNSET
    voivodeship: Union[Unset, str] = UNSET
    club: Union[Unset, str] = UNSET
    birth_date: Union[Unset, datetime.date] = UNSET
    birth_location: Union[Unset, str] = UNSET
    profession: Union[Unset, str] = UNSET
    education_level: Union[Unset, str] = UNSET
    number_of_votes: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        first_last_name = self.first_last_name
        last_first_name = self.last_first_name
        first_name = self.first_name
        second_name = self.second_name
        last_name = self.last_name
        email = self.email
        active = self.active
        inactive_cause = self.inactive_cause
        waiver_desc = self.waiver_desc
        district_num = self.district_num
        district_name = self.district_name
        voivodeship = self.voivodeship
        club = self.club
        birth_date: Union[Unset, str] = UNSET
        if not isinstance(self.birth_date, Unset):
            birth_date = self.birth_date.isoformat()

        birth_location = self.birth_location
        profession = self.profession
        education_level = self.education_level
        number_of_votes = self.number_of_votes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if first_last_name is not UNSET:
            field_dict["firstLastName"] = first_last_name
        if last_first_name is not UNSET:
            field_dict["lastFirstName"] = last_first_name
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if second_name is not UNSET:
            field_dict["secondName"] = second_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if active is not UNSET:
            field_dict["active"] = active
        if inactive_cause is not UNSET:
            field_dict["inactiveCause"] = inactive_cause
        if waiver_desc is not UNSET:
            field_dict["waiverDesc"] = waiver_desc
        if district_num is not UNSET:
            field_dict["districtNum"] = district_num
        if district_name is not UNSET:
            field_dict["districtName"] = district_name
        if voivodeship is not UNSET:
            field_dict["voivodeship"] = voivodeship
        if club is not UNSET:
            field_dict["club"] = club
        if birth_date is not UNSET:
            field_dict["birthDate"] = birth_date
        if birth_location is not UNSET:
            field_dict["birthLocation"] = birth_location
        if profession is not UNSET:
            field_dict["profession"] = profession
        if education_level is not UNSET:
            field_dict["educationLevel"] = education_level
        if number_of_votes is not UNSET:
            field_dict["numberOfVotes"] = number_of_votes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        first_last_name = d.pop("firstLastName", UNSET)

        last_first_name = d.pop("lastFirstName", UNSET)

        first_name = d.pop("firstName", UNSET)

        second_name = d.pop("secondName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        active = d.pop("active", UNSET)

        inactive_cause = d.pop("inactiveCause", UNSET)

        waiver_desc = d.pop("waiverDesc", UNSET)

        district_num = d.pop("districtNum", UNSET)

        district_name = d.pop("districtName", UNSET)

        voivodeship = d.pop("voivodeship", UNSET)

        club = d.pop("club", UNSET)

        _birth_date = d.pop("birthDate", UNSET)
        birth_date: Union[Unset, datetime.date]
        if isinstance(_birth_date, Unset):
            birth_date = UNSET
        else:
            birth_date = isoparse(_birth_date).date()

        birth_location = d.pop("birthLocation", UNSET)

        profession = d.pop("profession", UNSET)

        education_level = d.pop("educationLevel", UNSET)

        number_of_votes = d.pop("numberOfVotes", UNSET)

        mp = cls(
            id=id,
            first_last_name=first_last_name,
            last_first_name=last_first_name,
            first_name=first_name,
            second_name=second_name,
            last_name=last_name,
            email=email,
            active=active,
            inactive_cause=inactive_cause,
            waiver_desc=waiver_desc,
            district_num=district_num,
            district_name=district_name,
            voivodeship=voivodeship,
            club=club,
            birth_date=birth_date,
            birth_location=birth_location,
            profession=profession,
            education_level=education_level,
            number_of_votes=number_of_votes,
        )

        mp.additional_properties = d
        return mp

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
