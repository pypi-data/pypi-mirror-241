import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.print_info import PrintInfo


T = TypeVar("T", bound="Term")


@_attrs_define
class Term:
    """information about a term of the Sejm

    Attributes:
        num (Union[Unset, int]): Number of term of the Sejm Example: 9.
        from_ (Union[Unset, datetime.date]): Date start of term Example: 2019-11-12.
        to (Union[Unset, datetime.date]): Date end of term Example: 2019-11-12.
        current (Union[Unset, bool]): Current of term Example: True.
        prints (Union[Unset, PrintInfo]): info about prints
    """

    num: Union[Unset, int] = UNSET
    from_: Union[Unset, datetime.date] = UNSET
    to: Union[Unset, datetime.date] = UNSET
    current: Union[Unset, bool] = UNSET
    prints: Union[Unset, "PrintInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num = self.num
        from_: Union[Unset, str] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: Union[Unset, str] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        current = self.current
        prints: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prints, Unset):
            prints = self.prints.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num is not UNSET:
            field_dict["num"] = num
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if current is not UNSET:
            field_dict["current"] = current
        if prints is not UNSET:
            field_dict["prints"] = prints

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.print_info import PrintInfo

        d = src_dict.copy()
        num = d.pop("num", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, datetime.date]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_).date()

        _to = d.pop("to", UNSET)
        to: Union[Unset, datetime.date]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to).date()

        current = d.pop("current", UNSET)

        _prints = d.pop("prints", UNSET)
        prints: Union[Unset, PrintInfo]
        if isinstance(_prints, Unset):
            prints = UNSET
        else:
            prints = PrintInfo.from_dict(_prints)

        term = cls(
            num=num,
            from_=from_,
            to=to,
            current=current,
            prints=prints,
        )

        term.additional_properties = d
        return term

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
