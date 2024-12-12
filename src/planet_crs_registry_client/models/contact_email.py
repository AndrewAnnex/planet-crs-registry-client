from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ContactEmail")


@_attrs_define
class ContactEmail:
    """Contact Email.

    Attributes:
        first_name (str):
        name (str):
        email (str):
        comments (str):
    """

    first_name: str
    name: str
    email: str
    comments: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name

        name = self.name

        email = self.email

        comments = self.comments

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firstName": first_name,
                "name": name,
                "email": email,
                "comments": comments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName")

        name = d.pop("name")

        email = d.pop("email")

        comments = d.pop("comments")

        contact_email = cls(
            first_name=first_name,
            name=name,
            email=email,
            comments=comments,
        )

        contact_email.additional_properties = d
        return contact_email

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
