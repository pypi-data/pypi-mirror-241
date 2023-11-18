import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_stage import ProcessStage


T = TypeVar("T", bound="ProcessStageOpinion")


@_attrs_define
class ProcessStageOpinion:
    """opinion

    Attributes:
        stage_name (Union[Unset, str]): a name of a stage Example: I czytanie na posiedzeniu Sejmu.
        date (Union[Unset, datetime.date]): a stage date Example: 2019-11-28.
        children (Union[Unset, List['ProcessStage']]): child stages
        organ (Union[Unset, str]): organ Example: Organizacja samorządowa.
        opinion_received (Union[Unset, datetime.date]): date when the opinion was received Example: 2019-11-12.
        to_commission (Union[Unset, datetime.date]): date when the opinion was sent to commission Example: Sejm.
    """

    stage_name: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    children: Union[Unset, List["ProcessStage"]] = UNSET
    organ: Union[Unset, str] = UNSET
    opinion_received: Union[Unset, datetime.date] = UNSET
    to_commission: Union[Unset, datetime.date] = UNSET
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

        organ = self.organ
        opinion_received: Union[Unset, str] = UNSET
        if not isinstance(self.opinion_received, Unset):
            opinion_received = self.opinion_received.isoformat()

        to_commission: Union[Unset, str] = UNSET
        if not isinstance(self.to_commission, Unset):
            to_commission = self.to_commission.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stage_name is not UNSET:
            field_dict["stageName"] = stage_name
        if date is not UNSET:
            field_dict["date"] = date
        if children is not UNSET:
            field_dict["children"] = children
        if organ is not UNSET:
            field_dict["organ"] = organ
        if opinion_received is not UNSET:
            field_dict["opinionReceived"] = opinion_received
        if to_commission is not UNSET:
            field_dict["toCommission"] = to_commission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.process_stage import ProcessStage

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

        organ = d.pop("organ", UNSET)

        _opinion_received = d.pop("opinionReceived", UNSET)
        opinion_received: Union[Unset, datetime.date]
        if isinstance(_opinion_received, Unset):
            opinion_received = UNSET
        else:
            opinion_received = isoparse(_opinion_received).date()

        _to_commission = d.pop("toCommission", UNSET)
        to_commission: Union[Unset, datetime.date]
        if isinstance(_to_commission, Unset):
            to_commission = UNSET
        else:
            to_commission = isoparse(_to_commission).date()

        process_stage_opinion = cls(
            stage_name=stage_name,
            date=date,
            children=children,
            organ=organ,
            opinion_received=opinion_received,
            to_commission=to_commission,
        )

        process_stage_opinion.additional_properties = d
        return process_stage_opinion

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
