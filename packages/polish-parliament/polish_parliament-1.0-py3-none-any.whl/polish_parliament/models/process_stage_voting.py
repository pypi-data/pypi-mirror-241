import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_stage import ProcessStage
    from ..models.voting import Voting


T = TypeVar("T", bound="ProcessStageVoting")


@_attrs_define
class ProcessStageVoting:
    """voting on a Sejm sitting

    Attributes:
        stage_name (Union[Unset, str]): a name of a stage Example: I czytanie na posiedzeniu Sejmu.
        date (Union[Unset, datetime.date]): a stage date Example: 2019-11-28.
        children (Union[Unset, List['ProcessStage']]): child stages
        voting (Union[Unset, Voting]): a voting
    """

    stage_name: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    children: Union[Unset, List["ProcessStage"]] = UNSET
    voting: Union[Unset, "Voting"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stage_name = self.stage_name
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        children: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()

                children.append(children_item)

        voting: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.voting, Unset):
            voting = self.voting.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stage_name is not UNSET:
            field_dict["stageName"] = stage_name
        if date is not UNSET:
            field_dict["date"] = date
        if children is not UNSET:
            field_dict["children"] = children
        if voting is not UNSET:
            field_dict["voting"] = voting

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.process_stage import ProcessStage
        from ..models.voting import Voting

        d = src_dict.copy()
        stage_name = d.pop("stageName", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = ProcessStage.from_dict(children_item_data)

            children.append(children_item)

        _voting = d.pop("voting", UNSET)
        voting: Union[Unset, Voting]
        if isinstance(_voting, Unset):
            voting = UNSET
        else:
            voting = Voting.from_dict(_voting)

        process_stage_voting = cls(
            stage_name=stage_name,
            date=date,
            children=children,
            voting=voting,
        )

        process_stage_voting.additional_properties = d
        return process_stage_voting

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
