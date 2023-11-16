from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.language_string import LanguageString


T = TypeVar("T", bound="GetScoreDetailsByDateResponse200GamesItemAwayTeam")


@_attrs_define
class GetScoreDetailsByDateResponse200GamesItemAwayTeam:
    """
    Attributes:
        id (int):
        name (LanguageString):
        abbrev (str):
        score (int):
        sog (int):
        logo (str):
    """

    id: int
    name: "LanguageString"
    abbrev: str
    score: int
    sog: int
    logo: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name.to_dict()

        abbrev = self.abbrev
        score = self.score
        sog = self.sog
        logo = self.logo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "abbrev": abbrev,
                "score": score,
                "sog": sog,
                "logo": logo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.language_string import LanguageString

        d = src_dict.copy()
        id = d.pop("id")

        name = LanguageString.from_dict(d.pop("name"))

        abbrev = d.pop("abbrev")

        score = d.pop("score")

        sog = d.pop("sog")

        logo = d.pop("logo")

        get_score_details_by_date_response_200_games_item_away_team = cls(
            id=id,
            name=name,
            abbrev=abbrev,
            score=score,
            sog=sog,
            logo=logo,
        )

        get_score_details_by_date_response_200_games_item_away_team.additional_properties = d
        return get_score_details_by_date_response_200_games_item_away_team

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
