from typing import Callable

from .ytorrent_server_and_client_protocol_objects import *
from auto_everything.database import Database_Of_Yingshaoxo


def _search_function(self: Any, item_filter: Any, page_number:int|None=None, page_size:int|None=None, start_from:int=0, reverse:bool=False) -> list[dict[str, Any]]:
    search_temp_dict = {}
    search_temp_dict["_raw_search_counting"] = 0
    search_temp_dict["_search_counting"] = 0
    if (page_number!=None and page_size != None and start_from != None):
        search_temp_dict["_real_start"] = page_number * page_size
        search_temp_dict["_real_end"] = search_temp_dict["_real_start"] + page_size

    item_dict = item_filter.to_dict()

    def one_row_dict_filter(a_dict_: dict[str, Any]):
        search_temp_dict["_raw_search_counting"] += 1

        if (page_number!=None and page_size != None and start_from != None):
            if search_temp_dict["_raw_search_counting"] < start_from:
                return None

        result = True
        for key, value in item_dict.items():
            if value == None:
                # ignore None value because it is not defined
                continue
            if key not in a_dict_.keys():
                result = False
                break
            else:
                value2 = a_dict_.get(key)
                if value == value2:
                    continue
                else:
                    result = False
                    break

        final_result = None
        if result == True:
            search_temp_dict["_search_counting"] += 1
            final_result = a_dict_
        else:
            final_result = None

        if (page_number!=None and page_size != None and start_from != None):
            if search_temp_dict["_search_counting"] <= search_temp_dict["_real_start"]:
                return None
            if search_temp_dict["_search_counting"] > search_temp_dict["_real_end"]:
                return None

        return final_result

    return self.database_of_yingshaoxo.search(one_row_dict_handler=one_row_dict_filter)


def _raw_search_function(self: Any, one_row_json_string_handler: Callable[[str], dict[str, Any] | None], page_number:int|None=None, page_size:int|None=None, start_from:int=0, reverse:bool=False):
    search_temp_dict = {}
    search_temp_dict["_raw_search_counting"] = 0
    search_temp_dict["_search_counting"] = 0
    if (page_number!=None and page_size != None and start_from != None):
        search_temp_dict["_real_start"] = page_number * page_size
        search_temp_dict["_real_end"] = search_temp_dict["_real_start"] + page_size

    def new_one_row_json_string_handler(a_json_string: str):
        search_temp_dict["_raw_search_counting"] += 1

        if (page_number!=None and page_size != None and start_from != None):
            if search_temp_dict["_raw_search_counting"] < start_from:
                return None

        result = one_row_json_string_handler(a_json_string)

        if result != None:
            search_temp_dict["_search_counting"] += 1

        if (page_number!=None and page_size != None and start_from != None):
            if search_temp_dict["_search_counting"] <= search_temp_dict["_real_start"]:
                return None
            if search_temp_dict["_search_counting"] > search_temp_dict["_real_end"]:
                return None

        return result

    return list(self.database_of_yingshaoxo.raw_search(one_row_json_string_handler=new_one_row_json_string_handler))


def _delete(self, item_filter: Any) -> None:
    item_dict = item_filter.to_dict()
    def one_row_dict_filter(a_dict_: dict[str, Any]):
        result = True
        for key, value in item_dict.items():
            if value == None:
                # ignore None value because it is not defined
                continue
            if key not in a_dict_.keys():
                result = False
                break
            else:
                value2 = a_dict_.get(key)
                if value == value2:
                    continue
                else:
                    result = False
                    break
        return result
    self.database_of_yingshaoxo.delete(one_row_dict_filter=one_row_dict_filter)


def _update(self, old_item_filter: Any, new_item: Any):
    item_dict = old_item_filter.to_dict()
    def one_row_dict_handler(a_dict_: dict[str, Any]):
        result = True
        for key, value in item_dict.items():
            if value == None:
                # ignore None value because it is not defined
                continue
            if key not in a_dict_.keys():
                result = False
                break
            else:
                value2 = a_dict_.get(key)
                if value == value2:
                    continue
                else:
                    result = False
                    break
        if result == True:
            new_object = {
                key:value for key, value
                in new_item.to_dict().items()
                if value != None
            }
            a_dict_.update(new_object)
            return a_dict_
        else:
            return None
    self.database_of_yingshaoxo.update(one_row_dict_handler=one_row_dict_handler)


class Yingshaoxo_Database_Ytorrent_Config:
    def __init__(self, database_base_folder: str, use_sqlite: bool = False, global_multiprocessing_shared_dict: Any | None = None, auto_backup: bool = False) -> None:
        self.database_of_yingshaoxo = Database_Of_Yingshaoxo(database_name="Ytorrent_Config", database_base_folder=database_base_folder, use_sqlite=use_sqlite, global_multiprocessing_shared_dict=global_multiprocessing_shared_dict, auto_backup=auto_backup)

    def add(self, item: Ytorrent_Config):
        return self.database_of_yingshaoxo.add(data=item.to_dict())

    def search(self, item_filter: Ytorrent_Config, page_number:int|None=None, page_size:int|None=None, start_from:int=0, reverse:bool=False) -> list[Ytorrent_Config]:
        return [Ytorrent_Config().from_dict(one) for one in _search_function(self=self, item_filter=item_filter, page_number=page_number, page_size=page_size, start_from=start_from, reverse=reverse)]

    def raw_search(self, one_row_json_string_handler: Callable[[str], dict[str, Any] | None], page_number:int|None=None, page_size:int|None=None, start_from:int=0, reverse:bool=False) -> list[Ytorrent_Config]:
        '''
        one_row_json_string_handler: a_function to handle search process. If it returns None, we'll ignore it, otherwise, we'll add the return value into the result list.
        '''
        return [Ytorrent_Config().from_dict(one) for one in _raw_search_function(self=self, one_row_json_string_handler=one_row_json_string_handler, page_number=page_number, page_size=page_size, start_from=start_from, reverse=reverse)]

    def delete(self, item_filter: Ytorrent_Config):
        return _delete(self=self, item_filter=item_filter)

    def update(self, old_item_filter: Ytorrent_Config, new_item: Ytorrent_Config):
        return _update(self=self, old_item_filter=old_item_filter, new_item=new_item)


class Yingshaoxo_Database_A_Resource:
    def __init__(self, database_base_folder: str, use_sqlite: bool = False, global_multiprocessing_shared_dict: Any | None = None, auto_backup: bool = False) -> None:
        self.database_of_yingshaoxo = Database_Of_Yingshaoxo(database_name="A_Resource", database_base_folder=database_base_folder, use_sqlite=use_sqlite, global_multiprocessing_shared_dict=global_multiprocessing_shared_dict, auto_backup=auto_backup)

    def add(self, item: A_Resource):
        return self.database_of_yingshaoxo.add(data=item.to_dict())

    def search(self, item_filter: A_Resource, page_number:int|None=None, page_size:int|None=None, start_from:int=0, reverse:bool=False) -> list[A_Resource]:
        return [A_Resource().from_dict(one) for one in _search_function(self=self, item_filter=item_filter, page_number=page_number, page_size=page_size, start_from=start_from, reverse=reverse)]

    def raw_search(self, one_row_json_string_handler: Callable[[str], dict[str, Any] | None], page_number:int|None=None, page_size:int|None=None, start_from:int=0, reverse:bool=False) -> list[A_Resource]:
        '''
        one_row_json_string_handler: a_function to handle search process. If it returns None, we'll ignore it, otherwise, we'll add the return value into the result list.
        '''
        return [A_Resource().from_dict(one) for one in _raw_search_function(self=self, one_row_json_string_handler=one_row_json_string_handler, page_number=page_number, page_size=page_size, start_from=start_from, reverse=reverse)]

    def delete(self, item_filter: A_Resource):
        return _delete(self=self, item_filter=item_filter)

    def update(self, old_item_filter: A_Resource, new_item: A_Resource):
        return _update(self=self, old_item_filter=old_item_filter, new_item=new_item)


class Yingshaoxo_Database_Need_To_Upload_Notification:
    def __init__(self, database_base_folder: str, use_sqlite: bool = False, global_multiprocessing_shared_dict: Any | None = None, auto_backup: bool = False) -> None:
        self.database_of_yingshaoxo = Database_Of_Yingshaoxo(database_name="Need_To_Upload_Notification", database_base_folder=database_base_folder, use_sqlite=use_sqlite, global_multiprocessing_shared_dict=global_multiprocessing_shared_dict, auto_backup=auto_backup)

    def add(self, item: Need_To_Upload_Notification):
        return self.database_of_yingshaoxo.add(data=item.to_dict())

    def search(self, item_filter: Need_To_Upload_Notification, page_number:int|None=None, page_size:int|None=None, start_from:int=0, reverse:bool=False) -> list[Need_To_Upload_Notification]:
        return [Need_To_Upload_Notification().from_dict(one) for one in _search_function(self=self, item_filter=item_filter, page_number=page_number, page_size=page_size, start_from=start_from, reverse=reverse)]

    def raw_search(self, one_row_json_string_handler: Callable[[str], dict[str, Any] | None], page_number:int|None=None, page_size:int|None=None, start_from:int=0, reverse:bool=False) -> list[Need_To_Upload_Notification]:
        '''
        one_row_json_string_handler: a_function to handle search process. If it returns None, we'll ignore it, otherwise, we'll add the return value into the result list.
        '''
        return [Need_To_Upload_Notification().from_dict(one) for one in _raw_search_function(self=self, one_row_json_string_handler=one_row_json_string_handler, page_number=page_number, page_size=page_size, start_from=start_from, reverse=reverse)]

    def delete(self, item_filter: Need_To_Upload_Notification):
        return _delete(self=self, item_filter=item_filter)

    def update(self, old_item_filter: Need_To_Upload_Notification, new_item: Need_To_Upload_Notification):
        return _update(self=self, old_item_filter=old_item_filter, new_item=new_item)


class Yingshaoxo_Database_File_Segment:
    def __init__(self, database_base_folder: str, use_sqlite: bool = False, global_multiprocessing_shared_dict: Any | None = None, auto_backup: bool = False) -> None:
        self.database_of_yingshaoxo = Database_Of_Yingshaoxo(database_name="File_Segment", database_base_folder=database_base_folder, use_sqlite=use_sqlite, global_multiprocessing_shared_dict=global_multiprocessing_shared_dict, auto_backup=auto_backup)

    def add(self, item: File_Segment):
        return self.database_of_yingshaoxo.add(data=item.to_dict())

    def search(self, item_filter: File_Segment, page_number:int|None=None, page_size:int|None=None, start_from:int=0, reverse:bool=False) -> list[File_Segment]:
        return [File_Segment().from_dict(one) for one in _search_function(self=self, item_filter=item_filter, page_number=page_number, page_size=page_size, start_from=start_from, reverse=reverse)]

    def raw_search(self, one_row_json_string_handler: Callable[[str], dict[str, Any] | None], page_number:int|None=None, page_size:int|None=None, start_from:int=0, reverse:bool=False) -> list[File_Segment]:
        '''
        one_row_json_string_handler: a_function to handle search process. If it returns None, we'll ignore it, otherwise, we'll add the return value into the result list.
        '''
        return [File_Segment().from_dict(one) for one in _raw_search_function(self=self, one_row_json_string_handler=one_row_json_string_handler, page_number=page_number, page_size=page_size, start_from=start_from, reverse=reverse)]

    def delete(self, item_filter: File_Segment):
        return _delete(self=self, item_filter=item_filter)

    def update(self, old_item_filter: File_Segment, new_item: File_Segment):
        return _update(self=self, old_item_filter=old_item_filter, new_item=new_item)


class Yingshaoxo_Database_A_Whole_File:
    def __init__(self, database_base_folder: str, use_sqlite: bool = False, global_multiprocessing_shared_dict: Any | None = None, auto_backup: bool = False) -> None:
        self.database_of_yingshaoxo = Database_Of_Yingshaoxo(database_name="A_Whole_File", database_base_folder=database_base_folder, use_sqlite=use_sqlite, global_multiprocessing_shared_dict=global_multiprocessing_shared_dict, auto_backup=auto_backup)

    def add(self, item: A_Whole_File):
        return self.database_of_yingshaoxo.add(data=item.to_dict())

    def search(self, item_filter: A_Whole_File, page_number:int|None=None, page_size:int|None=None, start_from:int=0, reverse:bool=False) -> list[A_Whole_File]:
        return [A_Whole_File().from_dict(one) for one in _search_function(self=self, item_filter=item_filter, page_number=page_number, page_size=page_size, start_from=start_from, reverse=reverse)]

    def raw_search(self, one_row_json_string_handler: Callable[[str], dict[str, Any] | None], page_number:int|None=None, page_size:int|None=None, start_from:int=0, reverse:bool=False) -> list[A_Whole_File]:
        '''
        one_row_json_string_handler: a_function to handle search process. If it returns None, we'll ignore it, otherwise, we'll add the return value into the result list.
        '''
        return [A_Whole_File().from_dict(one) for one in _raw_search_function(self=self, one_row_json_string_handler=one_row_json_string_handler, page_number=page_number, page_size=page_size, start_from=start_from, reverse=reverse)]

    def delete(self, item_filter: A_Whole_File):
        return _delete(self=self, item_filter=item_filter)

    def update(self, old_item_filter: A_Whole_File, new_item: A_Whole_File):
        return _update(self=self, old_item_filter=old_item_filter, new_item=new_item)


class Yingshaoxo_Database_Excutor_ytorrent_server_and_client_protocol:
    def __init__(self, database_base_folder: str, use_sqlite: bool = False, global_multiprocessing_shared_dict: Any | None = None, auto_backup: bool = False):
        self._database_base_folder = database_base_folder
        self.Ytorrent_Config = Yingshaoxo_Database_Ytorrent_Config(database_base_folder=self._database_base_folder, use_sqlite=use_sqlite, global_multiprocessing_shared_dict=global_multiprocessing_shared_dict, auto_backup=auto_backup)
        self.A_Resource = Yingshaoxo_Database_A_Resource(database_base_folder=self._database_base_folder, use_sqlite=use_sqlite, global_multiprocessing_shared_dict=global_multiprocessing_shared_dict, auto_backup=auto_backup)
        self.Need_To_Upload_Notification = Yingshaoxo_Database_Need_To_Upload_Notification(database_base_folder=self._database_base_folder, use_sqlite=use_sqlite, global_multiprocessing_shared_dict=global_multiprocessing_shared_dict, auto_backup=auto_backup)
        self.File_Segment = Yingshaoxo_Database_File_Segment(database_base_folder=self._database_base_folder, use_sqlite=use_sqlite, global_multiprocessing_shared_dict=global_multiprocessing_shared_dict, auto_backup=auto_backup)
        self.A_Whole_File = Yingshaoxo_Database_A_Whole_File(database_base_folder=self._database_base_folder, use_sqlite=use_sqlite, global_multiprocessing_shared_dict=global_multiprocessing_shared_dict, auto_backup=auto_backup)


if __name__ == "__main__":
    database_excutor = Yingshaoxo_Database_Excutor_ytorrent_server_and_client_protocol(database_base_folder="/home/yingshaoxo/CS/auto_everything/example/database/yingshaoxo_database")