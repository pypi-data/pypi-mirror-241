from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetScoreDetailsByDateResponse200GameWeekItem")


@_attrs_define
class GetScoreDetailsByDateResponse200GameWeekItem:
    """
    Attributes:
        date (str):
        day_abbrev (str):
        number_of_games (int):
    """

    date: str
    day_abbrev: str
    number_of_games: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        day_abbrev = self.day_abbrev
        number_of_games = self.number_of_games

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "dayAbbrev": day_abbrev,
                "numberOfGames": number_of_games,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date")

        day_abbrev = d.pop("dayAbbrev")

        number_of_games = d.pop("numberOfGames")

        get_score_details_by_date_response_200_game_week_item = cls(
            date=date,
            day_abbrev=day_abbrev,
            number_of_games=number_of_games,
        )

        get_score_details_by_date_response_200_game_week_item.additional_properties = d
        return get_score_details_by_date_response_200_game_week_item

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
