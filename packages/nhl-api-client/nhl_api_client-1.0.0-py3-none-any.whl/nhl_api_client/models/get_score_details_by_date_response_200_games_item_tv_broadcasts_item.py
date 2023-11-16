from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetScoreDetailsByDateResponse200GamesItemTvBroadcastsItem")


@_attrs_define
class GetScoreDetailsByDateResponse200GamesItemTvBroadcastsItem:
    """
    Attributes:
        id (int):
        market (str):
        country_code (str):
        network (str):
    """

    id: int
    market: str
    country_code: str
    network: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        market = self.market
        country_code = self.country_code
        network = self.network

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "market": market,
                "countryCode": country_code,
                "network": network,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        market = d.pop("market")

        country_code = d.pop("countryCode")

        network = d.pop("network")

        get_score_details_by_date_response_200_games_item_tv_broadcasts_item = cls(
            id=id,
            market=market,
            country_code=country_code,
            network=network,
        )

        get_score_details_by_date_response_200_games_item_tv_broadcasts_item.additional_properties = d
        return get_score_details_by_date_response_200_games_item_tv_broadcasts_item

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
