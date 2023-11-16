from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetScoreDetailsByDateResponse200OddsPartnersItem")


@_attrs_define
class GetScoreDetailsByDateResponse200OddsPartnersItem:
    """
    Attributes:
        partner_id (int):
        country (str):
        name (str):
        image_url (str):
        bg_color (str):
        text_color (str):
        accent_color (str):
        site_url (Union[Unset, str]):
    """

    partner_id: int
    country: str
    name: str
    image_url: str
    bg_color: str
    text_color: str
    accent_color: str
    site_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        partner_id = self.partner_id
        country = self.country
        name = self.name
        image_url = self.image_url
        bg_color = self.bg_color
        text_color = self.text_color
        accent_color = self.accent_color
        site_url = self.site_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partnerId": partner_id,
                "country": country,
                "name": name,
                "imageUrl": image_url,
                "bgColor": bg_color,
                "textColor": text_color,
                "accentColor": accent_color,
            }
        )
        if site_url is not UNSET:
            field_dict["siteUrl"] = site_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        partner_id = d.pop("partnerId")

        country = d.pop("country")

        name = d.pop("name")

        image_url = d.pop("imageUrl")

        bg_color = d.pop("bgColor")

        text_color = d.pop("textColor")

        accent_color = d.pop("accentColor")

        site_url = d.pop("siteUrl", UNSET)

        get_score_details_by_date_response_200_odds_partners_item = cls(
            partner_id=partner_id,
            country=country,
            name=name,
            image_url=image_url,
            bg_color=bg_color,
            text_color=text_color,
            accent_color=accent_color,
            site_url=site_url,
        )

        get_score_details_by_date_response_200_odds_partners_item.additional_properties = d
        return get_score_details_by_date_response_200_odds_partners_item

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
