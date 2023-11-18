import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.voting_kind import VotingKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voting_option import VotingOption


T = TypeVar("T", bound="Voting")


@_attrs_define
class Voting:
    """a voting

    Attributes:
        term (Union[Unset, int]): a Sejm term Example: 9.
        sitting (Union[Unset, int]): a Sejm sitting number Example: 62.
        sitting_day (Union[Unset, int]): a day of Sejm sitting Example: 1.
        number (Union[Unset, int]): a voting number Example: 43.
        date (Union[Unset, datetime.datetime]): a voting date and time Example: 2022-09-29 15:56:30.
        title (Union[Unset, str]): a voting title Example: Pkt. 27 Sprawozdanie Komisji o rządowym projekcie ustawy o
            zmianie ustawy - Prawo energetyczne oraz ustawy o odnawialnych źródłach energii (druki nr 2634, 2644 i 2644-A).
        topic (Union[Unset, str]): a voting topic Example: głosowanie nad całością projektu.
        description (Union[Unset, str]): description Example: a description of a voting.
        yes (Union[Unset, int]): number of 'yes' votes Example: 209.
        no (Union[Unset, int]): number of 'no' votes Example: 17.
        abstain (Union[Unset, int]): number of 'abstain' votes Example: 4.
        not_participating (Union[Unset, int]): number of people who did not vote Example: 1.
        pdf_link (Union[Unset, str]): a link to a pdf file with voting results
        kind (Union[Unset, VotingKind]):
        voting_options (Union[Unset, List['VotingOption']]): a list of options when voting on a list
    """

    term: Union[Unset, int] = UNSET
    sitting: Union[Unset, int] = UNSET
    sitting_day: Union[Unset, int] = UNSET
    number: Union[Unset, int] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    title: Union[Unset, str] = UNSET
    topic: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    yes: Union[Unset, int] = UNSET
    no: Union[Unset, int] = UNSET
    abstain: Union[Unset, int] = UNSET
    not_participating: Union[Unset, int] = UNSET
    pdf_link: Union[Unset, str] = UNSET
    kind: Union[Unset, VotingKind] = UNSET
    voting_options: Union[Unset, List["VotingOption"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        term = self.term
        sitting = self.sitting
        sitting_day = self.sitting_day
        number = self.number
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        title = self.title
        topic = self.topic
        description = self.description
        yes = self.yes
        no = self.no
        abstain = self.abstain
        not_participating = self.not_participating
        pdf_link = self.pdf_link
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        voting_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.voting_options, Unset):
            voting_options = []
            for voting_options_item_data in self.voting_options:
                voting_options_item = voting_options_item_data.to_dict()

                voting_options.append(voting_options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if sitting is not UNSET:
            field_dict["sitting"] = sitting
        if sitting_day is not UNSET:
            field_dict["sittingDay"] = sitting_day
        if number is not UNSET:
            field_dict["number"] = number
        if date is not UNSET:
            field_dict["date"] = date
        if title is not UNSET:
            field_dict["title"] = title
        if topic is not UNSET:
            field_dict["topic"] = topic
        if description is not UNSET:
            field_dict["description"] = description
        if yes is not UNSET:
            field_dict["yes"] = yes
        if no is not UNSET:
            field_dict["no"] = no
        if abstain is not UNSET:
            field_dict["abstain"] = abstain
        if not_participating is not UNSET:
            field_dict["notParticipating"] = not_participating
        if pdf_link is not UNSET:
            field_dict["pdfLink"] = pdf_link
        if kind is not UNSET:
            field_dict["kind"] = kind
        if voting_options is not UNSET:
            field_dict["votingOptions"] = voting_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.voting_option import VotingOption

        d = src_dict.copy()
        term = d.pop("term", UNSET)

        sitting = d.pop("sitting", UNSET)

        sitting_day = d.pop("sittingDay", UNSET)

        number = d.pop("number", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        title = d.pop("title", UNSET)

        topic = d.pop("topic", UNSET)

        description = d.pop("description", UNSET)

        yes = d.pop("yes", UNSET)

        no = d.pop("no", UNSET)

        abstain = d.pop("abstain", UNSET)

        not_participating = d.pop("notParticipating", UNSET)

        pdf_link = d.pop("pdfLink", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, VotingKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = VotingKind(_kind)

        voting_options = []
        _voting_options = d.pop("votingOptions", UNSET)
        for voting_options_item_data in _voting_options or []:
            voting_options_item = VotingOption.from_dict(voting_options_item_data)

            voting_options.append(voting_options_item)

        voting = cls(
            term=term,
            sitting=sitting,
            sitting_day=sitting_day,
            number=number,
            date=date,
            title=title,
            topic=topic,
            description=description,
            yes=yes,
            no=no,
            abstain=abstain,
            not_participating=not_participating,
            pdf_link=pdf_link,
            kind=kind,
            voting_options=voting_options,
        )

        voting.additional_properties = d
        return voting

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
