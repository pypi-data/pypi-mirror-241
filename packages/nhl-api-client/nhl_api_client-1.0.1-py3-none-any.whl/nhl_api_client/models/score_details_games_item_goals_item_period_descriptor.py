from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="ScoreDetailsGamesItemGoalsItemPeriodDescriptor")


@_attrs_define
class ScoreDetailsGamesItemGoalsItemPeriodDescriptor:
    """
    Attributes:
        number (int):
        period_type (str):
    """

    number: int
    period_type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        period_type = self.period_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "periodType": period_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number")

        period_type = d.pop("periodType")

        score_details_games_item_goals_item_period_descriptor = cls(
            number=number,
            period_type=period_type,
        )

        score_details_games_item_goals_item_period_descriptor.additional_properties = d
        return score_details_games_item_goals_item_period_descriptor

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
