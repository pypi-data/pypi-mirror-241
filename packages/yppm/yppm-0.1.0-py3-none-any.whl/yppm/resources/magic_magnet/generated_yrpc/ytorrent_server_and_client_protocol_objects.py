import copy
from dataclasses import dataclass
from enum import Enum
from typing import Any


_ygrpc_official_types = [int, float, str, bool]


def convert_dict_that_has_enum_object_into_pure_dict(value: Any) -> dict[str, Any] | list[Any] | Any:
    if type(value) is list:
        new_list: list[Any] = []
        for one in value: #type: ignore
            new_list.append(convert_dict_that_has_enum_object_into_pure_dict(value=one)) 
        return new_list
    elif type(value) is dict:
        new_dict: dict[str, Any] = {}
        for key_, value_ in value.items(): #type: ignore
            new_dict[key_] = convert_dict_that_has_enum_object_into_pure_dict(value=value_) #type: ignore
        return new_dict
    else:
        if str(type(value)).startswith("<enum"):
            return value.name
        else:
            if type(value) in _ygrpc_official_types:
                return value
            else:
                # handle custom message data type
                if value == None:
                    return None
                elif str(type(value)).startswith("<class"):
                    return convert_dict_that_has_enum_object_into_pure_dict(
                        value=value.to_dict()
                    )
    return None


def convert_pure_dict_into_a_dict_that_has_enum_object(pure_value: Any, refrence_value: Any) -> Any:
    if type(pure_value) is list:
        new_list: list[Any] = []
        for one in pure_value: #type: ignore
            new_list.append(
                convert_pure_dict_into_a_dict_that_has_enum_object(pure_value=one, refrence_value=refrence_value)
            ) 
        return new_list
    elif type(pure_value) is dict:
        if str(refrence_value).startswith("<class"):
            new_object = refrence_value()
            old_property_list = getattr(new_object, "_property_name_to_its_type_dict")
            for key in old_property_list.keys():
                if key in pure_value.keys():
                    setattr(new_object, key, convert_pure_dict_into_a_dict_that_has_enum_object(pure_value[key], old_property_list[key])) # type: ignore
            return new_object
        else:
            return None
    else:
        if str(refrence_value).startswith("<enum"):
            default_value = None
            for temp_index, temp_value in enumerate(refrence_value._member_names_):
                if temp_value == pure_value:
                    default_value = refrence_value(temp_value) 
                    break
            return default_value
        else:
            if refrence_value in _ygrpc_official_types:
                return pure_value
            else:
                return None


class YRPC_OBJECT_BASE_CLASS:
    def to_dict(self, ignore_null: bool=False) -> dict[str, Any]:
        old_dict = {}
        for key in self._property_name_to_its_type_dict.keys(): #type: ignore
            old_dict[key] = self.__dict__[key] #type: ignore
        new_dict = convert_dict_that_has_enum_object_into_pure_dict(value=old_dict.copy())
        return new_dict.copy() #type: ignore

    def from_dict(self, dict: dict[str, Any]) -> Any:
        new_object = convert_pure_dict_into_a_dict_that_has_enum_object(pure_value=dict.copy(), refrence_value=self.__class__)

        new_object_dict = new_object.__dict__.copy() 
        for key, value in new_object_dict.items():
            if key in self.__dict__:
                setattr(self, key, value)

        return new_object

    def _clone(self) -> Any:
        return copy.deepcopy(self)




        
@dataclass()
class Ytorrent_Config(YRPC_OBJECT_BASE_CLASS):
    default_remote_service_port: int | None = None
    exposed_seeder_tracker_address: str | None = None
    default_local_service_port: int | None = None
    file_segments_memory_pool_size_in_mb: int | None = None
    max_acceptable_file_segment_size_in_mb: int | None = None
    polling_waiting_time_in_seconds: int | None = None
    tracker_ip_or_url_list: list[str] | None = None
    download_folder_path: str | None = None

    _property_name_to_its_type_dict = {
        "default_remote_service_port": int,
        "exposed_seeder_tracker_address": str,
        "default_local_service_port": int,
        "file_segments_memory_pool_size_in_mb": int,
        "max_acceptable_file_segment_size_in_mb": int,
        "polling_waiting_time_in_seconds": int,
        "tracker_ip_or_url_list": str,
        "download_folder_path": str,
    }

    @dataclass()
    class _key_string_dict:
        default_remote_service_port: str = "default_remote_service_port"
        exposed_seeder_tracker_address: str = "exposed_seeder_tracker_address"
        default_local_service_port: str = "default_local_service_port"
        file_segments_memory_pool_size_in_mb: str = "file_segments_memory_pool_size_in_mb"
        max_acceptable_file_segment_size_in_mb: str = "max_acceptable_file_segment_size_in_mb"
        polling_waiting_time_in_seconds: str = "polling_waiting_time_in_seconds"
        tracker_ip_or_url_list: str = "tracker_ip_or_url_list"
        download_folder_path: str = "download_folder_path"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Ytorrent_Config = super().from_dict(dict)
        return new_variable


@dataclass()
class A_Resource(YRPC_OBJECT_BASE_CLASS):
    name: str | None = None
    is_single_file: bool | None = None
    file_or_folder_hash: str | None = None
    file_or_folder_size_in_bytes: str | None = None
    root_folder: str | None = None
    folder_path_list_relative_to_root_folder: list[str] | None = None
    file_path_list_relative_to_root_folder: list[str] | None = None
    file_size_in_bytes_list: list[int] | None = None
    file_hash_list: list[str] | None = None
    file_download_status_list: list[bool] | None = None
    download_complete: bool | None = None
    exposed_seeder_tracker_address: str | None = None

    _property_name_to_its_type_dict = {
        "name": str,
        "is_single_file": bool,
        "file_or_folder_hash": str,
        "file_or_folder_size_in_bytes": str,
        "root_folder": str,
        "folder_path_list_relative_to_root_folder": str,
        "file_path_list_relative_to_root_folder": str,
        "file_size_in_bytes_list": int,
        "file_hash_list": str,
        "file_download_status_list": bool,
        "download_complete": bool,
        "exposed_seeder_tracker_address": str,
    }

    @dataclass()
    class _key_string_dict:
        name: str = "name"
        is_single_file: str = "is_single_file"
        file_or_folder_hash: str = "file_or_folder_hash"
        file_or_folder_size_in_bytes: str = "file_or_folder_size_in_bytes"
        root_folder: str = "root_folder"
        folder_path_list_relative_to_root_folder: str = "folder_path_list_relative_to_root_folder"
        file_path_list_relative_to_root_folder: str = "file_path_list_relative_to_root_folder"
        file_size_in_bytes_list: str = "file_size_in_bytes_list"
        file_hash_list: str = "file_hash_list"
        file_download_status_list: str = "file_download_status_list"
        download_complete: str = "download_complete"
        exposed_seeder_tracker_address: str = "exposed_seeder_tracker_address"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: A_Resource = super().from_dict(dict)
        return new_variable


@dataclass()
class Need_To_Upload_Notification(YRPC_OBJECT_BASE_CLASS):
    file_or_folder_hash: str | None = None
    file_path_relative_to_root_folder: str | None = None
    file_segment_size_in_bytes: int | None = None
    segment_number: int | None = None

    _property_name_to_its_type_dict = {
        "file_or_folder_hash": str,
        "file_path_relative_to_root_folder": str,
        "file_segment_size_in_bytes": int,
        "segment_number": int,
    }

    @dataclass()
    class _key_string_dict:
        file_or_folder_hash: str = "file_or_folder_hash"
        file_path_relative_to_root_folder: str = "file_path_relative_to_root_folder"
        file_segment_size_in_bytes: str = "file_segment_size_in_bytes"
        segment_number: str = "segment_number"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Need_To_Upload_Notification = super().from_dict(dict)
        return new_variable


@dataclass()
class File_Segment(YRPC_OBJECT_BASE_CLASS):
    file_or_folder_hash: str | None = None
    file_path_relative_to_root_folder: str | None = None
    file_segment_size_in_bytes: int | None = None
    segment_number: int | None = None
    file_segment_bytes_in_base64: str | None = None
    _current_time_in_timestamp: str | None = None

    _property_name_to_its_type_dict = {
        "file_or_folder_hash": str,
        "file_path_relative_to_root_folder": str,
        "file_segment_size_in_bytes": int,
        "segment_number": int,
        "file_segment_bytes_in_base64": str,
        "_current_time_in_timestamp": str,
    }

    @dataclass()
    class _key_string_dict:
        file_or_folder_hash: str = "file_or_folder_hash"
        file_path_relative_to_root_folder: str = "file_path_relative_to_root_folder"
        file_segment_size_in_bytes: str = "file_segment_size_in_bytes"
        segment_number: str = "segment_number"
        file_segment_bytes_in_base64: str = "file_segment_bytes_in_base64"
        _current_time_in_timestamp: str = "_current_time_in_timestamp"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: File_Segment = super().from_dict(dict)
        return new_variable


@dataclass()
class A_Whole_File(YRPC_OBJECT_BASE_CLASS):
    file_hash: str | None = None
    root_folder: str | None = None
    file_name: str | None = None
    file_segment_list: list[File_Segment] | None = None

    _property_name_to_its_type_dict = {
        "file_hash": str,
        "root_folder": str,
        "file_name": str,
        "file_segment_list": File_Segment,
    }

    @dataclass()
    class _key_string_dict:
        file_hash: str = "file_hash"
        root_folder: str = "root_folder"
        file_name: str = "file_name"
        file_segment_list: str = "file_segment_list"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: A_Whole_File = super().from_dict(dict)
        return new_variable


@dataclass()
class Seed_Request(YRPC_OBJECT_BASE_CLASS):
    a_resource: A_Resource | None = None

    _property_name_to_its_type_dict = {
        "a_resource": A_Resource,
    }

    @dataclass()
    class _key_string_dict:
        a_resource: str = "a_resource"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Seed_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Seed_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    success: bool | None = None
    someone_needs_you_to_upload_your_file: bool | None = None
    need_to_upload_notification_list: list[Need_To_Upload_Notification] | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "success": bool,
        "someone_needs_you_to_upload_your_file": bool,
        "need_to_upload_notification_list": Need_To_Upload_Notification,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        success: str = "success"
        someone_needs_you_to_upload_your_file: str = "someone_needs_you_to_upload_your_file"
        need_to_upload_notification_list: str = "need_to_upload_notification_list"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Seed_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Upload_Request(YRPC_OBJECT_BASE_CLASS):
    need_to_upload_notification: Need_To_Upload_Notification | None = None
    file_segment_bytes_in_base64: str | None = None

    _property_name_to_its_type_dict = {
        "need_to_upload_notification": Need_To_Upload_Notification,
        "file_segment_bytes_in_base64": str,
    }

    @dataclass()
    class _key_string_dict:
        need_to_upload_notification: str = "need_to_upload_notification"
        file_segment_bytes_in_base64: str = "file_segment_bytes_in_base64"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Upload_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Upload_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    success: str | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "success": str,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        success: str = "success"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Upload_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Search_Request(YRPC_OBJECT_BASE_CLASS):
    search_input: str | None = None
    page_size: int | None = None
    page_number: int | None = None

    _property_name_to_its_type_dict = {
        "search_input": str,
        "page_size": int,
        "page_number": int,
    }

    @dataclass()
    class _key_string_dict:
        search_input: str = "search_input"
        page_size: str = "page_size"
        page_number: str = "page_number"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Search_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Search_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    resource_list: list[A_Resource] | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "resource_list": A_Resource,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        resource_list: str = "resource_list"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Search_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Download_Resource_Info_Request(YRPC_OBJECT_BASE_CLASS):
    file_or_folder_hash: str | None = None

    _property_name_to_its_type_dict = {
        "file_or_folder_hash": str,
    }

    @dataclass()
    class _key_string_dict:
        file_or_folder_hash: str = "file_or_folder_hash"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Download_Resource_Info_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Download_Resource_Info_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    try_it_later_when_other_need_to_upload: bool | None = None
    a_resource: A_Resource | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "try_it_later_when_other_need_to_upload": bool,
        "a_resource": A_Resource,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        try_it_later_when_other_need_to_upload: str = "try_it_later_when_other_need_to_upload"
        a_resource: str = "a_resource"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Download_Resource_Info_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Download_Request(YRPC_OBJECT_BASE_CLASS):
    need_to_upload_notification: Need_To_Upload_Notification | None = None

    _property_name_to_its_type_dict = {
        "need_to_upload_notification": Need_To_Upload_Notification,
    }

    @dataclass()
    class _key_string_dict:
        need_to_upload_notification: str = "need_to_upload_notification"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Download_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Download_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    try_it_later_when_other_need_to_upload: bool | None = None
    file_segment_bytes_in_base64: str | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "try_it_later_when_other_need_to_upload": bool,
        "file_segment_bytes_in_base64": str,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        try_it_later_when_other_need_to_upload: str = "try_it_later_when_other_need_to_upload"
        file_segment_bytes_in_base64: str = "file_segment_bytes_in_base64"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Download_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Get_Shared_Tracker_List_Request(YRPC_OBJECT_BASE_CLASS):


    _property_name_to_its_type_dict = {

    }

    @dataclass()
    class _key_string_dict:
        pass

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Get_Shared_Tracker_List_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Get_Shared_Tracker_List_Response(YRPC_OBJECT_BASE_CLASS):
    tracker_ip_list: list[str] | None = None

    _property_name_to_its_type_dict = {
        "tracker_ip_list": str,
    }

    @dataclass()
    class _key_string_dict:
        tracker_ip_list: str = "tracker_ip_list"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Get_Shared_Tracker_List_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Version_Request(YRPC_OBJECT_BASE_CLASS):


    _property_name_to_its_type_dict = {

    }

    @dataclass()
    class _key_string_dict:
        pass

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Version_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Version_Response(YRPC_OBJECT_BASE_CLASS):
    name: str | None = None
    version_code: int | None = None

    _property_name_to_its_type_dict = {
        "name": str,
        "version_code": int,
    }

    @dataclass()
    class _key_string_dict:
        name: str = "name"
        version_code: str = "version_code"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Version_Response = super().from_dict(dict)
        return new_variable