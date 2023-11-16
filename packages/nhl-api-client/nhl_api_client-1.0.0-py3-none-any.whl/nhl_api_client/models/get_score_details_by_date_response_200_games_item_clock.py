from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetScoreDetailsByDateResponse200GamesItemClock")


@_attrs_define
class GetScoreDetailsByDateResponse200GamesItemClock:
    """
    Attributes:
        time_remaining (str):
        seconds_remaining (int):
        running (bool):
        in_intermission (bool):
    """

    time_remaining: str
    seconds_remaining: int
    running: bool
    in_intermission: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time_remaining = self.time_remaining
        seconds_remaining = self.seconds_remaining
        running = self.running
        in_intermission = self.in_intermission

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeRemaining": time_remaining,
                "secondsRemaining": seconds_remaining,
                "running": running,
                "inIntermission": in_intermission,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time_remaining = d.pop("timeRemaining")

        seconds_remaining = d.pop("secondsRemaining")

        running = d.pop("running")

        in_intermission = d.pop("inIntermission")

        get_score_details_by_date_response_200_games_item_clock = cls(
            time_remaining=time_remaining,
            seconds_remaining=seconds_remaining,
            running=running,
            in_intermission=in_intermission,
        )

        get_score_details_by_date_response_200_games_item_clock.additional_properties = d
        return get_score_details_by_date_response_200_games_item_clock

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
