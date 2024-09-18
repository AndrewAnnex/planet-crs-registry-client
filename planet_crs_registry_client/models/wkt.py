import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WKT")


@_attrs_define
class WKT:
    """This references a WKT

    Attributes:
        created_at (datetime.datetime): The date where the record has been inserted
        id (str): ID of WKT. Pattern of the ID is the following IAU:<version>:<code>
        version (int): Version of the WKT
        code (int): WKT code
        solar_body (str): Solar body such as Mercury, Venus, ...
        datum_name (str): Datum name
        ellipsoid_name (str): Ellipsoid name
        wkt (str): WKT
        projection_name (Union[None, Unset, str]): Projection name
    """

    created_at: datetime.datetime
    id: str
    version: int
    code: int
    solar_body: str
    datum_name: str
    ellipsoid_name: str
    wkt: str
    projection_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        version = self.version

        code = self.code

        solar_body = self.solar_body

        datum_name = self.datum_name

        ellipsoid_name = self.ellipsoid_name

        wkt = self.wkt

        projection_name: Union[None, Unset, str]
        if isinstance(self.projection_name, Unset):
            projection_name = UNSET
        else:
            projection_name = self.projection_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "version": version,
                "code": code,
                "solar_body": solar_body,
                "datum_name": datum_name,
                "ellipsoid_name": ellipsoid_name,
                "wkt": wkt,
            }
        )
        if projection_name is not UNSET:
            field_dict["projection_name"] = projection_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        id = d.pop("id")

        version = d.pop("version")

        code = d.pop("code")

        solar_body = d.pop("solar_body")

        datum_name = d.pop("datum_name")

        ellipsoid_name = d.pop("ellipsoid_name")

        wkt = d.pop("wkt")

        def _parse_projection_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        projection_name = _parse_projection_name(d.pop("projection_name", UNSET))

        wkt = cls(
            created_at=created_at,
            id=id,
            version=version,
            code=code,
            solar_body=solar_body,
            datum_name=datum_name,
            ellipsoid_name=ellipsoid_name,
            wkt=wkt,
            projection_name=projection_name,
        )

        return wkt
