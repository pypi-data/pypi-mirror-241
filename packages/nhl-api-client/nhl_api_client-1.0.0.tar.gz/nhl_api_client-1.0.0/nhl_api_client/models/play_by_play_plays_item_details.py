from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayByPlayPlaysItemDetails")


@_attrs_define
class PlayByPlayPlaysItemDetails:
    """
    Attributes:
        event_owner_team_id (Union[Unset, None, int]):
        losing_player_id (Union[Unset, None, int]):
        winning_player_id (Union[Unset, None, int]):
        x_coord (Union[Unset, None, int]):
        y_coord (Union[Unset, None, int]):
        zone_code (Union[Unset, None, str]):
        reason (Union[Unset, None, str]):
    """

    event_owner_team_id: Union[Unset, None, int] = UNSET
    losing_player_id: Union[Unset, None, int] = UNSET
    winning_player_id: Union[Unset, None, int] = UNSET
    x_coord: Union[Unset, None, int] = UNSET
    y_coord: Union[Unset, None, int] = UNSET
    zone_code: Union[Unset, None, str] = UNSET
    reason: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_owner_team_id = self.event_owner_team_id
        losing_player_id = self.losing_player_id
        winning_player_id = self.winning_player_id
        x_coord = self.x_coord
        y_coord = self.y_coord
        zone_code = self.zone_code
        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_owner_team_id is not UNSET:
            field_dict["eventOwnerTeamId"] = event_owner_team_id
        if losing_player_id is not UNSET:
            field_dict["losingPlayerId"] = losing_player_id
        if winning_player_id is not UNSET:
            field_dict["winningPlayerId"] = winning_player_id
        if x_coord is not UNSET:
            field_dict["xCoord"] = x_coord
        if y_coord is not UNSET:
            field_dict["yCoord"] = y_coord
        if zone_code is not UNSET:
            field_dict["zoneCode"] = zone_code
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_owner_team_id = d.pop("eventOwnerTeamId", UNSET)

        losing_player_id = d.pop("losingPlayerId", UNSET)

        winning_player_id = d.pop("winningPlayerId", UNSET)

        x_coord = d.pop("xCoord", UNSET)

        y_coord = d.pop("yCoord", UNSET)

        zone_code = d.pop("zoneCode", UNSET)

        reason = d.pop("reason", UNSET)

        play_by_play_plays_item_details = cls(
            event_owner_team_id=event_owner_team_id,
            losing_player_id=losing_player_id,
            winning_player_id=winning_player_id,
            x_coord=x_coord,
            y_coord=y_coord,
            zone_code=zone_code,
            reason=reason,
        )

        play_by_play_plays_item_details.additional_properties = d
        return play_by_play_plays_item_details

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
