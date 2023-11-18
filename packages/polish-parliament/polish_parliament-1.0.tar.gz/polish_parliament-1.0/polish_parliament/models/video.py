import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Video")


@_attrs_define
class Video:
    r"""a video

    Attributes:
        unid (Union[Unset, str]): An unique indentifier of a transmission Example: 758DAA6CDF68DFC0C12588F6003C6EF3.
        video_link (Union[Unset, str]): An URL or URLs to a video transmission Example:
            http://r.dcs.redcdn.pl/nvr/o2/sejm/ENC01/live.livx, http://r.dcs.redcdn.pl/nvr/o2/sejm/ENC30/live.livx,
            http://r.dcs.redcdn.pl/nvr/o2/sejm/ENC31/live.livx,
            http://r.dcs.redcdn.pl/nvr/o2/sejm/ENC32/live.livx?startTime=710323200000.
        video_messages_link (Union[Unset, str]): A link to a messages for a transmission
        type (Union[Unset, str]): A type of transmission Example: komisja.
        transcribe (Union[Unset, bool]): Is there a transcription available Example: True.
        start_date_time (Union[Unset, datetime.datetime]): A start date and time of transmission Example: 2023-05-24
            10:00:00.
        end_date_time (Union[Unset, datetime.datetime]): An end date and time of transmission Example: 2023-05-24
            12:00:00.
        sign_lang_link (Union[Unset, str]): An URL of a sign language transmission
        title (Union[Unset, str]): A title of a transmission Example: Parlamentarny Zespół ds. Personelu Niemedycznego
            Ochrony Zdrowia.
        audio (Union[Unset, str]): A link to a an audio file
        room (Union[Unset, str]): A room where the transmission takes place Example: sala im. Konstytucji 3-go Maja (nr
            118, bud. C).
        description (Union[Unset, str]): A description of a transmission Example: Medyczne zawody niemedyczne -
            przyszłość przenoszenia niektórych dodatkowych zadań w ramach opieki nad pacjentem na personel niemedyczny oraz
            tworzenie związanych z tym możliwości rozwoju zawodowego dla personelu.\r\n\r\n.
        committee (Union[Unset, str]): A committee code if the transmission is from a committee meeting Example: SUE.
    """

    unid: Union[Unset, str] = UNSET
    video_link: Union[Unset, str] = UNSET
    video_messages_link: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    transcribe: Union[Unset, bool] = UNSET
    start_date_time: Union[Unset, datetime.datetime] = UNSET
    end_date_time: Union[Unset, datetime.datetime] = UNSET
    sign_lang_link: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    audio: Union[Unset, str] = UNSET
    room: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    committee: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unid = self.unid
        video_link = self.video_link
        video_messages_link = self.video_messages_link
        type = self.type
        transcribe = self.transcribe
        start_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        end_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_date_time, Unset):
            end_date_time = self.end_date_time.isoformat()

        sign_lang_link = self.sign_lang_link
        title = self.title
        audio = self.audio
        room = self.room
        description = self.description
        committee = self.committee

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unid is not UNSET:
            field_dict["unid"] = unid
        if video_link is not UNSET:
            field_dict["videoLink"] = video_link
        if video_messages_link is not UNSET:
            field_dict["videoMessagesLink"] = video_messages_link
        if type is not UNSET:
            field_dict["type"] = type
        if transcribe is not UNSET:
            field_dict["transcribe"] = transcribe
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time
        if sign_lang_link is not UNSET:
            field_dict["signLangLink"] = sign_lang_link
        if title is not UNSET:
            field_dict["title"] = title
        if audio is not UNSET:
            field_dict["audio"] = audio
        if room is not UNSET:
            field_dict["room"] = room
        if description is not UNSET:
            field_dict["description"] = description
        if committee is not UNSET:
            field_dict["committee"] = committee

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unid = d.pop("unid", UNSET)

        video_link = d.pop("videoLink", UNSET)

        video_messages_link = d.pop("videoMessagesLink", UNSET)

        type = d.pop("type", UNSET)

        transcribe = d.pop("transcribe", UNSET)

        _start_date_time = d.pop("startDateTime", UNSET)
        start_date_time: Union[Unset, datetime.datetime]
        if isinstance(_start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = isoparse(_start_date_time)

        _end_date_time = d.pop("endDateTime", UNSET)
        end_date_time: Union[Unset, datetime.datetime]
        if isinstance(_end_date_time, Unset):
            end_date_time = UNSET
        else:
            end_date_time = isoparse(_end_date_time)

        sign_lang_link = d.pop("signLangLink", UNSET)

        title = d.pop("title", UNSET)

        audio = d.pop("audio", UNSET)

        room = d.pop("room", UNSET)

        description = d.pop("description", UNSET)

        committee = d.pop("committee", UNSET)

        video = cls(
            unid=unid,
            video_link=video_link,
            video_messages_link=video_messages_link,
            type=type,
            transcribe=transcribe,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            sign_lang_link=sign_lang_link,
            title=title,
            audio=audio,
            room=room,
            description=description,
            committee=committee,
        )

        video.additional_properties = d
        return video

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
