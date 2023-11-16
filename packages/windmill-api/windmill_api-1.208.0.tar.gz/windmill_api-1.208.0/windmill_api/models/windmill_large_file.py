from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WindmillLargeFile")


@_attrs_define
class WindmillLargeFile:
    """
    Attributes:
        s3 (str):
        s3_bucket (Union[Unset, str]):
    """

    s3: str
    s3_bucket: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        s3 = self.s3
        s3_bucket = self.s3_bucket

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "s3": s3,
            }
        )
        if s3_bucket is not UNSET:
            field_dict["s3_bucket"] = s3_bucket

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        s3 = d.pop("s3")

        s3_bucket = d.pop("s3_bucket", UNSET)

        windmill_large_file = cls(
            s3=s3,
            s3_bucket=s3_bucket,
        )

        windmill_large_file.additional_properties = d
        return windmill_large_file

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
