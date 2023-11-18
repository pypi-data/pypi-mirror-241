from .ytorrent_server_and_client_protocol_objects import *


from typing import Any
import json
from auto_everything.http_ import Yingshaoxo_Http_Server, Yingshaoxo_Http_Request


class Service_ytorrent_server_and_client_protocol:
    def seed(self, headers: dict[str, str], item: Seed_Request) -> Seed_Response:
        default_response = Seed_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def search(self, headers: dict[str, str], item: Search_Request) -> Search_Response:
        default_response = Search_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def download_resource_info(self, headers: dict[str, str], item: Download_Resource_Info_Request) -> Download_Resource_Info_Response:
        default_response = Download_Resource_Info_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def download(self, headers: dict[str, str], item: Download_Request) -> Download_Response:
        default_response = Download_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def upload(self, headers: dict[str, str], item: Upload_Request) -> Upload_Response:
        default_response = Upload_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def get_shared_tracker_list(self, headers: dict[str, str], item: Get_Shared_Tracker_List_Request) -> Get_Shared_Tracker_List_Response:
        default_response = Get_Shared_Tracker_List_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def version(self, headers: dict[str, str], item: Version_Request) -> Version_Response:
        default_response = Version_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response


def run(service_instance: Service_ytorrent_server_and_client_protocol, port: str, html_folder_path: str="", serve_html_under_which_url: str="/"):
    def handle_get_url(sub_url: str, headers: dict[str, str]) -> str:
        return 'Hi there, this website is using yrpc (Yingshaoxo remote procedure control module).'

    def handle_post_url(sub_url: str, headers: dict[str, str], item: dict[str, Any]) -> dict | str:
        sub_url = sub_url.strip("/")
        sub_url = sub_url.replace("ytorrent_server_and_client_protocol", "", 1)
        sub_url = sub_url.strip("/")
        request_url = sub_url.split("/")[0].strip()

        if (request_url == ""):
            return f"Request url '{request_url}' is empty"
        elif (request_url == "seed"):
            correct_item = Seed_Request().from_dict(item)
            return json.dumps((service_instance.seed(headers, correct_item)).to_dict())

        elif (request_url == "search"):
            correct_item = Search_Request().from_dict(item)
            return json.dumps((service_instance.search(headers, correct_item)).to_dict())

        elif (request_url == "download_resource_info"):
            correct_item = Download_Resource_Info_Request().from_dict(item)
            return json.dumps((service_instance.download_resource_info(headers, correct_item)).to_dict())

        elif (request_url == "download"):
            correct_item = Download_Request().from_dict(item)
            return json.dumps((service_instance.download(headers, correct_item)).to_dict())

        elif (request_url == "upload"):
            correct_item = Upload_Request().from_dict(item)
            return json.dumps((service_instance.upload(headers, correct_item)).to_dict())

        elif (request_url == "get_shared_tracker_list"):
            correct_item = Get_Shared_Tracker_List_Request().from_dict(item)
            return json.dumps((service_instance.get_shared_tracker_list(headers, correct_item)).to_dict())

        elif (request_url == "version"):
            correct_item = Version_Request().from_dict(item)
            return json.dumps((service_instance.version(headers, correct_item)).to_dict())

        return f"No API url matchs '{request_url}'"

    def general_handler(request: Yingshaoxo_Http_Request) -> dict | str:
        response = f"No handler for {request.url}"
        if request.method == "GET":
            response = handle_get_url(request.url, request.headers)
        elif request.method == "POST":
            response = handle_post_url(request.url, request.headers, json.loads(request.payload))
        return response

    router = {
        r"(.*)": general_handler,
    }

    yingshaoxo_http_server = Yingshaoxo_Http_Server(router=router)
    yingshaoxo_http_server.start(host="0.0.0.0", port=int(port), html_folder_path=html_folder_path, serve_html_under_which_url=serve_html_under_which_url)


if __name__ == "__main__":
    service_instance = Service_ytorrent_server_and_client_protocol()
    run(service_instance, port="6060")