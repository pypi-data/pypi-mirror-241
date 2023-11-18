from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VotingOption")


@_attrs_define
class VotingOption:
    """voting option when voting on a list

    Attributes:
        option (Union[Unset, str]): an option Example: STAROŃ LIDIA, INFORMACJA NR 1.
        description (Union[Unset, str]): an optional description Example: w sprawie realizacji rządowego "Programu
            budowy 100 obwodnic na lata 2020-2030".
        votes (Union[Unset, int]): number of votes for this option Example: 213.
    """

    option: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    votes: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        option = self.option
        description = self.description
        votes = self.votes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if option is not UNSET:
            field_dict["option"] = option
        if description is not UNSET:
            field_dict["description"] = description
        if votes is not UNSET:
            field_dict["votes"] = votes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        option = d.pop("option", UNSET)

        description = d.pop("description", UNSET)

        votes = d.pop("votes", UNSET)

        voting_option = cls(
            option=option,
            description=description,
            votes=votes,
        )

        voting_option.additional_properties = d
        return voting_option

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
