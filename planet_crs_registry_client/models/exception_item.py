from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exception_text import ExceptionText


T = TypeVar("T", bound="ExceptionItem")


@_attrs_define
class ExceptionItem:
    """
    Attributes:
        exception_code (str):
        exception_text (ExceptionText):
    """

    exception_code: str
    exception_text: "ExceptionText"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exception_code = self.exception_code

        exception_text = self.exception_text.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exceptionCode": exception_code,
                "exceptionText": exception_text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.exception_text import ExceptionText

        d = src_dict.copy()
        exception_code = d.pop("exceptionCode")

        exception_text = ExceptionText.from_dict(d.pop("exceptionText"))

        exception_item = cls(
            exception_code=exception_code,
            exception_text=exception_text,
        )

        exception_item.additional_properties = d
        return exception_item

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
