import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment


T = TypeVar("T", bound="Reply")


@_attrs_define
class Reply:
    """reply to an interpellation or question

    Attributes:
        key (Union[Unset, str]): a reply identifier Example: BJWJSS.
        receipt_date (Union[Unset, datetime.date]): A date when the reply was received Example: 2021-01-29.
        last_modified (Union[Unset, datetime.datetime]): A date of last modification of a document Example: 2022-09-07
            15:01:42.
        from_ (Union[Unset, str]): A name of an author Example: Sekretarz stanu Waldemar Kraska.
        links (Union[Unset, List[Any]]): Links to HTML page with a description or a content (body)
        only_attachment (Union[Unset, bool]): Flag indicating that this reply contains only an attachment (without HTML
            body)
        attachments (Union[Unset, List['Attachment']]): Attachments
    """

    key: Union[Unset, str] = UNSET
    receipt_date: Union[Unset, datetime.date] = UNSET
    last_modified: Union[Unset, datetime.datetime] = UNSET
    from_: Union[Unset, str] = UNSET
    links: Union[Unset, List[Any]] = UNSET
    only_attachment: Union[Unset, bool] = UNSET
    attachments: Union[Unset, List["Attachment"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        receipt_date: Union[Unset, str] = UNSET
        if not isinstance(self.receipt_date, Unset):
            receipt_date = self.receipt_date.isoformat()

        last_modified: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        from_ = self.from_
        links: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links

        only_attachment = self.only_attachment
        attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()

                attachments.append(attachments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if receipt_date is not UNSET:
            field_dict["receiptDate"] = receipt_date
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if from_ is not UNSET:
            field_dict["from"] = from_
        if links is not UNSET:
            field_dict["links"] = links
        if only_attachment is not UNSET:
            field_dict["onlyAttachment"] = only_attachment
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attachment import Attachment

        d = src_dict.copy()
        key = d.pop("key", UNSET)

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

        from_ = d.pop("from", UNSET)

        links = cast(List[Any], d.pop("links", UNSET))

        only_attachment = d.pop("onlyAttachment", UNSET)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = Attachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        reply = cls(
            key=key,
            receipt_date=receipt_date,
            last_modified=last_modified,
            from_=from_,
            links=links,
            only_attachment=only_attachment,
            attachments=attachments,
        )

        reply.additional_properties = d
        return reply

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
