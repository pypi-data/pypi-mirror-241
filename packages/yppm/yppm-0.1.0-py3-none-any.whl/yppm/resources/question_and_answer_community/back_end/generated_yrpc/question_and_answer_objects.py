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
class A_Post(YRPC_OBJECT_BASE_CLASS):
    owner_id: str | None = None
    id: str | None = None
    title: str | None = None
    description: str | None = None
    comment_id_list: list[str] | None = None
    create_time_in_10_numbers_timestamp_format: int | None = None
    tag: str | None = None

    _property_name_to_its_type_dict = {
        "owner_id": str,
        "id": str,
        "title": str,
        "description": str,
        "comment_id_list": str,
        "create_time_in_10_numbers_timestamp_format": int,
        "tag": str,
    }

    @dataclass()
    class _key_string_dict:
        owner_id: str = "owner_id"
        id: str = "id"
        title: str = "title"
        description: str = "description"
        comment_id_list: str = "comment_id_list"
        create_time_in_10_numbers_timestamp_format: str = "create_time_in_10_numbers_timestamp_format"
        tag: str = "tag"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: A_Post = super().from_dict(dict)
        return new_variable


@dataclass()
class A_Comment(YRPC_OBJECT_BASE_CLASS):
    owner_id: str | None = None
    id: str | None = None
    parent_post_id: str | None = None
    parent_post_owner_id: str | None = None
    description: str | None = None
    create_time_in_10_numbers_timestamp_format: int | None = None
    tag: str | None = None

    _property_name_to_its_type_dict = {
        "owner_id": str,
        "id": str,
        "parent_post_id": str,
        "parent_post_owner_id": str,
        "description": str,
        "create_time_in_10_numbers_timestamp_format": int,
        "tag": str,
    }

    @dataclass()
    class _key_string_dict:
        owner_id: str = "owner_id"
        id: str = "id"
        parent_post_id: str = "parent_post_id"
        parent_post_owner_id: str = "parent_post_owner_id"
        description: str = "description"
        create_time_in_10_numbers_timestamp_format: str = "create_time_in_10_numbers_timestamp_format"
        tag: str = "tag"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: A_Comment = super().from_dict(dict)
        return new_variable


@dataclass()
class About_Request(YRPC_OBJECT_BASE_CLASS):


    _property_name_to_its_type_dict = {

    }

    @dataclass()
    class _key_string_dict:
        pass

    def from_dict(self, dict: dict[str, Any]):
        new_variable: About_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class About_Response(YRPC_OBJECT_BASE_CLASS):
    about: str | None = None

    _property_name_to_its_type_dict = {
        "about": str,
    }

    @dataclass()
    class _key_string_dict:
        about: str = "about"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: About_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Ask_Yingshaoxo_Ai_Request(YRPC_OBJECT_BASE_CLASS):
    input: str | None = None

    _property_name_to_its_type_dict = {
        "input": str,
    }

    @dataclass()
    class _key_string_dict:
        input: str = "input"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Ask_Yingshaoxo_Ai_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Ask_Yingshaoxo_Ai_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    answers: str | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "answers": str,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        answers: str = "answers"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Ask_Yingshaoxo_Ai_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Search_Request(YRPC_OBJECT_BASE_CLASS):
    search_input: str | None = None
    page_size: int | None = None
    page_number: int | None = None
    owner_id: str | None = None

    _property_name_to_its_type_dict = {
        "search_input": str,
        "page_size": int,
        "page_number": int,
        "owner_id": str,
    }

    @dataclass()
    class _key_string_dict:
        search_input: str = "search_input"
        page_size: str = "page_size"
        page_number: str = "page_number"
        owner_id: str = "owner_id"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Search_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Search_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    post_list: list[A_Post] | None = None
    comment_list: list[A_Comment] | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "post_list": A_Post,
        "comment_list": A_Comment,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        post_list: str = "post_list"
        comment_list: str = "comment_list"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Search_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Get_A_Post_Request(YRPC_OBJECT_BASE_CLASS):
    id: str | None = None

    _property_name_to_its_type_dict = {
        "id": str,
    }

    @dataclass()
    class _key_string_dict:
        id: str = "id"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Get_A_Post_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Get_A_Post_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    post: A_Post | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "post": A_Post,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        post: str = "post"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Get_A_Post_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Get_Comment_List_By_Id_List_Request(YRPC_OBJECT_BASE_CLASS):
    comment_id_list: list[str] | None = None

    _property_name_to_its_type_dict = {
        "comment_id_list": str,
    }

    @dataclass()
    class _key_string_dict:
        comment_id_list: str = "comment_id_list"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Get_Comment_List_By_Id_List_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Get_Comment_List_By_Id_List_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    comment_list: list[A_Comment] | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "comment_list": A_Comment,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        comment_list: str = "comment_list"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Get_Comment_List_By_Id_List_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Add_Post_Request(YRPC_OBJECT_BASE_CLASS):
    username: str | None = None
    a_post: A_Post | None = None

    _property_name_to_its_type_dict = {
        "username": str,
        "a_post": A_Post,
    }

    @dataclass()
    class _key_string_dict:
        username: str = "username"
        a_post: str = "a_post"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Add_Post_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Add_Post_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    success: bool | None = None
    post_id: str | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "success": bool,
        "post_id": str,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        success: str = "success"
        post_id: str = "post_id"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Add_Post_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Comment_Post_Request(YRPC_OBJECT_BASE_CLASS):
    username: str | None = None
    a_comment: A_Comment | None = None

    _property_name_to_its_type_dict = {
        "username": str,
        "a_comment": A_Comment,
    }

    @dataclass()
    class _key_string_dict:
        username: str = "username"
        a_comment: str = "a_comment"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Comment_Post_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Comment_Post_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    success: bool | None = None
    comment_id: str | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "success": bool,
        "comment_id": str,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        success: str = "success"
        comment_id: str = "comment_id"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Comment_Post_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Download_Backup_Data_Request(YRPC_OBJECT_BASE_CLASS):
    username: str | None = None

    _property_name_to_its_type_dict = {
        "username": str,
    }

    @dataclass()
    class _key_string_dict:
        username: str = "username"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Download_Backup_Data_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Download_Backup_Data_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    file_name: str | None = None
    file_bytes_in_base64_format: str | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "file_name": str,
        "file_bytes_in_base64_format": str,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        file_name: str = "file_name"
        file_bytes_in_base64_format: str = "file_bytes_in_base64_format"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Download_Backup_Data_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Admin_Download_Backup_Data_Request(YRPC_OBJECT_BASE_CLASS):
    token: str | None = None

    _property_name_to_its_type_dict = {
        "token": str,
    }

    @dataclass()
    class _key_string_dict:
        token: str = "token"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Admin_Download_Backup_Data_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Admin_Download_Backup_Data_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    file_name: str | None = None
    file_bytes_in_base64_format: str | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "file_name": str,
        "file_bytes_in_base64_format": str,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        file_name: str = "file_name"
        file_bytes_in_base64_format: str = "file_bytes_in_base64_format"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Admin_Download_Backup_Data_Response = super().from_dict(dict)
        return new_variable


@dataclass()
class Admin_Upload_Backup_Data_Request(YRPC_OBJECT_BASE_CLASS):
    token: str | None = None
    file_bytes_in_base64_format: str | None = None

    _property_name_to_its_type_dict = {
        "token": str,
        "file_bytes_in_base64_format": str,
    }

    @dataclass()
    class _key_string_dict:
        token: str = "token"
        file_bytes_in_base64_format: str = "file_bytes_in_base64_format"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Admin_Upload_Backup_Data_Request = super().from_dict(dict)
        return new_variable


@dataclass()
class Admin_Upload_Backup_Data_Response(YRPC_OBJECT_BASE_CLASS):
    error: str | None = None
    success: bool | None = None

    _property_name_to_its_type_dict = {
        "error": str,
        "success": bool,
    }

    @dataclass()
    class _key_string_dict:
        error: str = "error"
        success: str = "success"

    def from_dict(self, dict: dict[str, Any]):
        new_variable: Admin_Upload_Backup_Data_Response = super().from_dict(dict)
        return new_variable