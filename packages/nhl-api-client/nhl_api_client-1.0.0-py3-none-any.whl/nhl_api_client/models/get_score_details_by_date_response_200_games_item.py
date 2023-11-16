from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_score_details_by_date_response_200_games_item_away_team import (
        GetScoreDetailsByDateResponse200GamesItemAwayTeam,
    )
    from ..models.get_score_details_by_date_response_200_games_item_clock import (
        GetScoreDetailsByDateResponse200GamesItemClock,
    )
    from ..models.get_score_details_by_date_response_200_games_item_game_outcome import (
        GetScoreDetailsByDateResponse200GamesItemGameOutcome,
    )
    from ..models.get_score_details_by_date_response_200_games_item_goals_item import (
        GetScoreDetailsByDateResponse200GamesItemGoalsItem,
    )
    from ..models.get_score_details_by_date_response_200_games_item_home_team import (
        GetScoreDetailsByDateResponse200GamesItemHomeTeam,
    )
    from ..models.get_score_details_by_date_response_200_games_item_period_descriptor import (
        GetScoreDetailsByDateResponse200GamesItemPeriodDescriptor,
    )
    from ..models.get_score_details_by_date_response_200_games_item_tv_broadcasts_item import (
        GetScoreDetailsByDateResponse200GamesItemTvBroadcastsItem,
    )
    from ..models.language_string import LanguageString


T = TypeVar("T", bound="GetScoreDetailsByDateResponse200GamesItem")


@_attrs_define
class GetScoreDetailsByDateResponse200GamesItem:
    """
    Attributes:
        id (int):
        season (int):
        game_type (int):
        game_date (str):
        venue (LanguageString):
        start_time_utc (str):
        eastern_utc_offset (str):
        venue_utc_offset (str):
        tv_broadcasts (List['GetScoreDetailsByDateResponse200GamesItemTvBroadcastsItem']):
        game_state (str):
        game_schedule_state (str):
        away_team (GetScoreDetailsByDateResponse200GamesItemAwayTeam):
        home_team (GetScoreDetailsByDateResponse200GamesItemHomeTeam):
        game_center_link (str):
        three_min_recap (str):
        clock (GetScoreDetailsByDateResponse200GamesItemClock):
        neutral_site (bool):
        venue_timezone (str):
        period (int):
        period_descriptor (GetScoreDetailsByDateResponse200GamesItemPeriodDescriptor):
        game_outcome (GetScoreDetailsByDateResponse200GamesItemGameOutcome):
        goals (List['GetScoreDetailsByDateResponse200GamesItemGoalsItem']):
        three_min_recap_fr (Union[Unset, str]):
    """

    id: int
    season: int
    game_type: int
    game_date: str
    venue: "LanguageString"
    start_time_utc: str
    eastern_utc_offset: str
    venue_utc_offset: str
    tv_broadcasts: List["GetScoreDetailsByDateResponse200GamesItemTvBroadcastsItem"]
    game_state: str
    game_schedule_state: str
    away_team: "GetScoreDetailsByDateResponse200GamesItemAwayTeam"
    home_team: "GetScoreDetailsByDateResponse200GamesItemHomeTeam"
    game_center_link: str
    three_min_recap: str
    clock: "GetScoreDetailsByDateResponse200GamesItemClock"
    neutral_site: bool
    venue_timezone: str
    period: int
    period_descriptor: "GetScoreDetailsByDateResponse200GamesItemPeriodDescriptor"
    game_outcome: "GetScoreDetailsByDateResponse200GamesItemGameOutcome"
    goals: List["GetScoreDetailsByDateResponse200GamesItemGoalsItem"]
    three_min_recap_fr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        season = self.season
        game_type = self.game_type
        game_date = self.game_date
        venue = self.venue.to_dict()

        start_time_utc = self.start_time_utc
        eastern_utc_offset = self.eastern_utc_offset
        venue_utc_offset = self.venue_utc_offset
        tv_broadcasts = []
        for tv_broadcasts_item_data in self.tv_broadcasts:
            tv_broadcasts_item = tv_broadcasts_item_data.to_dict()

            tv_broadcasts.append(tv_broadcasts_item)

        game_state = self.game_state
        game_schedule_state = self.game_schedule_state
        away_team = self.away_team.to_dict()

        home_team = self.home_team.to_dict()

        game_center_link = self.game_center_link
        three_min_recap = self.three_min_recap
        clock = self.clock.to_dict()

        neutral_site = self.neutral_site
        venue_timezone = self.venue_timezone
        period = self.period
        period_descriptor = self.period_descriptor.to_dict()

        game_outcome = self.game_outcome.to_dict()

        goals = []
        for goals_item_data in self.goals:
            goals_item = goals_item_data.to_dict()

            goals.append(goals_item)

        three_min_recap_fr = self.three_min_recap_fr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "season": season,
                "gameType": game_type,
                "gameDate": game_date,
                "venue": venue,
                "startTimeUTC": start_time_utc,
                "easternUTCOffset": eastern_utc_offset,
                "venueUTCOffset": venue_utc_offset,
                "tvBroadcasts": tv_broadcasts,
                "gameState": game_state,
                "gameScheduleState": game_schedule_state,
                "awayTeam": away_team,
                "homeTeam": home_team,
                "gameCenterLink": game_center_link,
                "threeMinRecap": three_min_recap,
                "clock": clock,
                "neutralSite": neutral_site,
                "venueTimezone": venue_timezone,
                "period": period,
                "periodDescriptor": period_descriptor,
                "gameOutcome": game_outcome,
                "goals": goals,
            }
        )
        if three_min_recap_fr is not UNSET:
            field_dict["threeMinRecapFr"] = three_min_recap_fr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_score_details_by_date_response_200_games_item_away_team import (
            GetScoreDetailsByDateResponse200GamesItemAwayTeam,
        )
        from ..models.get_score_details_by_date_response_200_games_item_clock import (
            GetScoreDetailsByDateResponse200GamesItemClock,
        )
        from ..models.get_score_details_by_date_response_200_games_item_game_outcome import (
            GetScoreDetailsByDateResponse200GamesItemGameOutcome,
        )
        from ..models.get_score_details_by_date_response_200_games_item_goals_item import (
            GetScoreDetailsByDateResponse200GamesItemGoalsItem,
        )
        from ..models.get_score_details_by_date_response_200_games_item_home_team import (
            GetScoreDetailsByDateResponse200GamesItemHomeTeam,
        )
        from ..models.get_score_details_by_date_response_200_games_item_period_descriptor import (
            GetScoreDetailsByDateResponse200GamesItemPeriodDescriptor,
        )
        from ..models.get_score_details_by_date_response_200_games_item_tv_broadcasts_item import (
            GetScoreDetailsByDateResponse200GamesItemTvBroadcastsItem,
        )
        from ..models.language_string import LanguageString

        d = src_dict.copy()
        id = d.pop("id")

        season = d.pop("season")

        game_type = d.pop("gameType")

        game_date = d.pop("gameDate")

        venue = LanguageString.from_dict(d.pop("venue"))

        start_time_utc = d.pop("startTimeUTC")

        eastern_utc_offset = d.pop("easternUTCOffset")

        venue_utc_offset = d.pop("venueUTCOffset")

        tv_broadcasts = []
        _tv_broadcasts = d.pop("tvBroadcasts")
        for tv_broadcasts_item_data in _tv_broadcasts:
            tv_broadcasts_item = GetScoreDetailsByDateResponse200GamesItemTvBroadcastsItem.from_dict(
                tv_broadcasts_item_data
            )

            tv_broadcasts.append(tv_broadcasts_item)

        game_state = d.pop("gameState")

        game_schedule_state = d.pop("gameScheduleState")

        away_team = GetScoreDetailsByDateResponse200GamesItemAwayTeam.from_dict(d.pop("awayTeam"))

        home_team = GetScoreDetailsByDateResponse200GamesItemHomeTeam.from_dict(d.pop("homeTeam"))

        game_center_link = d.pop("gameCenterLink")

        three_min_recap = d.pop("threeMinRecap")

        clock = GetScoreDetailsByDateResponse200GamesItemClock.from_dict(d.pop("clock"))

        neutral_site = d.pop("neutralSite")

        venue_timezone = d.pop("venueTimezone")

        period = d.pop("period")

        period_descriptor = GetScoreDetailsByDateResponse200GamesItemPeriodDescriptor.from_dict(
            d.pop("periodDescriptor")
        )

        game_outcome = GetScoreDetailsByDateResponse200GamesItemGameOutcome.from_dict(d.pop("gameOutcome"))

        goals = []
        _goals = d.pop("goals")
        for goals_item_data in _goals:
            goals_item = GetScoreDetailsByDateResponse200GamesItemGoalsItem.from_dict(goals_item_data)

            goals.append(goals_item)

        three_min_recap_fr = d.pop("threeMinRecapFr", UNSET)

        get_score_details_by_date_response_200_games_item = cls(
            id=id,
            season=season,
            game_type=game_type,
            game_date=game_date,
            venue=venue,
            start_time_utc=start_time_utc,
            eastern_utc_offset=eastern_utc_offset,
            venue_utc_offset=venue_utc_offset,
            tv_broadcasts=tv_broadcasts,
            game_state=game_state,
            game_schedule_state=game_schedule_state,
            away_team=away_team,
            home_team=home_team,
            game_center_link=game_center_link,
            three_min_recap=three_min_recap,
            clock=clock,
            neutral_site=neutral_site,
            venue_timezone=venue_timezone,
            period=period,
            period_descriptor=period_descriptor,
            game_outcome=game_outcome,
            goals=goals,
            three_min_recap_fr=three_min_recap_fr,
        )

        get_score_details_by_date_response_200_games_item.additional_properties = d
        return get_score_details_by_date_response_200_games_item

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
