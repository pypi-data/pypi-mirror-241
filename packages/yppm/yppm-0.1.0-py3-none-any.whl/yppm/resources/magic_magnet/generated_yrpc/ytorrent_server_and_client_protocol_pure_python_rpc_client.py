from .ytorrent_server_and_client_protocol_objects import *

from typing import Any, Callable
import json
from urllib import request


def _send_a_post(url: str, data: dict, headers: dict | None=None) -> str:
    a_request = request.Request(url, method="POST")
    a_request.add_header('Content-Type', 'application/json')
    if headers != None:
        for key, value in headers.items():
            a_request.add_header(key, value)
    data = json.dumps(data, indent=4)
    data = data.encode("utf-8", errors="ignore")
    r_ = request.urlopen(a_request, data=data)
    content = r_.read().decode("utf-8", errors="ignore")
    return content


class Client_ytorrent_server_and_client_protocol:
    def __init__(self, service_url: str, headers: dict[str, Any] | None = None, error_handle_function: Callable[[str], None] | None = None, special_error_key: str = "__yingshaoxo's_error__", interceptor_function: Callable[[dict], None] | None = None):
        if (service_url.endswith("/")):
            service_url = service_url[:-1]
        self._service_url = service_url 

        if headers == None:
            headers = {}
        self._header = headers

        def _default_error_handle_function(error_message: str):
            print(f"errors: {error_message}")
        if error_handle_function == None:
            error_handle_function = _default_error_handle_function
        self._error_handle_function = error_handle_function

        self._special_error_key = special_error_key

        def _default_interceptor_function(data: dict):
            pass
        if interceptor_function == None:
            interceptor_function = _default_interceptor_function
        self._interceptor_function = interceptor_function

    def _get_reponse_or_error_by_url_path_and_input(self, sub_url: str, input_dict: dict[str, Any]):
        the_url = f"{self._service_url}/ytorrent_server_and_client_protocol/{sub_url}/"
        try:
            response = _send_a_post(url=the_url, data=input_dict, headers=self._header)
            json_response = json.loads(response)
            self._interceptor_function(json_response)
            return json_response
        except Exception as e: 
            return {self._special_error_key: str(e)}

    def seed(self, item: Seed_Request, ignore_error: bool | None=None) -> Seed_Response | None:
        result = self._get_reponse_or_error_by_url_path_and_input("seed", item.to_dict())
        if self._special_error_key in result.keys():
            if ((ignore_error == None) or ((ignore_error != None) and (not ignore_error))):
                self._error_handle_function(result[self._special_error_key])
            return None
        else:
            return Seed_Response().from_dict(result)

    def search(self, item: Search_Request, ignore_error: bool | None=None) -> Search_Response | None:
        result = self._get_reponse_or_error_by_url_path_and_input("search", item.to_dict())
        if self._special_error_key in result.keys():
            if ((ignore_error == None) or ((ignore_error != None) and (not ignore_error))):
                self._error_handle_function(result[self._special_error_key])
            return None
        else:
            return Search_Response().from_dict(result)

    def download_resource_info(self, item: Download_Resource_Info_Request, ignore_error: bool | None=None) -> Download_Resource_Info_Response | None:
        result = self._get_reponse_or_error_by_url_path_and_input("download_resource_info", item.to_dict())
        if self._special_error_key in result.keys():
            if ((ignore_error == None) or ((ignore_error != None) and (not ignore_error))):
                self._error_handle_function(result[self._special_error_key])
            return None
        else:
            return Download_Resource_Info_Response().from_dict(result)

    def download(self, item: Download_Request, ignore_error: bool | None=None) -> Download_Response | None:
        result = self._get_reponse_or_error_by_url_path_and_input("download", item.to_dict())
        if self._special_error_key in result.keys():
            if ((ignore_error == None) or ((ignore_error != None) and (not ignore_error))):
                self._error_handle_function(result[self._special_error_key])
            return None
        else:
            return Download_Response().from_dict(result)

    def upload(self, item: Upload_Request, ignore_error: bool | None=None) -> Upload_Response | None:
        result = self._get_reponse_or_error_by_url_path_and_input("upload", item.to_dict())
        if self._special_error_key in result.keys():
            if ((ignore_error == None) or ((ignore_error != None) and (not ignore_error))):
                self._error_handle_function(result[self._special_error_key])
            return None
        else:
            return Upload_Response().from_dict(result)

    def get_shared_tracker_list(self, item: Get_Shared_Tracker_List_Request, ignore_error: bool | None=None) -> Get_Shared_Tracker_List_Response | None:
        result = self._get_reponse_or_error_by_url_path_and_input("get_shared_tracker_list", item.to_dict())
        if self._special_error_key in result.keys():
            if ((ignore_error == None) or ((ignore_error != None) and (not ignore_error))):
                self._error_handle_function(result[self._special_error_key])
            return None
        else:
            return Get_Shared_Tracker_List_Response().from_dict(result)

    def version(self, item: Version_Request, ignore_error: bool | None=None) -> Version_Response | None:
        result = self._get_reponse_or_error_by_url_path_and_input("version", item.to_dict())
        if self._special_error_key in result.keys():
            if ((ignore_error == None) or ((ignore_error != None) and (not ignore_error))):
                self._error_handle_function(result[self._special_error_key])
            return None
        else:
            return Version_Response().from_dict(result)