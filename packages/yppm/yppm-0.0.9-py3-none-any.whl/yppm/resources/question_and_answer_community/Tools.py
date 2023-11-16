#!/usr/bin/env /home/yingshaoxo/anaconda3/bin/python3
import os
import re
import json

from auto_everything.base import Python, Terminal
from auto_everything.develop import YRPC
from auto_everything.disk import Disk
from auto_everything.database import Database_Of_Yingshaoxo
from auto_everything.io import IO


py = Python()
t = Terminal()
yrpc = YRPC()
disk = Disk()
io_ = IO()


class Tools():
    def __init__(self) -> None:
        self.project_root_folder = disk.get_directory_path(os.path.realpath(os.path.abspath(__file__)))

    def generate_protocol_files(self):
        input_folder=disk.join_paths(self.project_root_folder, "./protocol")
        input_files = ["question_and_answer.proto"]
        output_folder_for_python=disk.join_paths(self.project_root_folder, "./back_end/generated_yrpc")
        output_folder_for_javascript=disk.join_paths(self.project_root_folder, "./front_end/src/generated_yrpc")

        yrpc.generate_code(
            which_language="typescript",
            input_folder=input_folder,
            input_files=input_files,
            output_folder=output_folder_for_javascript
        )

        yrpc.generate_code(
            which_language="python",
            input_folder=input_folder,
            input_files=input_files,
            output_folder=output_folder_for_python
        )

        Database_Of_Yingshaoxo.generate_code_from_yrpc_protocol(
            which_language="python",
            input_folder=input_folder,
            input_files=input_files,
            output_folder=output_folder_for_python
        )

    def build_front_end(self):
        t.run(f"""
        cd {self.project_root_folder}
        cd front_end
        npm i
        npm run build

        #rm -fr ../back_end/vue/*
        #mkdir -p ../back_end/vue/*
        #cp -fr dist/* ../back_end/vue/
        """)

    def rebuild_docker_image(self):
        t.run(f"""
        cd {self.project_root_folder}
        docker-compose -f docker-compose.service.yaml up -d --build
        """)

    def generate_translation_json_file(self):
        # pip install translators
        # You have to make sure the text you want to translate do not contain `'`
        import translators as ts

        folders_for_string_search = [
            disk.join_paths(self.project_root_folder, "front_end/src"),
            disk.join_paths(self.project_root_folder, "back_end")
        ]
        files = []
        for folder in folders_for_string_search:
            files += disk.get_files(folder=folder, type_limiter=[".vue", ".ts", ".py"])

        txt = ""
        for file in files:
            txt += io_.read(file) + "\n\n"

        result_list = []
        result_list += re.findall(r"'(.*?)'", txt)
        result_list += re.findall(r'"(.*?)"', txt)
        result_list += re.findall(r'>(.*)<', txt)
        result_list += re.findall(r'>\n((?:.|\n)*?)<', txt, re.DOTALL)

        result_list = [one for one in result_list if "\n" not in one.strip()]

        new_result_list = []
        for each in result_list:
            new_result_list += [one for one in re.findall(r"[\w_ ,\.']+", each, re.DOTALL) if one.strip() != ""]
            # new_result_list += [one for one in re.findall(r"[\w,;'\"\s_.?!!@$()/]+", each, re.DOTALL) if one.strip() != ""]
            # new_result_list += [one for one in re.findall(r"[\w,;'\" _.?!!@$()/]+", each, re.DOTALL) if one.strip() != ""]

        new_result_list = [one.strip() for one in new_result_list if one.strip() != ""]
        new_result_list = [one.strip('_') for one in new_result_list if one.strip() != ""]
        new_result_list = [one.strip() for one in new_result_list if one.strip() != ""]
        new_result_list = [one for one in new_result_list if not all([char.isnumeric() for char in one])]
        new_result_list = [one.lower() for one in new_result_list]
        new_result_list = list(set(new_result_list))

        target_json_file = disk.join_paths(self.project_root_folder, "front_end/src/assets", "language_dict.json")
        default_json_object = {
            "": {
                "en": "",
                "cn": "",
            },
        }
        json_object = {}
        try:
            source_json_text = io_.read(target_json_file)
            json_object = json.loads(source_json_text)
        except Exception as e:
            pass

        for old in new_result_list:
            if old not in json_object.keys():
                new = ts.translate_text(query_text=old.replace("_", " "), from_language="en", to_language="zh", translator="bing")
                json_object[old] = {
                    "en": old.replace("_", " ").title(),
                    "cn": new
                }
                io_.write(target_json_file, json.dumps(json_object, indent=4, sort_keys=True))
                # sleep(0.5)

        json_object.update(default_json_object)
        io_.write(target_json_file, json.dumps(json_object, indent=4, sort_keys=True))


py.make_it_runnable()
py.fire(Tools)
