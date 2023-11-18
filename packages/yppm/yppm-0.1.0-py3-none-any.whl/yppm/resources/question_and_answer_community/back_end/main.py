from typing import Any
import sys
import multiprocessing
from time import sleep
from datetime import datetime
import multiprocessing
import os
import re
import json
import random

if os.path.exists("../../../auto_everything"):
    sys.path.insert(1, "../../../")

from auto_everything.terminal import Terminal, Terminal_User_Interface
from auto_everything.python import Python
from auto_everything.disk import Disk, Store
from auto_everything.io import IO
from auto_everything.time import Time
from auto_everything.ml import ML
from auto_everything.string_ import String
ml = ML()
terminal = Terminal()
terminal_user_interface = Terminal_User_Interface()
disk = Disk()
python = Python()
io_ = IO()
time_ = Time()
store = Store("the_question_and_answer_community_config")
string_ = String()

import generated_yrpc.question_and_answer_objects as question_and_answer_objects
import generated_yrpc.question_and_answer_pure_python_rpc as question_and_answer_pure_python_rpc
from generated_yrpc.question_and_answer_yingshaoxo_database_rpc import Yingshaoxo_Database_Excutor_question_and_answer


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
print()
disk.create_a_folder(the_database_path)


offline_question_and_answer_bot_dataset_path = disk.join_paths(resource_basic_folder_path, "./yingshaoxo_chat_data")
if not disk.exists(offline_question_and_answer_bot_dataset_path):
    terminal.run(f"""
    git clone https://gitlab.com/yingshaoxo/yingshaoxo_txt_data.git "{offline_question_and_answer_bot_dataset_path}"
    """)
text_generator = ml.Yingshaoxo_Text_Generator(
    input_txt_folder_path=offline_question_and_answer_bot_dataset_path,
    use_machine_learning=False,
    type_limiter=[".txt", ".backup", ".md"]
)
new_text = text_generator.text_source_data
#new_text = new_text.replace("\n\n__**__**__yingshaoxo_is_the_top_one__**__**__\n\n", "\n\n\n") # You have to replace this seperator with your own dataset seperator
#generator_dict = text_generator.get_global_string_dict_by_using_yingshaoxo_method(new_text, levels=20)

the_text_list = [one.strip() for one in new_text.split("\n\n__**__**__yingshaoxo_is_the_top_one__**__**__\n\n") if one.strip() != ""]

new_text_list = []
for one in the_text_list:
    new_text_list += one.split("\n#")
the_text_list = new_text_list

"""
new_text_list = []
for one in the_text_list:
    new_text_list += one.split("\n\n\n")
the_text_list = new_text_list
"""

def decode_response(text: str, chat_context: str):
    #print("`"+text+"`")
    splits = text.split("\n\n__**__**__yingshaoxo_is_the_top_one__**__**__\n\n")
    if (len(splits) > 1):
        response = splits[1].strip()
    elif (len(splits) == 1):
        response = splits[0].strip()
    else:
        response = ""
    new_code = f"""
chat_context = '''{chat_context}'''

{response}
"""
    final_response = terminal.run_python_code(code=new_code)
    if final_response.strip() == "":
        final_response = response
    final_response = "\n".join([one for one in final_response.split("\n") if not one.strip().startswith("__**")])
    return final_response


#multiprocess_manager_socket_service = multiprocessing.Manager()
#global_shared_dict = multiprocess_manager_socket_service.dict()
database_excutor_for_remote_service = Yingshaoxo_Database_Excutor_question_and_answer(database_base_folder=the_database_path, use_sqlite=False, global_multiprocessing_shared_dict=None)


def verify_if_it_is_admin(the_token: str) -> bool:
    admin_token = store.get("admin_token", None)

    if admin_token == None:
        the_token = str(the_token)
        store.set("admin_token", the_token)
        return True

    admin_token = str(admin_token)
    if admin_token == the_token:
        return True
    else:
        return False


class Question_And_Answer_Service(question_and_answer_pure_python_rpc.Service_question_and_answer):
    def about(self, headers: dict[str, str], item: question_and_answer_objects.About_Request) -> question_and_answer_objects.About_Response:
        default_response = question_and_answer_objects.About_Response()

        try:
            default_response.about = "The yppm question and answer community was created by yingshaoxo."
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def ask_yingshaoxo_ai(self, headers: dict[str, str], item: question_and_answer_objects.Ask_Yingshaoxo_Ai_Request) -> question_and_answer_objects.Ask_Yingshaoxo_Ai_Response:
        default_response = question_and_answer_objects.Ask_Yingshaoxo_Ai_Response()

        try:
            if item.input == None:
                default_response.error == "You should give me input"
                return default_response
            item.input = item.input.strip()

            if text_generator == None:
                default_response.answers = "No txt database path set."
                return default_response

            if len(the_text_list) == 0:
                default_response.answers = "No txt list data."
                return default_response

            response1, response, response2 = text_generator.do_text_search(item.input, the_text_list, quick_mode=False)
            if response2 != "":
                if string_.compare_two_sentences(item.input, response) >= 0.5:
                    response = response2

            if response == "":
                response = text_generator.search_and_get_following_text_in_a_exact_way(input_text=item.input, quick_mode=True)
                response = decode_response(text=response, chat_context=item.input)

            #response = text_generator.get_next_x_chars_by_using_yingshaoxo_method(item.input, x=512, global_string_dict=generator_dict)
            #splits = response.split("\n\n\n")
            #response = "\n\n__________\n\n".join(splits[0:2])
            #response = response.strip()

            default_response.answers = response
        except Exception as e:
            print(f"Error: {e}")
            default_response.error = str(e)
            #default_response.success = False

        return default_response

    def visitor_search(self, headers: dict[str, str], item: question_and_answer_objects.Search_Request) -> question_and_answer_objects.Search_Response:
        default_response = question_and_answer_objects.Search_Response()

        try:
            if item.search_input == None:
                default_response.error == "You should give me input"
                return default_response
            item.search_input = item.search_input.strip()

            def a_handler(raw_json_text: str) -> dict[str, Any] | None:
                search_text = item.search_input
                json_object = json.loads(raw_json_text)
                if search_text.lower() in str(json_object).lower():
                    return json_object
                return None
            post_search_list = database_excutor_for_remote_service.A_Post.raw_search(one_row_json_string_handler=a_handler, page_number=item.page_number, page_size=item.page_size)
            default_response.post_list = post_search_list

            def a_comment_handler(raw_json_text: str) -> dict[str, Any] | None:
                search_text = item.search_input
                json_object = json.loads(raw_json_text)
                if search_text.lower() in str(json_object).lower():
                    return json_object
                return None
            comment_search_list = database_excutor_for_remote_service.A_Comment.raw_search(one_row_json_string_handler=a_comment_handler, page_number=item.page_number, page_size=item.page_size)
            default_response.comment_list = comment_search_list

            return default_response
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    def visitor_get_a_post(self, headers: dict[str, str], item: question_and_answer_objects.Get_A_Post_Request) -> question_and_answer_objects.Get_A_Post_Response:
        default_response = question_and_answer_objects.Get_A_Post_Response()

        try:
            result_list = database_excutor_for_remote_service.A_Post.search(item_filter=question_and_answer_objects.A_Post(
                id=item.id
            ))
            if len(result_list) > 0:
                default_response.post = result_list[0]
        except Exception as e:
            print(f"Error: {e}")
            default_response.error = str(e)
            #default_response.success = False

        return default_response

    def visitor_get_comment_list_by_id_list(self, headers: dict[str, str], item: question_and_answer_objects.Get_Comment_List_By_Id_List_Request) -> question_and_answer_objects.Get_Comment_List_By_Id_List_Response:
        default_response = question_and_answer_objects.Get_Comment_List_By_Id_List_Response()

        try:
            def a_handler(raw_json_text: str) -> dict[str, Any] | None:
                json_object = json.loads(raw_json_text)
                if json_object["id"] in item.comment_id_list:
                    return json_object
                return None
            comment_list = database_excutor_for_remote_service.A_Comment.raw_search(one_row_json_string_handler=a_handler)
            default_response.comment_list = comment_list
        except Exception as e:
            print(f"Error: {e}")
            default_response.error = str(e)
            #default_response.success = False

        return default_response

    def user_add_post(self, headers: dict[str, str], item: question_and_answer_objects.Add_Post_Request) -> question_and_answer_objects.Add_Post_Response:
        default_response = question_and_answer_objects.Add_Post_Response()

        try:
            if item.username == None:
                item.username = ""
            if item.a_post.title == None:
                default_response.error = "You should give me a title for your question."
                return default_response
            if item.a_post.description == None:
                default_response.error = "You should give me a description for your question."
                return default_response

            item.a_post.title = item.a_post.title.strip()
            item.a_post.description = item.a_post.description.strip()

            if len(item.a_post.title) > 300:
                default_response.error = "You should not publish a title that greater than 300 characters."
                return default_response
            if len(item.a_post.description) > 10000:
                default_response.error = "You should not publish a description that greater than 10000 characters."
                return default_response

            result_list = database_excutor_for_remote_service.A_Post.search(item_filter=question_and_answer_objects.A_Post(
                title=item.a_post.title
            ))
            if len(result_list) > 0:
                default_response.error = "You should change a title for your question. It is already been taken."
                return default_response

            random_numbers = "".join([str(random.randint(0, 9)) for i in range(6)])
            new_id = item.a_post.title[:30].replace(" ", "_").replace("-", "_") + random_numbers
            database_excutor_for_remote_service.A_Post.add(question_and_answer_objects.A_Post(
                owner_id=item.username,
                id=new_id,
                title=item.a_post.title,
                description=item.a_post.description,
                comment_id_list=[],
                create_time_in_10_numbers_timestamp_format=time_.get_current_timestamp_in_10_digits_format(),
                tag=[], # for example, [ad, spam, adult]
            ))
            default_response.post_id = new_id
            default_response.success = True
        except Exception as e:
            print(f"Error: {e}")
            default_response.error = str(e)
            default_response.success = False

        return default_response

    def user_comment_post(self, headers: dict[str, str], item: question_and_answer_objects.Comment_Post_Request) -> question_and_answer_objects.Comment_Post_Response:
        default_response = question_and_answer_objects.Comment_Post_Response()

        try:
            if item.username == None:
                item.username = ""
            if item.a_comment.description == None:
                default_response.error = "You should give me a description for your comment."
                return default_response

            item.a_comment.description = item.a_comment.description.strip()
            if len(item.a_comment.description) > 1000:
                default_response.error = "You should not publish a comment that greater than 1000 characters."
                return default_response

            if item.a_comment.parent_post_id == None or item.a_comment.parent_post_owner_id == None:
                default_response.error = "You should give me the parent_post_id and parent_post_owner_id for your comment."
                return default_response
            post_list = database_excutor_for_remote_service.A_Post.search(item_filter=question_and_answer_objects.A_Post(
                id=item.a_comment.parent_post_id,
                owner_id=item.a_comment.parent_post_owner_id
            ))
            if len(post_list) == 0:
                default_response.error = "The question you want to add comment to, is not exists."
                return default_response

            result_list = database_excutor_for_remote_service.A_Comment.search(item_filter=question_and_answer_objects.A_Comment(
                description=item.a_comment.description
            ))
            if len(result_list) > 0:
                default_response.error = "The comment you want to add is used by someone maybe at some other question/post."
                return default_response

            # add comment
            random_numbers = "".join([str(random.randint(0, 9)) for i in range(6)])
            new_id = item.a_comment.description[:30].replace(" ", "_").replace("-", "_") + random_numbers
            database_excutor_for_remote_service.A_Comment.add(question_and_answer_objects.A_Comment(
                owner_id=item.username,
                id=new_id,
                parent_post_id=item.a_comment.parent_post_id,
                parent_post_owner_id=item.a_comment.parent_post_owner_id,
                description=item.a_comment.description,
                create_time_in_10_numbers_timestamp_format=time_.get_current_timestamp_in_10_digits_format(),
                tag=[], # for example, [ad, spam, adult]
            ))

            # add comment id to the old post comment_list
            that_post = post_list[0]
            if that_post.comment_id_list == None:
                that_post.comment_id_list = [new_id]
            else:
                that_post.comment_id_list += [new_id]
            post_list = database_excutor_for_remote_service.A_Post.update(old_item_filter=question_and_answer_objects.A_Post(
                id=that_post.id,
                owner_id=that_post.owner_id
            ), new_item=that_post)

            default_response.comment_id = new_id
            default_response.success = True
        except Exception as e:
            print(f"Error: {e}")
            default_response.error = str(e)
            #default_response.success = False

        return default_response

    def user_download_backup_data(self, headers: dict[str, str], item: question_and_answer_objects.Download_Backup_Data_Request) -> question_and_answer_objects.Download_Backup_Data_Response:
        default_response = question_and_answer_objects.Download_Backup_Data_Response()

        try:
            if item.username == None:
                default_response.error = "You should give me a username to download its data."
                return default_response

            all_data = {}

            question_list = database_excutor_for_remote_service.A_Post.search(item_filter=question_and_answer_objects.A_Post(
                owner_id=item.username
            ))
            all_data["questions"] = [one.to_dict() for one in question_list]

            comment_list = database_excutor_for_remote_service.A_Comment.search(item_filter=question_and_answer_objects.A_Comment(
                owner_id=item.username
            ))
            all_data["comments"] = [one.to_dict() for one in comment_list]

            all_data_json_text = json.dumps(all_data, indent=4)

            temp_json_file = disk.get_a_temp_file_path("user_data_backup.json")
            default_response.file_bytes_in_base64_format = disk.bytes_to_base64(all_data_json_text.encode("utf-8"))
            default_response.file_name = "user_data_backup.json"
        except Exception as e:
            print(f"Error: {e}")
            default_response.error = str(e)
            #default_response.success = False

        return default_response

    def admin_download_backup_data(self, headers: dict[str, str], item: question_and_answer_objects.Admin_Download_Backup_Data_Request) -> question_and_answer_objects.Admin_Download_Backup_Data_Response:
        default_response = question_and_answer_objects.Admin_Download_Backup_Data_Response()

        try:
            if item.token == None:
                default_response.error = "You should give me the token."
                return default_response

            if verify_if_it_is_admin(item.token) == False:
                default_response.error = "The admin token is wrong."
                return default_response

            target_file_name = f"question_and_answer_backup_{str(datetime.now()).split('.')[0]}.zip"
            temp_zip_file = disk.get_a_temp_file_path(target_file_name)
            disk.compress(input_folder_path=the_database_path, output_zip_path=temp_zip_file)
            bytes_io_data = disk.get_bytesio_from_a_file(temp_zip_file)
            default_response.file_bytes_in_base64_format = disk.bytesio_to_base64(bytes_io_data)
            default_response.file_name = target_file_name
        except Exception as e:
            print(f"Error: {e}")
            default_response.error = str(e)
            #default_response.success = False

        return default_response

    def admin_upload_backup_data(self, headers: dict[str, str], item: question_and_answer_objects.Admin_Upload_Backup_Data_Request) -> question_and_answer_objects.Admin_Upload_Backup_Data_Response:
        default_response = question_and_answer_objects.Admin_Upload_Backup_Data_Response()

        try:
            if item.token == None:
                default_response.error = "You should give me the token."
                return default_response

            if verify_if_it_is_admin(item.token) == False:
                default_response.error = "The admin token is wrong."
                return default_response

            base64_string = item.file_bytes_in_base64_format
            if base64_string == None:
                default_response.error = "the 'file_bytes_in_base64_format' shoudn't be None"
                return default_response

            the_backup_zip_file_bytes_io = disk.base64_to_bytesio(base64_string=base64_string)
            backup_zip_file = disk.get_a_temp_file_path('backup.zip')
            disk.save_bytesio_to_file(bytes_io=the_backup_zip_file_bytes_io, file_path=backup_zip_file)

            temp_saving_folder: str = disk.join_paths(disk.get_the_temp_dir(), "question_and_answer_community_backup")
            if disk.exists(temp_saving_folder):
                disk.delete_a_folder(temp_saving_folder)
            disk.uncompress(backup_zip_file, temp_saving_folder)

            disk.copy_a_folder(source_folder_path=temp_saving_folder, target_folder_path=database_excutor_for_remote_service._database_base_folder)

            default_response.success = True
        except Exception as e:
            print(f"Error: {e}")
            default_response.error = str(e)
            #default_response.success = False

        return default_response


def generate_robots_txt_and_sitemap_xml(domain: str, output_folder: str):
    if not disk.exists(output_folder):
        print(f"Can't generate robots.txt and sitemap.xml to {output_folder}")
        return

    import urllib.parse
    robots = f"""
User-agent: *
Sitemap: {domain}/sitemaps.xml
""".strip()

    sitemap_part = """
"""
    sitemap_part_list = []
    search_list = database_excutor_for_remote_service.A_Post.search(item_filter=question_and_answer_objects.A_Post())
    for one in search_list:
        last_modify_time = time_.get_datetime_object_from_timestamp(one.create_time_in_10_numbers_timestamp_format).strftime("%y-%m-%d")
        safe_name = urllib.parse.quote_plus(one.id)
        sitemap_part_list.append(f"""
   <url>
      <loc>{domain}/detail_page?id={safe_name}</loc>
      <lastmod>{last_modify_time}</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.8</priority>
   </url>
""")
    sitemap_part_list_text = "\n".join(sitemap_part_list)

    sitemap = f"""
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_part_list_text}
</urlset>
""".strip()

    robot_txt_path = disk.join_paths(output_folder, "robots.txt")
    io_.write(robot_txt_path, robots)

    sitemap_xml_path = disk.join_paths(output_folder, "sitemaps.xml")
    io_.write(sitemap_xml_path, sitemap)


def run_service(port: str):
    database_excutor_for_remote_service.A_Post.database_of_yingshaoxo.refactor_database()
    database_excutor_for_remote_service.A_Comment.database_of_yingshaoxo.refactor_database()
    service_instance = Question_And_Answer_Service()

    html_folder_path = "../front_end/dist"
    generate_robots_txt_and_sitemap_xml(domain="https://ask.ai-tools-online.xyz", output_folder=html_folder_path)
    question_and_answer_pure_python_rpc.run(service_instance, port=port, html_folder_path=html_folder_path)


print("YPPM community Service starts at: http://0.0.0.0:54321")
run_service("54321")
