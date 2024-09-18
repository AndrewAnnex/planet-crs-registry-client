from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exception_item import ExceptionItem


T = TypeVar("T", bound="ExceptionReport")


@_attrs_define
class ExceptionReport:
    """
    Attributes:
        exception (ExceptionItem):
        version (Union[Unset, str]):  Default: '2.0.0'.
        schema_location (Union[Unset, str]):  Default: 'http://www.opengis.net/ows/2.0
            http://schemas.opengis.net/ows/2.0/owsExceptionReport.xsd'.
    """

    exception: "ExceptionItem"
    version: Union[Unset, str] = "2.0.0"
    schema_location: Union[Unset, str] = (
        "http://www.opengis.net/ows/2.0 http://schemas.opengis.net/ows/2.0/owsExceptionReport.xsd"
    )
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exception = self.exception.to_dict()

        version = self.version

        schema_location = self.schema_location

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exception": exception,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if schema_location is not UNSET:
            field_dict["schema_location"] = schema_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.exception_item import ExceptionItem

        d = src_dict.copy()
        exception = ExceptionItem.from_dict(d.pop("exception"))

        version = d.pop("version", UNSET)

        schema_location = d.pop("schema_location", UNSET)

        exception_report = cls(
            exception=exception,
            version=version,
            schema_location=schema_location,
        )

        exception_report.additional_properties = d
        return exception_report

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
