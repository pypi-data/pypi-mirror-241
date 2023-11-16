from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_score_details_by_date_response_200_game_week_item import (
        GetScoreDetailsByDateResponse200GameWeekItem,
    )
    from ..models.get_score_details_by_date_response_200_games_item import GetScoreDetailsByDateResponse200GamesItem
    from ..models.get_score_details_by_date_response_200_odds_partners_item import (
        GetScoreDetailsByDateResponse200OddsPartnersItem,
    )


T = TypeVar("T", bound="GetScoreDetailsByDateResponse200")


@_attrs_define
class GetScoreDetailsByDateResponse200:
    """
    Attributes:
        prev_date (str):
        current_date (str):
        next_date (str):
        game_week (List['GetScoreDetailsByDateResponse200GameWeekItem']):
        odds_partners (List['GetScoreDetailsByDateResponse200OddsPartnersItem']):
        games (List['GetScoreDetailsByDateResponse200GamesItem']):
    """

    prev_date: str
    current_date: str
    next_date: str
    game_week: List["GetScoreDetailsByDateResponse200GameWeekItem"]
    odds_partners: List["GetScoreDetailsByDateResponse200OddsPartnersItem"]
    games: List["GetScoreDetailsByDateResponse200GamesItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prev_date = self.prev_date
        current_date = self.current_date
        next_date = self.next_date
        game_week = []
        for game_week_item_data in self.game_week:
            game_week_item = game_week_item_data.to_dict()

            game_week.append(game_week_item)

        odds_partners = []
        for odds_partners_item_data in self.odds_partners:
            odds_partners_item = odds_partners_item_data.to_dict()

            odds_partners.append(odds_partners_item)

        games = []
        for games_item_data in self.games:
            games_item = games_item_data.to_dict()

            games.append(games_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prevDate": prev_date,
                "currentDate": current_date,
                "nextDate": next_date,
                "gameWeek": game_week,
                "oddsPartners": odds_partners,
                "games": games,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_score_details_by_date_response_200_game_week_item import (
            GetScoreDetailsByDateResponse200GameWeekItem,
        )
        from ..models.get_score_details_by_date_response_200_games_item import GetScoreDetailsByDateResponse200GamesItem
        from ..models.get_score_details_by_date_response_200_odds_partners_item import (
            GetScoreDetailsByDateResponse200OddsPartnersItem,
        )

        d = src_dict.copy()
        prev_date = d.pop("prevDate")

        current_date = d.pop("currentDate")

        next_date = d.pop("nextDate")

        game_week = []
        _game_week = d.pop("gameWeek")
        for game_week_item_data in _game_week:
            game_week_item = GetScoreDetailsByDateResponse200GameWeekItem.from_dict(game_week_item_data)

            game_week.append(game_week_item)

        odds_partners = []
        _odds_partners = d.pop("oddsPartners")
        for odds_partners_item_data in _odds_partners:
            odds_partners_item = GetScoreDetailsByDateResponse200OddsPartnersItem.from_dict(odds_partners_item_data)

            odds_partners.append(odds_partners_item)

        games = []
        _games = d.pop("games")
        for games_item_data in _games:
            games_item = GetScoreDetailsByDateResponse200GamesItem.from_dict(games_item_data)

            games.append(games_item)

        get_score_details_by_date_response_200 = cls(
            prev_date=prev_date,
            current_date=current_date,
            next_date=next_date,
            game_week=game_week,
            odds_partners=odds_partners,
            games=games,
        )

        get_score_details_by_date_response_200.additional_properties = d
        return get_score_details_by_date_response_200

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
