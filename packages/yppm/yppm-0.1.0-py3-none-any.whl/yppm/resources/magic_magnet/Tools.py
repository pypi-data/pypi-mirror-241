#!/usr/bin/env /home/yingshaoxo/anaconda3/bin/python3
import os

from auto_everything.base import Python, Terminal
from auto_everything.develop import YRPC
from auto_everything.disk import Disk
from auto_everything.database import Database_Of_Yingshaoxo


py = Python()
t = Terminal()
yrpc = YRPC()
disk = Disk()


class Tools():
    def __init__(self) -> None:
        self.project_root_folder = disk.get_directory_path(os.path.realpath(os.path.abspath(__file__)))

    def generate_protocol_files(self):
        # yrpc.generate_code(
        #     which_language="typescript",
        #     input_folder="./protocols",
        #     input_files=["it_has_alternatives.proto"],
        #     output_folder="./front_end/src/generated_yrpc"
        # )

        yrpc.generate_code(
            which_language="python",
            input_folder=disk.join_paths(self.project_root_folder, "./protocols"),
            input_files=["ytorrent_server_and_client_protocol.proto"],
            output_folder=disk.join_paths(self.project_root_folder, "./generated_yrpc")
        )

        Database_Of_Yingshaoxo.generate_code_from_yrpc_protocol(
            which_language="python",
            input_folder=disk.join_paths(self.project_root_folder, "./protocols"),
            input_files=["ytorrent_server_and_client_protocol.proto"],
            output_folder=disk.join_paths(self.project_root_folder, "./generated_yrpc")
        )

    # def build_front_end(self):
    #     t.run(f"""
    #     cd {self.project_root_folder}
    #     cd front_end
    #     yarn
    #     yarn build
    #     rm -fr ../backend_service/backend_service/vue/*
    #     mkdir -p ../backend_service/backend_service/vue
    #     cp -fr dist/* ../backend_service/backend_service/vue/
    #     """)

    # def rebuild_docker_image(self):
    #     # self.build_front_end()
    #     t.run(f"""
    #     cd {self.project_root_folder}
    #     docker-compose -f docker-compose.service.yaml down
    #     docker rmi yingshaoxo/it_has_alternatives
    #     docker-compose -f docker-compose.service.yaml up -d
    #     """)

    # def run(self):
    #     pass


py.make_it_runnable()
py.fire(Tools)
