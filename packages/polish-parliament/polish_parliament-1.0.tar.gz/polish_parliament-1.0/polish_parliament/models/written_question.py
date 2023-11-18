import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reply import Reply


T = TypeVar("T", bound="WrittenQuestion")


@_attrs_define
class WrittenQuestion:
    """A written question (pl: zapytanie).

    Attributes:
        term (Union[Unset, int]): A Sejm term when the document was submitted Example: 9.
        num (Union[Unset, int]): A document number Example: 14710.
        title (Union[Unset, str]): A title of the case Example: Interpelacja w sprawie trudnej sytuacji osób
            niepełnosprawnych z uwagi na kwarantannę nakładaną na ich opiekunów.
        receipt_date (Union[Unset, datetime.date]): A date when the case was received Example: 2020-11-16.
        last_modified (Union[Unset, datetime.datetime]): A date of last modification of a document Example: 2022-09-07
            15:01:42.
        links (Union[Unset, List[Any]]): Links to HTML pages with a description or a content (body)
        from_ (Union[Unset, List[str]]): A list of IDs of MPs who submitted the question Example: 101.
        to (Union[Unset, List[str]]): A list of ministries to whom the question was sent Example: ['minister rodziny i
            polityki społecznej', 'minister zdrowia'].
        sent_date (Union[Unset, datetime.date]): A date when the interpellation was sent to recipients Example:
            2021-01-20.
        replies (Union[Unset, List['Reply']]): A list of replies
    """

    term: Union[Unset, int] = UNSET
    num: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    receipt_date: Union[Unset, datetime.date] = UNSET
    last_modified: Union[Unset, datetime.datetime] = UNSET
    links: Union[Unset, List[Any]] = UNSET
    from_: Union[Unset, List[str]] = UNSET
    to: Union[Unset, List[str]] = UNSET
    sent_date: Union[Unset, datetime.date] = UNSET
    replies: Union[Unset, List["Reply"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        term = self.term
        num = self.num
        title = self.title
        receipt_date: Union[Unset, str] = UNSET
        if not isinstance(self.receipt_date, Unset):
            receipt_date = self.receipt_date.isoformat()

        last_modified: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        links: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links

        from_: Union[Unset, List[str]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_

        to: Union[Unset, List[str]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to

        sent_date: Union[Unset, str] = UNSET
        if not isinstance(self.sent_date, Unset):
            sent_date = self.sent_date.isoformat()

        replies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.replies, Unset):
            replies = []
            for replies_item_data in self.replies:
                replies_item = replies_item_data.to_dict()

                replies.append(replies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if num is not UNSET:
            field_dict["num"] = num
        if title is not UNSET:
            field_dict["title"] = title
        if receipt_date is not UNSET:
            field_dict["receiptDate"] = receipt_date
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if links is not UNSET:
            field_dict["links"] = links
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if sent_date is not UNSET:
            field_dict["sentDate"] = sent_date
        if replies is not UNSET:
            field_dict["replies"] = replies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reply import Reply

        d = src_dict.copy()
        term = d.pop("term", UNSET)

        num = d.pop("num", UNSET)

        title = d.pop("title", UNSET)

        _receipt_date = d.pop("receiptDate", UNSET)
        receipt_date: Union[Unset, datetime.date]
        if isinstance(_receipt_date, Unset):
            receipt_date = UNSET
        else:
            receipt_date = isoparse(_receipt_date).date()

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: Union[Unset, datetime.datetime]
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        links = cast(List[Any], d.pop("links", UNSET))

        from_ = cast(List[str], d.pop("from", UNSET))

        to = cast(List[str], d.pop("to", UNSET))

        _sent_date = d.pop("sentDate", UNSET)
        sent_date: Union[Unset, datetime.date]
        if isinstance(_sent_date, Unset):
            sent_date = UNSET
        else:
            sent_date = isoparse(_sent_date).date()

        replies = []
        _replies = d.pop("replies", UNSET)
        for replies_item_data in _replies or []:
            replies_item = Reply.from_dict(replies_item_data)

            replies.append(replies_item)

        written_question = cls(
            term=term,
            num=num,
            title=title,
            receipt_date=receipt_date,
            last_modified=last_modified,
            links=links,
            from_=from_,
            to=to,
            sent_date=sent_date,
            replies=replies,
        )

        written_question.additional_properties = d
        return written_question

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
