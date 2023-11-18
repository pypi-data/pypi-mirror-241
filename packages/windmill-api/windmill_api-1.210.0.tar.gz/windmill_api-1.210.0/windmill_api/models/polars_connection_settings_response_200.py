from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polars_connection_settings_response_200_dataset_keys_item import (
        PolarsConnectionSettingsResponse200DatasetKeysItem,
    )


T = TypeVar("T", bound="PolarsConnectionSettingsResponse200")


@_attrs_define
class PolarsConnectionSettingsResponse200:
    """
    Attributes:
        dataset_keys (Union[Unset, List['PolarsConnectionSettingsResponse200DatasetKeysItem']]):
    """

    dataset_keys: Union[Unset, List["PolarsConnectionSettingsResponse200DatasetKeysItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dataset_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dataset_keys, Unset):
            dataset_keys = []
            for dataset_keys_item_data in self.dataset_keys:
                dataset_keys_item = dataset_keys_item_data.to_dict()

                dataset_keys.append(dataset_keys_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dataset_keys is not UNSET:
            field_dict["dataset_keys"] = dataset_keys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.polars_connection_settings_response_200_dataset_keys_item import (
            PolarsConnectionSettingsResponse200DatasetKeysItem,
        )

        d = src_dict.copy()
        dataset_keys = []
        _dataset_keys = d.pop("dataset_keys", UNSET)
        for dataset_keys_item_data in _dataset_keys or []:
            dataset_keys_item = PolarsConnectionSettingsResponse200DatasetKeysItem.from_dict(dataset_keys_item_data)

            dataset_keys.append(dataset_keys_item)

        polars_connection_settings_response_200 = cls(
            dataset_keys=dataset_keys,
        )

        polars_connection_settings_response_200.additional_properties = d
        return polars_connection_settings_response_200

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
