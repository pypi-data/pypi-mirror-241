print("This is a server, but also a client. It is a node in a people for people network.")
print()

from typing import Any
import sys
import multiprocessing
from time import sleep
from datetime import datetime
import multiprocessing
import os
import re
import json

if os.path.exists("../../auto_everything"):
    sys.path.insert(1, "../../")

from auto_everything.terminal import Terminal, Terminal_User_Interface
from auto_everything.python import Python
from auto_everything.disk import Disk, Store
from auto_everything.io import IO
from auto_everything.cryptography import Encryption_And_Decryption, Password_Generator, JWT_Tool
from auto_everything.time import Time
terminal = Terminal()
terminal_user_interface = Terminal_User_Interface()
disk = Disk()
python = Python()
io_ = IO()
time_ = Time()
core_store = Store("magic_magnet_core_channel")
#data_store = Store("magic_magnet_data_channel")

#import generated_yrpc.ytorrent_server_and_client_protocol_objects as ytorrent_server_and_client_protocol_objects
import generated_yrpc.ytorrent_server_and_client_protocol_objects as ytorrent_objects
import generated_yrpc.ytorrent_server_and_client_protocol_pure_python_rpc as ytorrent_server_and_client_protocol_pure_python_rpc
from generated_yrpc.ytorrent_server_and_client_protocol_yingshaoxo_database_rpc import Yingshaoxo_Database_Excutor_ytorrent_server_and_client_protocol

import generated_yrpc.ytorrent_server_and_client_protocol_pure_python_rpc_client as ytorrent_server_and_client_protocol_pure_python_rpc_client

SECRET_TEXT = "some 'people' are spying on you"
encryption_and_decryption = Encryption_And_Decryption()
secret_dict = encryption_and_decryption.get_secret_alphabet_dict(a_secret_string=SECRET_TEXT)
password_generator = Password_Generator(SECRET_TEXT)

jwt_tool = JWT_Tool()

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    #print('running in a PyInstaller bundle')
    def resource_path(relative_path: str) -> str:
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path) #type: ignore
        return os.path.join(os.path.abspath("."), relative_path)
    resource_basic_folder_path = resource_path(".")
    the_database_path = disk.join_paths(disk.get_parent_directory_path(disk.get_parent_directory_path(resource_basic_folder_path)), './database_data')
else:
    #print('running in a normal Python process')
    resource_basic_folder_path = disk.get_directory_path(__file__)
    the_database_path = disk.join_paths(resource_basic_folder_path, './database_data')

print(f"resource_basic_folder_path: {resource_basic_folder_path}")
print(f"database_path: {the_database_path}")
print(f"default download_path: ~/Downloads/Ytorrent_Download")
print()
disk.create_a_folder(the_database_path)
remote_database_path = disk.join_paths(the_database_path, "remote_service")
local_database_path = disk.join_paths(the_database_path, "local_service")
the_manager_ = multiprocessing.Manager()
a_global_dict_for_multiprocessing = the_manager_.dict()
#database_excutor_for_remote_service = Yingshaoxo_Database_Excutor_ytorrent_server_and_client_protocol(database_base_folder=remote_database_path, use_sqlite=False, global_multiprocessing_shared_dict=a_global_dict_for_multiprocessing)
database_excutor_for_remote_service = Yingshaoxo_Database_Excutor_ytorrent_server_and_client_protocol(database_base_folder=remote_database_path, use_sqlite=False)
database_excutor_for_local_service = Yingshaoxo_Database_Excutor_ytorrent_server_and_client_protocol(database_base_folder=local_database_path, use_sqlite=False)


# For now, the ytorrent_config object will not synchronize between processes and threads
YTORRENT_CONFIG = ytorrent_objects.Ytorrent_Config(
    default_remote_service_port=1111,
    exposed_seeder_tracker_address=None, # we may need to automatically get the public ip address, so it would be http://0.0.0.0:1111
    default_local_service_port=1212,
    file_segments_memory_pool_size_in_mb=200,
    max_acceptable_file_segment_size_in_mb=1,
    polling_waiting_time_in_seconds=60,
    tracker_ip_or_url_list=["https://ytorrent.ai-tools-online.xyz"],
    download_folder_path=terminal.fix_path("~/Downloads/Ytorrent_Download", startswith=True)
)
json_configuration_folder_path = terminal.fix_path("~/.ytorrent", startswith=True)
disk.create_a_folder(json_configuration_folder_path)
json_configuration_file_path = disk.join_paths(json_configuration_folder_path, "configuration.json")
tracker_urls_file_path = disk.join_paths(json_configuration_folder_path, "tracker_urls.txt")
if (disk.exists(json_configuration_file_path)):
    json_configuration_object = json.loads(io_.read(json_configuration_file_path))
    tracker_ip_or_url_list_ = YTORRENT_CONFIG.tracker_ip_or_url_list
    temp_dict = YTORRENT_CONFIG.to_dict()
    temp_dict.update(json_configuration_object)
    if tracker_ip_or_url_list_ != None:
        temp_dict["tracker_ip_or_url_list"] = tracker_ip_or_url_list_ + temp_dict["tracker_ip_or_url_list"]
    YTORRENT_CONFIG = YTORRENT_CONFIG.from_dict(temp_dict)
if (disk.exists(tracker_urls_file_path)):
    tracker_text = io_.read(tracker_urls_file_path).strip()
    new_tracker_ip_list = tracker_text.split("\n")
    new_tracker_ip_list = [one.strip() for one in new_tracker_ip_list]
    new_tracker_ip_list.reverse()
    if YTORRENT_CONFIG.tracker_ip_or_url_list != None:
        YTORRENT_CONFIG.tracker_ip_or_url_list = new_tracker_ip_list + YTORRENT_CONFIG.tracker_ip_or_url_list

_default_remote_service_port = os.getenv("default_remote_service_port")
if _default_remote_service_port is not None:
    YTORRENT_CONFIG.default_remote_service_port = int(_default_remote_service_port)

_default_local_service_port = os.getenv("default_local_service_port")
if _default_local_service_port is not None:
    YTORRENT_CONFIG.default_local_service_port = int(_default_local_service_port)

_exposed_seeder_tracker_address = os.getenv("exposed_seeder_tracker_address")
if _exposed_seeder_tracker_address is not None:
    YTORRENT_CONFIG.exposed_seeder_tracker_address = int(_exposed_seeder_tracker_address)

_file_segments_memory_pool_size_in_mb = os.getenv("file_segments_memory_pool_size_in_mb")
if _file_segments_memory_pool_size_in_mb is not None:
    YTORRENT_CONFIG.file_segments_memory_pool_size_in_mb = int(_file_segments_memory_pool_size_in_mb)

_max_acceptable_file_segment_size_in_mb = os.getenv("max_acceptable_file_segment_size_in_mb")
if _max_acceptable_file_segment_size_in_mb is not None:
    YTORRENT_CONFIG.max_acceptable_file_segment_size_in_mb = int(_max_acceptable_file_segment_size_in_mb)

_polling_waiting_time_in_seconds = os.getenv("polling_waiting_time_in_seconds")
if _polling_waiting_time_in_seconds is not None:
    YTORRENT_CONFIG.polling_waiting_time_in_seconds = int(_polling_waiting_time_in_seconds)

_tracker_ip_or_url_list = os.getenv("tracker_ip_or_url_list")
if _tracker_ip_or_url_list is not None:
    if YTORRENT_CONFIG.tracker_ip_or_url_list == None:
        YTORRENT_CONFIG.tracker_ip_or_url_list = []
    if "," in _tracker_ip_or_url_list:
        YTORRENT_CONFIG.tracker_ip_or_url_list = [one.strip() for one in _tracker_ip_or_url_list.split(",")] + YTORRENT_CONFIG.tracker_ip_or_url_list
    else:
        YTORRENT_CONFIG.tracker_ip_or_url_list = [_tracker_ip_or_url_list.strip()] + YTORRENT_CONFIG.tracker_ip_or_url_list


YTORRENT_CONFIG.download_folder_path = terminal.fix_path(YTORRENT_CONFIG.download_folder_path, startswith=True)
disk.create_a_folder(disk.get_directory_path(YTORRENT_CONFIG.download_folder_path))

YTORRENT_CONFIG.tracker_ip_or_url_list = [one for one in YTORRENT_CONFIG.tracker_ip_or_url_list if one.strip()!=""]
YTORRENT_CONFIG.tracker_ip_or_url_list = list(set(YTORRENT_CONFIG.tracker_ip_or_url_list))
print(YTORRENT_CONFIG.tracker_ip_or_url_list)


def refactor_database():
    database_excutor_for_remote_service.A_Resource.database_of_yingshaoxo.refactor_database()
    database_excutor_for_remote_service.Ytorrent_Config.database_of_yingshaoxo.refactor_database()
    database_excutor_for_remote_service.Need_To_Upload_Notification.database_of_yingshaoxo.refactor_database()
    database_excutor_for_remote_service.File_Segment.database_of_yingshaoxo.refactor_database()

    database_excutor_for_local_service.A_Resource.database_of_yingshaoxo.refactor_database()
    database_excutor_for_local_service.Ytorrent_Config.database_of_yingshaoxo.refactor_database()
    database_excutor_for_local_service.Need_To_Upload_Notification.database_of_yingshaoxo.refactor_database()
    database_excutor_for_local_service.File_Segment.database_of_yingshaoxo.refactor_database()


class Ytorrent_Remote_Service(ytorrent_server_and_client_protocol_pure_python_rpc.Service_ytorrent_server_and_client_protocol):
    def seed(self, headers: dict[str, str], item: ytorrent_objects.Seed_Request) -> ytorrent_objects.Seed_Response:
        default_response = ytorrent_objects.Seed_Response()

        resource_search_result_list = database_excutor_for_remote_service.A_Resource.search(item_filter=ytorrent_objects.A_Resource(
            file_or_folder_hash=item.a_resource.file_or_folder_hash
        ))
        if len(resource_search_result_list) == 0:
            database_excutor_for_remote_service.A_Resource.add(item=item.a_resource)

        try:
            start_time = time_.get_datetime_object_from_timestamp(time_.get_current_timestamp_in_10_digits_format())
            # check if there has any user wanted to download a file or folder this seeder provides
            # if so, return the download request
            # this check should let the user wait for 60 seconds
            while True:
                # check if someone wants to download something
                need_to_upload_list = database_excutor_for_remote_service.Need_To_Upload_Notification.search(item_filter=
                    ytorrent_objects.Need_To_Upload_Notification(file_or_folder_hash=item.a_resource.file_or_folder_hash)
                )
                if len(need_to_upload_list) > 0:
                    # someone needs to download a file or folder
                    # if that file segment is not in server, we ask the seeder to upload
                    real_need_list = []
                    for one in need_to_upload_list:
                        segment_filter = ytorrent_objects.File_Segment(
                                file_or_folder_hash=one.file_or_folder_hash,
                                file_path_relative_to_root_folder=one.file_path_relative_to_root_folder,
                                file_segment_size_in_bytes=one.file_segment_size_in_bytes,
                                segment_number=one.segment_number
                            )
                        file_segment_list = database_excutor_for_remote_service.File_Segment.search(item_filter=
                            segment_filter
                        )
                        if len(file_segment_list) == 0:
                            real_need_list.append(one)

                    default_response.need_to_upload_notification_list = real_need_list
                    default_response.someone_needs_you_to_upload_your_file = True
                    default_response.success = True
                    return default_response

                current_time = time_.get_datetime_object_from_timestamp(time_.get_current_timestamp_in_10_digits_format())
                if ((current_time - start_time).seconds >= 60):
                    # it is just a normal timeout, the user should make another seed request immediatly
                    default_response.need_to_upload_notification_list = []
                    default_response.someone_needs_you_to_upload_your_file = False
                    default_response.success = True
                    return default_response
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def search(self, headers: dict[str, str], item: ytorrent_objects.Search_Request) -> ytorrent_objects.Search_Response:
        default_response = ytorrent_objects.Search_Response()

        try:
            def a_handler(raw_json_text: str) -> dict[str, Any] | None:
                search_text = item.search_input
                json_object = json.loads(raw_json_text)
                if search_text.lower() in json_object["name"].lower():
                    return json_object
                return None
            resource_search_result_list = database_excutor_for_remote_service.A_Resource.raw_search(one_row_json_string_handler=a_handler, page_number=item.page_number, page_size=item.page_size)
            #resource_search_result_list = database_excutor_for_remote_service.A_Resource.search(item_filter=ytorrent_objects.A_Resource(
            #    name=item.search_input
            #))
            default_response.resource_list = resource_search_result_list
        except Exception as e:
            print(f"Error: {e}")
            default_response.error = str(e)
            #default_response.success = False

        return default_response

    def download_resource_info(self, headers: dict[str, str], item: ytorrent_objects.Download_Resource_Info_Request) -> ytorrent_objects.Download_Resource_Info_Response:
        default_response = ytorrent_objects.Download_Resource_Info_Response()

        try:
            resource_search_result_list = database_excutor_for_remote_service.A_Resource.search(item_filter=ytorrent_objects.A_Resource(
                file_or_folder_hash=item.file_or_folder_hash
            ))
            if len(resource_search_result_list) > 0:
                default_response.a_resource = resource_search_result_list[0]
                default_response.try_it_later_when_other_need_to_upload = False
            else:
                default_response.try_it_later_when_other_need_to_upload = True
                default_response.error = "No such file segment yet, others needs to upload it."
        except Exception as e:
            print(f"Error: {e}")
            default_response.error = str(e)
            #default_response.success = False

        return default_response

    def download(self, headers: dict[str, str], item: ytorrent_objects.Download_Request) -> ytorrent_objects.Download_Response:
        default_response = ytorrent_objects.Download_Response()

        try:
            start_time = time_.get_datetime_object_from_timestamp(time_.get_current_timestamp_in_10_digits_format())
            # check if there has an upload matchs user needs
            # if so, return that upload 
            # this check should let the user wait for 60 seconds
            while True:
                segment_filter = ytorrent_objects.File_Segment(
                        file_or_folder_hash=item.need_to_upload_notification.file_or_folder_hash,
                        file_path_relative_to_root_folder=item.need_to_upload_notification.file_path_relative_to_root_folder,
                        file_segment_size_in_bytes=item.need_to_upload_notification.file_segment_size_in_bytes,
                        segment_number=item.need_to_upload_notification.segment_number
                    )
                file_segment_list = database_excutor_for_remote_service.File_Segment.search(item_filter=
                    segment_filter
                )
                if len(file_segment_list) > 0:
                    file_segment = file_segment_list[0]
                    default_response.file_segment_bytes_in_base64 = file_segment.file_segment_bytes_in_base64
                    default_response.try_it_later_when_other_need_to_upload = False

                    database_excutor_for_remote_service.File_Segment.delete(segment_filter)
                    database_excutor_for_remote_service.Need_To_Upload_Notification.delete(item_filter=
                        ytorrent_objects.Need_To_Upload_Notification(file_or_folder_hash=item.need_to_upload_notification.file_or_folder_hash)
                    )

                    return default_response
                else:
                    # ask someone to upload if there has no exists file segments
                    need_to_upload_list = database_excutor_for_remote_service.Need_To_Upload_Notification.search(item_filter=
                        item.need_to_upload_notification
                    )
                    if len(need_to_upload_list) == 0:
                        database_excutor_for_remote_service.Need_To_Upload_Notification.add(item.need_to_upload_notification)

                current_time = time_.get_datetime_object_from_timestamp(time_.get_current_timestamp_in_10_digits_format())
                if ((current_time - start_time).seconds >= 60):
                    # it is just a normal timeout, the user should make another seed request immediatly
                    default_response.try_it_later_when_other_need_to_upload = True
                    return default_response
        except Exception as e:
            print(f"Error: {e}")
            default_response.error = str(e)
            #default_response.success = False

        return default_response

    def upload(self, headers: dict[str, str], item: ytorrent_objects.Upload_Request) -> ytorrent_objects.Upload_Response:
        default_response = ytorrent_objects.Upload_Response()

        try:
            file_segment_list = database_excutor_for_remote_service.File_Segment.search(item_filter=
                ytorrent_objects.File_Segment(
                    file_or_folder_hash=item.need_to_upload_notification.file_or_folder_hash,
                    file_path_relative_to_root_folder=item.need_to_upload_notification.file_path_relative_to_root_folder,
                    file_segment_size_in_bytes=item.need_to_upload_notification.file_segment_size_in_bytes,
                    segment_number=item.need_to_upload_notification.segment_number
                )
            )
            if len(file_segment_list) == 0:
                database_excutor_for_remote_service.File_Segment.add(item=ytorrent_objects.File_Segment(
                    file_or_folder_hash=item.need_to_upload_notification.file_or_folder_hash,
                    file_path_relative_to_root_folder=item.need_to_upload_notification.file_path_relative_to_root_folder,
                    file_segment_size_in_bytes=item.need_to_upload_notification.file_segment_size_in_bytes,
                    segment_number=item.need_to_upload_notification.segment_number,
                    file_segment_bytes_in_base64=item.file_segment_bytes_in_base64,
                    _current_time_in_timestamp=time_.get_current_timestamp_in_10_digits_format()
                ))
            default_response.success = True
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def get_shared_tracker_list(self, headers: dict[str, str], item: ytorrent_objects.Get_Shared_Tracker_List_Request) -> ytorrent_objects.Get_Shared_Tracker_List_Response:
        default_response = ytorrent_objects.Get_Shared_Tracker_List_Response()

        try:
            # You have to make YTORRENT_CONFIG a dynamic class, which means no matter I change it from where, multiprocess or threading, the change will across all places where used it. Similar to vue reactive() object, or proxy dict, or proxy class
            default_response.tracker_ip_list = YTORRENT_CONFIG.tracker_ip_or_url_list
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def version(self, headers: dict[str, str], item: ytorrent_objects.Version_Request) -> ytorrent_objects.Version_Response:
        default_response = ytorrent_objects.Version_Response()

        try:
            default_response.name = "ytorrent"
            default_response.version_code = 1
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response


def run_remote_yrpc_service(port: str):
    service_instance = Ytorrent_Remote_Service()
    ytorrent_server_and_client_protocol_pure_python_rpc.run(service_instance, port=port)


class Ytorrent_Local_Service(ytorrent_server_and_client_protocol_pure_python_rpc.Service_ytorrent_server_and_client_protocol):
    def seed(self, headers: dict[str, str], item: ytorrent_objects.Seed_Request) -> ytorrent_objects.Seed_Response:
        default_response = ytorrent_objects.Seed_Response()

        try:
            start_time = time_.get_datetime_object_from_timestamp(time_.get_current_timestamp_in_10_digits_format())
            # check if there has any user wanted to download a file or folder this seeder provides
            # if so, return the download request
            # this check should be in a while loop, we'll check it for every 1 second
            """
                current_time = time_.get_datetime_object_from_timestamp(time_.get_current_timestamp_in_10_digits_format())
                if ((current_time - start_time).seconds >= 60):
                    # it is just a normal timeout, the user should make another seed request immediatly
                    default_response.success = True
                    return default_response
            """
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def search(self, headers: dict[str, str], item: ytorrent_objects.Search_Request) -> ytorrent_objects.Search_Response:
        default_response = ytorrent_objects.Search_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def download(self, headers: dict[str, str], item: ytorrent_objects.Download_Request) -> ytorrent_objects.Download_Response:
        default_response = ytorrent_objects.Download_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def upload(self, headers: dict[str, str], item: ytorrent_objects.Upload_Request) -> ytorrent_objects.Upload_Response:
        default_response = ytorrent_objects.Upload_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def version(self, headers: dict[str, str], item: ytorrent_objects.Version_Request) -> ytorrent_objects.Version_Response:
        default_response = ytorrent_objects.Version_Response()

        try:
            default_response.name = "ytorrent"
            default_response.version_code = 1
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response


def run_local_yrpc_service(port: str):
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        #print('running in a PyInstaller bundle')
        def resource_path(relative_path: str) -> str:
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path) #type: ignore
            return os.path.join(os.path.abspath("."), relative_path)
        vue_html_file_folder = resource_path("./vue")
    else:
        #print('running in a normal Python process')
        vue_html_file_folder = disk.join_paths(disk.get_directory_path(__file__), "./vue")

    disk.create_a_folder(vue_html_file_folder)

    service_instance = Ytorrent_Local_Service()
    ytorrent_server_and_client_protocol_pure_python_rpc.run(service_instance, port=port, html_folder_path=vue_html_file_folder)


def get_remote_client_list(addtional_tracker_list: list[str] = []) -> list[ytorrent_server_and_client_protocol_pure_python_rpc_client.Client_ytorrent_server_and_client_protocol]:
    remote_service_address_list = list(set(YTORRENT_CONFIG.tracker_ip_or_url_list))
    remote_service_address_list = addtional_tracker_list + remote_service_address_list
    client_list = []
    for an_address in remote_service_address_list:
        remote_client = ytorrent_server_and_client_protocol_pure_python_rpc_client.Client_ytorrent_server_and_client_protocol(service_url=an_address)
        client_list.append(remote_client)
    return client_list

def local_background_seeding_process():
    # this should be a single while loop, which does everything that needs to work for every x seconds
    project_root_folder = disk.get_directory_path(os.path.realpath(os.path.abspath(__file__)))

    remote_service_address = f"http://127.0.0.1:{YTORRENT_CONFIG.default_remote_service_port}"
    local_service_address = f"http://127.0.0.1:{YTORRENT_CONFIG.default_local_service_port}"

    client_list = get_remote_client_list()

    def do_the_seeding_based_on_local_database_data():
        resouce_list = database_excutor_for_local_service.A_Resource.search(item_filter=ytorrent_objects.A_Resource(
            download_complete=True
        ))
        for a_resource in resouce_list:
            seed_request = ytorrent_objects.Seed_Request(a_resource=a_resource)
            for client in client_list:
                try:
                    seed_response = client.seed(seed_request)
                    if seed_response.error != None:
                        print(seed_response.error)
                        continue
                    else:
                        print(seed_response)
                        if seed_response.someone_needs_you_to_upload_your_file == False:
                            continue
                        else:
                            if seed_response.need_to_upload_notification_list == None:
                                continue
                            for need_to_upload_notification in seed_response.need_to_upload_notification_list:
                                file_hash = need_to_upload_notification.file_or_folder_hash
                                target_resource_list = [one for one in resouce_list if one.file_or_folder_hash == file_hash]
                                if len(target_resource_list) == 0:
                                    continue
                                else:
                                    target_resource = target_resource_list[0]
                                    target_project_path = disk.join_paths(target_resource.root_folder, target_resource.name)
                                    target_file_path = disk.join_paths(target_resource.root_folder, need_to_upload_notification.file_path_relative_to_root_folder)
                                    target_file_path = terminal.fix_path(target_file_path, startswith=True)
                                    #print(target_resource.root_folder, need_to_upload_notification.file_path_relative_to_root_folder)
                                    if not disk.exists(target_project_path):
                                        database_excutor_for_local_service.A_Resource.delete(item_filter=ytorrent_objects.A_Resource(file_or_folder_hash=target_resource.file_or_folder_hash))
                                        continue
                                    if not disk.exists(target_file_path):
                                        continue

                                    bytesio_data = disk.get_part_of_a_file_in_bytesio_format_from_a_file(target_file_path, need_to_upload_notification.file_segment_size_in_bytes, need_to_upload_notification.segment_number)
                                    base64_data = disk.bytesio_to_base64(bytesio_data)
                                    upload_request = ytorrent_objects.Upload_Request(
                                        need_to_upload_notification=need_to_upload_notification,
                                        file_segment_bytes_in_base64=base64_data,
                                    )
                                    upload_response = client.upload(upload_request)
                                    print()
                                    print("Upload for ", need_to_upload_notification.file_path_relative_to_root_folder, need_to_upload_notification.segment_number, upload_response.success)
                except Exception as e:
                    print(e)

    while True:
        try:
            do_the_seeding_based_on_local_database_data()
        except Exception as e:
            print(e)
        sleep(1)


def local_background_download_process():
    # this should be a single while loop, which does everything that needs to work for every x seconds
    project_root_folder = disk.get_directory_path(os.path.realpath(os.path.abspath(__file__)))

    remote_service_address = f"http://127.0.0.1:{YTORRENT_CONFIG.default_remote_service_port}"
    local_service_address = f"http://127.0.0.1:{YTORRENT_CONFIG.default_local_service_port}"

    client_list = get_remote_client_list()

    def download_a_file_segment(empty_file_segment: ytorrent_objects.File_Segment) -> str | None:
        download_request = ytorrent_objects.Download_Request(
            need_to_upload_notification=ytorrent_objects.Need_To_Upload_Notification(
                file_or_folder_hash=empty_file_segment.file_or_folder_hash,
                file_path_relative_to_root_folder=empty_file_segment.file_path_relative_to_root_folder,
                file_segment_size_in_bytes=empty_file_segment.file_segment_size_in_bytes,
                segment_number=empty_file_segment.segment_number
            )
        )
        if YTORRENT_CONFIG.exposed_seeder_tracker_address != None:
            # get file from original file hoster
            clients = get_remote_client_list(addtional_tracker_list=[YTORRENT_CONFIG.exposed_seeder_tracker_address])
        else:
            clients = get_remote_client_list()
        for client in clients:
            response = client.download(download_request)
            if response.error != None:
                print(response.error)
                continue
            else:
                return response.file_segment_bytes_in_base64
        return None

    def mark_one_resource_download_success(a_resource: ytorrent_objects.A_Resource):
        if a_resource.exposed_seeder_tracker_address != None:
            YTORRENT_CONFIG.tracker_ip_or_url_list += [a_resource.exposed_seeder_tracker_address]
        database_excutor_for_local_service.A_Resource.update(
            old_item_filter=ytorrent_objects.A_Resource(file_or_folder_hash=a_resource.file_or_folder_hash),
            new_item=ytorrent_objects.A_Resource(download_complete=True, exposed_seeder_tracker_address=YTORRENT_CONFIG.exposed_seeder_tracker_address)
        )

    def mark_one_file_download_success(a_whole_file: ytorrent_objects.A_Whole_File, a_resource: ytorrent_objects.A_Resource):
        #print(len(a_resource.file_hash_list), len(set(a_resource.file_hash_list)))
        target_index = a_resource.file_hash_list.index(a_whole_file.file_hash)
        a_resource.file_download_status_list[target_index] = True
        database_excutor_for_local_service.A_Resource.update(
            old_item_filter=ytorrent_objects.A_Resource(file_or_folder_hash=a_resource.file_or_folder_hash),
            new_item=ytorrent_objects.A_Resource(file_download_status_list=a_resource.file_download_status_list)
        )
        print(f"Download complete marked")
        print()

    def export_a_whole_file_to_disk(a_whole_file: ytorrent_objects.A_Whole_File) -> bool:
        if a_whole_file.root_folder == None:
            download_folder = YTORRENT_CONFIG.download_folder_path
        else:
            download_folder = a_whole_file.root_folder

        target_path = disk.join_paths(download_folder, a_whole_file.file_name)
        target_path = terminal.fix_path(target_path, startswith=True)
        target_path = disk.get_absolute_path(target_path)
        target_folder = disk.get_directory_path(target_path)
        disk.create_a_folder(target_folder)
        print(target_path)

        target_hash = a_whole_file.file_hash[len(a_whole_file.file_name):]

        if disk.exists(target_path):
            real_hash = disk.get_hash_of_a_file_by_using_sha1(target_path)
            if real_hash == target_hash:
                return True
            else:
                disk.delete_a_file(target_path)

        for segment in a_whole_file.file_segment_list:
            part_data = disk.base64_to_bytes(segment.file_segment_bytes_in_base64)
            with open(target_path, "ab") as f:
                f.write(part_data)

        real_hash = disk.get_hash_of_a_file_by_using_sha1(target_path)
        if (real_hash == target_hash):
            print("Hash code matchs")
            return True
        else:
            print("Hash code match failed, delele it anddownload it again")
            print()
            return False

    def do_the_downloading_based_on_local_database_data():
        a_search_result_list = database_excutor_for_local_service.A_Resource.search(item_filter=ytorrent_objects.A_Resource(
            download_complete=False
        ))

        if (len(a_search_result_list) == 0):
            return
        else:
            for a_resource in a_search_result_list:
                # you may check if all files get downloaded successfully or not, if success, set download_complete flag to A_Resource
                for client in client_list:
                    if a_resource.file_download_status_list == None:
                        # You need to download Resource from network
                        # download the resource, then update a_resource in database to complete details
                        response = client.download_resource_info(ytorrent_objects.Download_Resource_Info_Request(
                            file_or_folder_hash=a_resource.file_or_folder_hash
                        ))
                        if response.error != None:
                            print(response.error)
                        else:
                            if response.a_resource != None:
                                response.a_resource.download_complete = False
                                response.a_resource.root_folder = YTORRENT_CONFIG.download_folder_path
                                response.a_resource.file_download_status_list = [False for one in response.a_resource.file_path_list_relative_to_root_folder]
                                database_excutor_for_local_service.A_Resource.update(
                                    old_item_filter=ytorrent_objects.A_Resource(
                                        file_or_folder_hash=a_resource.file_or_folder_hash
                                    ),
                                    new_item=response.a_resource
                                )
                                continue
                    else:
                        print(a_resource)
                        if all(a_resource.file_download_status_list):
                            for a_folder in a_resource.folder_path_list_relative_to_root_folder:
                                disk.create_a_folder(disk.join_paths(a_resource.root_folder, a_folder))
                            mark_one_resource_download_success(a_resource)
                            continue

                        # download that files by iterate files, then create a_whole_file, then create file_segments 
                        for index, a_file in enumerate(a_resource.file_path_list_relative_to_root_folder):
                            download_complete = a_resource.file_download_status_list[index]
                            file_hash = a_resource.file_hash_list[index]
                            file_size = a_resource.file_size_in_bytes_list[index]
                            if download_complete == True:
                                continue

                            a_whole_file = ytorrent_objects.A_Whole_File(
                                file_hash=file_hash,
                                root_folder=a_resource.root_folder,
                                file_name=a_file,
                                file_segment_list=[]
                            )

                            # if there already has a file, continue if it is right one, delete it if it is wrong one
                            if a_whole_file.root_folder == None:
                                download_folder = YTORRENT_CONFIG.download_folder_path
                            else:
                                download_folder = a_whole_file.root_folder
                            target_path = disk.join_paths(download_folder, a_whole_file.file_name)
                            target_path = terminal.fix_path(target_path, startswith=True)
                            target_path = disk.get_absolute_path(target_path)
                            target_folder = disk.get_directory_path(target_path)
                            disk.create_a_folder(target_folder)

                            target_hash = a_whole_file.file_hash[len(a_whole_file.file_name):]

                            if disk.exists(target_path):
                                real_hash = disk.get_hash_of_a_file_by_using_sha1(target_path)
                                if real_hash == target_hash:
                                    mark_one_file_download_success(a_whole_file, a_resource)
                                    continue
                                else:
                                    disk.delete_a_file(target_path)

                            # if there does not have a file
                            max_acceptable_file_segment_size_in_bytes = YTORRENT_CONFIG.max_acceptable_file_segment_size_in_mb * 1024 * 1024
                            segments_number = file_size // max_acceptable_file_segment_size_in_bytes
                            if (file_size % max_acceptable_file_segment_size_in_bytes) != 0:
                                segments_number += 1
                            file_segment_list = []
                            for i in range(segments_number):
                                a_file_segment = ytorrent_objects.File_Segment(
                                    file_or_folder_hash=a_resource.file_or_folder_hash,
                                    file_path_relative_to_root_folder=a_file,
                                    file_segment_size_in_bytes=max_acceptable_file_segment_size_in_bytes,
                                    segment_number=i+1,
                                    file_segment_bytes_in_base64=None,
                                    _current_time_in_timestamp=time_.get_current_timestamp_in_10_digits_format()
                                )
                                print(a_file_segment)
                                while True:
                                    a_file_segment.file_segment_bytes_in_base64 = download_a_file_segment(a_file_segment)
                                    if a_file_segment.file_segment_bytes_in_base64 != None:
                                        print("Segment downloaded.")
                                        break
                                file_segment_list.append(a_file_segment)

                            a_whole_file.file_segment_list = file_segment_list

                            success = export_a_whole_file_to_disk(a_whole_file)
                            if success == True:
                                mark_one_file_download_success(a_whole_file, a_resource)
                            else:
                                continue

    while True:
        try:
            do_the_downloading_based_on_local_database_data()
        except Exception as e:
            print(e)
        sleep(3)


def remote_background_delete_file_segments_process():
    # this should be a single while loop, which does everything that needs to work for every x seconds
    project_root_folder = disk.get_directory_path(os.path.realpath(os.path.abspath(__file__)))

    def do_the_deletion_if_it_reachs_limitation():
        file_segment_list = database_excutor_for_remote_service.File_Segment.search(item_filter=
            ytorrent_objects.File_Segment()
        )
        pool_size_in_mb = 0
        for one_file in file_segment_list:
            if one_file.file_segment_size_in_bytes != None:
                one_file_size = int(one_file.file_segment_size_in_bytes / 1024 / 1024)
                pool_size_in_mb += one_file_size
        if pool_size_in_mb >= YTORRENT_CONFIG.file_segments_memory_pool_size_in_mb:
            the_oldest_timestamp = float("inf")
            the_one = None
            for one_file in file_segment_list:
                if one_file._current_time_in_timestamp != None:
                    if one_file._current_time_in_timestamp < the_oldest_timestamp:
                        the_oldest_timestamp = one_file._current_time_in_timestamp
                        the_one = one_file
            if the_one != None:
                database_excutor_for_remote_service.File_Segment.delete(item_filter=
                    ytorrent_objects.File_Segment(
                        _current_time_in_timestamp=the_one._current_time_in_timestamp
                    )
                )

    while True:
        try:
            do_the_deletion_if_it_reachs_limitation()
        except Exception as e:
            print(e)
        sleep(3)


def start_all_service():
    process_list = [
        multiprocessing.Process(target=run_remote_yrpc_service, args=("1111",)),
        multiprocessing.Process(target=run_local_yrpc_service, args=("1212",)),
        multiprocessing.Process(target=local_background_seeding_process, args=()),
        multiprocessing.Process(target=local_background_download_process, args=()),
        multiprocessing.Process(target=remote_background_delete_file_segments_process, args=()),
    ]

    def kill_all_process():
        for process in process_list:
            if process.is_alive():
                process.terminate()

    try:
        for process in process_list:
            process.start()

        while all([
            one.is_alive()
            for one in process_list
        ]):
            sleep(3)
            if core_store.get("stop_signal", False) == True:
                kill_all_process()
    except Exception as e:
        print(e)

    # If one of them get killed, kill them all
    kill_all_process()
    core_store.set("stop_signal", False)


class Ytorrent_Client():
    def __init__(self):
        self.project_root_folder = disk.get_directory_path(os.path.realpath(os.path.abspath(__file__)))

        self.remote_service_address = f"http://127.0.0.1:{YTORRENT_CONFIG.default_remote_service_port}"
        self.local_service_address = f"http://127.0.0.1:{YTORRENT_CONFIG.default_local_service_port}"
        # local service in port 1212 should not get exposed to public network

        self.remote_service_address_list = list(set(YTORRENT_CONFIG.tracker_ip_or_url_list))

        self.remote_client = ytorrent_server_and_client_protocol_pure_python_rpc_client.Client_ytorrent_server_and_client_protocol(service_url=self.remote_service_address)
        self.local_client = ytorrent_server_and_client_protocol_pure_python_rpc_client.Client_ytorrent_server_and_client_protocol(service_url=self.local_service_address)

        try:
            response = self.remote_client.version(ytorrent_objects.Version_Request())
            if response.name == "ytorrent":
                # the remote service is on
                pass
            else:
                raise Exception(f"The remote ytorrent service is not runing in {self.remote_service_address}")

            response = self.local_client.version(ytorrent_objects.Version_Request())
            if response.name == "ytorrent":
                # the local service is on
                pass
            else:
                raise Exception(f"The local ytorrent service is not runing in {self.local_service_address}")
        except Exception as e:
            print(e)
            print("\n\n_______________\n\n")
            print(f"We'll launch a tracker service at {self.remote_service_address}")
            print(f"We'll launch a user interface service at {self.local_service_address}")
            print(f"> You have to disable some DNS service 'Browser Integrity Check' to allow python http client to access your API service.")
            print("\n\n_______________\n\n")
            print(f"Please open another shell/bash tab to execute your command again.")
            print()
            start_all_service()
            exit()

    def seed(self, file_or_folder_path: str):
        # seed this file, put it into database, do not allow user to seed the same resource twice
        def get_child_relative_path(parent_path, child_path):
            return child_path[len(parent_path):].lstrip("/")

        file_or_folder_path = disk.get_absolute_path(file_or_folder_path)

        if not disk.exists(file_or_folder_path):
            raise Exception(f"The file you want to seed is not exists: {file_or_folder_path}")

        root_folder = disk.get_parent_directory_path(file_or_folder_path)
        root_folder = disk.get_absolute_path(root_folder)

        name = disk.get_file_name(file_or_folder_path)
        is_single_file = (not disk.is_directory(file_or_folder_path))

        #print(root_folder, name)

        file_or_folder_hash = None
        file_or_folder_size_in_bytes = None
        if (is_single_file):
            file_or_folder_hash = disk.get_hash_of_a_file_by_using_sha1(file_or_folder_path)
            file_or_folder_size_in_bytes = disk.get_file_size(file_or_folder_path)
        else:
            file_or_folder_hash = disk.get_hash_of_a_folder(file_or_folder_path, print_log=True)
            file_or_folder_size_in_bytes = disk.get_folder_size(file_or_folder_path)

        #print(file_or_folder_hash)
        #print(file_or_folder_size_in_bytes)

        folder_path_list_relative_to_root_folder = []
        file_path_list_relative_to_root_folder = []
        file_path_content_hash_list = []
        file_size_in_bytes_list = []
        if is_single_file == True:
            part_of_file_or_folder_path = get_child_relative_path(root_folder, file_or_folder_path)
            file_path_list_relative_to_root_folder.append(part_of_file_or_folder_path)
            file_path_content_hash_list.append(part_of_file_or_folder_path + disk.get_hash_of_a_file_by_using_sha1(file_or_folder_path))
            file_size_in_bytes_list.append(disk.get_file_size(file_or_folder_path))
        else:
            files = disk.get_folder_and_files_with_gitignore(folder=file_or_folder_path, return_list_than_tree=True)
            files = [one.path for one in files]
            files.sort()
            #files = disk.get_files(file_or_folder_path)
            for file in files:
                part_of_file_or_folder_path = get_child_relative_path(root_folder, file)
                if disk.is_directory(file):
                    folder_path_list_relative_to_root_folder.append(part_of_file_or_folder_path)
                else:
                    file_path_list_relative_to_root_folder.append(part_of_file_or_folder_path)
                    file_path_content_hash_list.append(part_of_file_or_folder_path + disk.get_hash_of_a_file_by_using_sha1(file))
                    # since there may have duplicate same files inside of a folder, that's why I add 'relative path' into hash code to make it unique
                    file_size_in_bytes_list.append(disk.get_file_size(file))

        a_resource = ytorrent_objects.A_Resource(
            name=name,
            is_single_file=is_single_file,
            file_or_folder_hash=file_or_folder_hash,
            file_or_folder_size_in_bytes=str(file_or_folder_size_in_bytes),
            root_folder=root_folder,
            folder_path_list_relative_to_root_folder=folder_path_list_relative_to_root_folder,
            file_path_list_relative_to_root_folder=file_path_list_relative_to_root_folder,
            file_size_in_bytes_list=file_size_in_bytes_list,
            file_hash_list=file_path_content_hash_list,
            file_download_status_list=[True for one in file_path_content_hash_list],
            download_complete=True,
            exposed_seeder_tracker_address=YTORRENT_CONFIG.exposed_seeder_tracker_address,
        )

        a_search_result_list = database_excutor_for_local_service.A_Resource.search(item_filter=ytorrent_objects.A_Resource(
            name=a_resource.name,
            root_folder=a_resource.root_folder
        ))
        if (len(a_search_result_list) == 0):
            database_excutor_for_local_service.A_Resource.add(item=a_resource)
        else:
            raise Exception(f"The file/folder you want to seed is already in seeding: {file_or_folder_path}")

        print(a_resource)
        print(f"This file is in seeding now: {file_or_folder_path}")

    def search(self, keywords: str):
        client_list = get_remote_client_list()

        def page_seperation(page_size:int, current_page:int):
            import urllib.parse
            search_request = ytorrent_objects.Search_Request(
                search_input = keywords.strip(),
                page_size = page_size,
                page_number = current_page
            )
            for client in client_list:
                search_response = client.search(search_request)
                if search_response.error != None:
                    print(search_response.error)
                    continue
                else:
                    final_result = []
                    if search_response.resource_list == None:
                        continue
                    for one in search_response.resource_list:
                        name = one.name.replace("|", "")
                        if len(name)>30:
                            name = name[:15] + "..." + name[-15:]
                        safe_name = urllib.parse.quote_plus(name)
                        file_size = disk.get_file_size(None, "MB", int(one.file_or_folder_size_in_bytes))
                        hash_code = one.file_or_folder_hash
                        final_result.append((f"{name} ({file_size}MB) | magnet_magic:?xt={hash_code}&dn={safe_name[:10]}&tr={client._service_url}", None))
                    return final_result
            return []
        return page_seperation
        # do search on the network, here the network is our database, has to have page seperation, for each resource, you should give user a certain magnet link like: magnet_magic:?xt=xxx

    def download(self, magic_magnet_link: str):
        # magnet_magic:?xt=c32c6c252901fc7afaa755015993e29a63e644ec397aa31d65536959dcfedf12&tr=http://192.168.49.111:1111
        hash_code = magic_magnet_link.split("?xt=")[1].split("&")[0]
        tracker_ip_list = []
        splits = magic_magnet_link.split("&tr=")
        for one in splits:
            if one.startswith("http"):
                tracker_ip_list.append(one)
        # need to find a way to share new tracker_ip_list to Ytorrent_Config, one possible way is to use auto_everything store to save that config as a json object, then whenever it get changed, update that config object in memory

        # need to create a list of Need_To_Upload_Notification in database, so the background process will download it one by one
        a_resource = ytorrent_objects.A_Resource(
            file_or_folder_hash=hash_code,
            download_complete=False
        )
        result_list = database_excutor_for_local_service.A_Resource.search(item_filter=ytorrent_objects.A_Resource(
            file_or_folder_hash=hash_code,
        ))
        if (len(result_list) == 0):
            a_resource.root_folder = YTORRENT_CONFIG.download_folder_path
            database_excutor_for_local_service.A_Resource.add(item=a_resource)
            print("The download is started.")
            print(f"You may found it later at: {a_resource.root_folder}")
        else:
            one = result_list[0]
            if one.download_complete == True:
                target_path = disk.join_paths(one.root_folder, one.name)
                target_path = terminal.fix_path(target_path, startswith=True)
                print(target_path)
                if not disk.exists(target_path):
                    database_excutor_for_local_service.A_Resource.delete(ytorrent_objects.A_Resource(
                        file_or_folder_hash=hash_code,
                    ))
                    self.download(magic_magnet_link)
                else:
                    raise Exception(f"The file/folder you want to download is already complete: {magic_magnet_link}\nYou can found it at {target_path}")
            else:
                raise Exception(f"The file/folder you want to download is already in downloading: {magic_magnet_link}\nYou can found it at {one.root_folder}")

    def stop(self):
        """
        Stop all service that related magic magnet software.
        """
        core_store.set("stop_signal", True)
        print("In quiting...")
        sleep(4)
        print("Quit successfully")


class Command_Line_Interface():
    def __init__(self) -> None:
        self.ytorrent_client = Ytorrent_Client()

    def seed(self, file_or_folder_path: str):
        self.ytorrent_client.seed(file_or_folder_path)

    def search(self, keywords: str):
        page_seperation_function = self.ytorrent_client.search(keywords)
        result = terminal_user_interface.selection_box(text="Please select one:", selections=[], seperate_page_loading_function=page_seperation_function)
        print()
        splits = result.split(" | ")
        print(splits[1])

    def download(self, magic_magnet_link: str):
        self.ytorrent_client.download(magic_magnet_link)

    def stop(self):
        """
        Stop all service that related to magic magnet software.
        """
        self.ytorrent_client.stop()

    def version(self):
        print("Magic Magnet v1. (author yingshaoxo)")


if __name__ == '__main__':
    refactor_database()
    python.fire(Command_Line_Interface)

