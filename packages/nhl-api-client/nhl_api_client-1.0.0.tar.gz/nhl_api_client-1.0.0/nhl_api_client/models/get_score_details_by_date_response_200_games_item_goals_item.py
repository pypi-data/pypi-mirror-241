from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_score_details_by_date_response_200_games_item_goals_item_period_descriptor import (
        GetScoreDetailsByDateResponse200GamesItemGoalsItemPeriodDescriptor,
    )
    from ..models.language_string import LanguageString


T = TypeVar("T", bound="GetScoreDetailsByDateResponse200GamesItemGoalsItem")


@_attrs_define
class GetScoreDetailsByDateResponse200GamesItemGoalsItem:
    """
    Attributes:
        period (int):
        period_descriptor (GetScoreDetailsByDateResponse200GamesItemGoalsItemPeriodDescriptor):
        time_in_period (str):
        player_id (int):
        name (LanguageString):
        mugshot (str):
        team_abbrev (str):
        goals_to_date (int):
        away_score (int):
        home_score (int):
        strength (str):
        highlight_clip (int):
        highlight_clip_fr (Union[Unset, int]):
    """

    period: int
    period_descriptor: "GetScoreDetailsByDateResponse200GamesItemGoalsItemPeriodDescriptor"
    time_in_period: str
    player_id: int
    name: "LanguageString"
    mugshot: str
    team_abbrev: str
    goals_to_date: int
    away_score: int
    home_score: int
    strength: str
    highlight_clip: int
    highlight_clip_fr: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period
        period_descriptor = self.period_descriptor.to_dict()

        time_in_period = self.time_in_period
        player_id = self.player_id
        name = self.name.to_dict()

        mugshot = self.mugshot
        team_abbrev = self.team_abbrev
        goals_to_date = self.goals_to_date
        away_score = self.away_score
        home_score = self.home_score
        strength = self.strength
        highlight_clip = self.highlight_clip
        highlight_clip_fr = self.highlight_clip_fr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
                "periodDescriptor": period_descriptor,
                "timeInPeriod": time_in_period,
                "playerId": player_id,
                "name": name,
                "mugshot": mugshot,
                "teamAbbrev": team_abbrev,
                "goalsToDate": goals_to_date,
                "awayScore": away_score,
                "homeScore": home_score,
                "strength": strength,
                "highlightClip": highlight_clip,
            }
        )
        if highlight_clip_fr is not UNSET:
            field_dict["highlightClipFr"] = highlight_clip_fr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_score_details_by_date_response_200_games_item_goals_item_period_descriptor import (
            GetScoreDetailsByDateResponse200GamesItemGoalsItemPeriodDescriptor,
        )
        from ..models.language_string import LanguageString

        d = src_dict.copy()
        period = d.pop("period")

        period_descriptor = GetScoreDetailsByDateResponse200GamesItemGoalsItemPeriodDescriptor.from_dict(
            d.pop("periodDescriptor")
        )

        time_in_period = d.pop("timeInPeriod")

        player_id = d.pop("playerId")

        name = LanguageString.from_dict(d.pop("name"))

        mugshot = d.pop("mugshot")

        team_abbrev = d.pop("teamAbbrev")

        goals_to_date = d.pop("goalsToDate")

        away_score = d.pop("awayScore")

        home_score = d.pop("homeScore")

        strength = d.pop("strength")

        highlight_clip = d.pop("highlightClip")

        highlight_clip_fr = d.pop("highlightClipFr", UNSET)

        get_score_details_by_date_response_200_games_item_goals_item = cls(
            period=period,
            period_descriptor=period_descriptor,
            time_in_period=time_in_period,
            player_id=player_id,
            name=name,
            mugshot=mugshot,
            team_abbrev=team_abbrev,
            goals_to_date=goals_to_date,
            away_score=away_score,
            home_score=home_score,
            strength=strength,
            highlight_clip=highlight_clip,
            highlight_clip_fr=highlight_clip_fr,
        )

        get_score_details_by_date_response_200_games_item_goals_item.additional_properties = d
        return get_score_details_by_date_response_200_games_item_goals_item

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
