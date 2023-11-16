#!/usr/bin/env /usr/bin/python3
from typing import Any

import os
import sys
import platform
import json
import re
from time import sleep

try:
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # in pyinstaller
        def resource_path(relative_path: str) -> str:
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path) #type: ignore
            return os.path.join(os.path.abspath("."), relative_path)
        _the_current_path = resource_path(".")
        sys.path.append(os.path.abspath(_the_current_path.replace("/./", "/")))
    else:
        # normal process
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
except Exception as e:
    pass

from auto_everything.io import IO
from auto_everything.disk import Disk
from auto_everything.python import Python
from auto_everything.terminal import Terminal, Terminal_User_Interface
try:
    from auto_everything.string_ import String
except Exception as e:
    from auto_everything.string import String
from auto_everything.ml import ML

py = Python()
io_ = IO()
terminal = Terminal()
disk = Disk()
python_ = Python()
terminal_user_interface = Terminal_User_Interface()
string_ = String()
ml = ML()


class Tools():
    def __init__(self) -> None:
        # get static resource folder
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            #print('running in a PyInstaller bundle')
            def resource_path(relative_path: str) -> str:
                if hasattr(sys, '_MEIPASS'):
                    return os.path.join(sys._MEIPASS, relative_path) #type: ignore
                return os.path.join(os.path.abspath("."), relative_path)
            resource_basic_folder_path = resource_path(".")
        else:
            #print('running in a normal Python process')
            resource_basic_folder_path = disk.get_directory_path(__file__)
        self.resource_basic_folder_path = disk.join_paths(resource_basic_folder_path, 'resources').replace("/./", "/")
        self.auto_everything_basic_folder_path = disk.join_paths(resource_basic_folder_path, 'auto_everything').replace("/./", "/")

        # get python executable path
        self.host_python_executable_path = "python"
        if " 3." in terminal.run_command("python --version"):
            self.host_python_executable_path = "python"
        elif " 3." in terminal.run_command("python3 --version"):
            self.host_python_executable_path = "python3"

        # get git user email and username
        self.git_user_email = terminal.run_command("git config user.email").strip().split('\n')[0]
        self.git_user_name = terminal.run_command("git config user.name").strip().split('\n')[0].lower()
        if self.git_user_name == "":
            try:
                self.git_user_name = string_.remove_all_special_characters_from_a_string(os.getlogin(), white_list_characters='_').strip().lower()
            except Exception as e:
                print(e)
                self.git_user_name = ""
            if self.git_user_name == "":
                self.git_user_name = platform.system().lower().strip()

        # get project base folder
        self.project_root_folder = os.getcwd()

        # get virtual env folder
        self.virtual_env_folder = disk.join_paths(self.project_root_folder, ".venv")
        # self.env_activate_file_path = disk.join_paths(self.virtual_env_folder, "bin/activate")

        # get package json file
        self.package_json_file_path = disk.join_paths(self.project_root_folder, "package.json")

        # get local dependencies folder
        self.python_local_modules_folder = disk.join_paths(self.project_root_folder, ".python_modules")

    def _add_to_gitignore(self, name: str):
        gitignore_path = disk.join_paths(self.project_root_folder, ".gitignore")
        if disk.exists(gitignore_path):
            text = io_.read(gitignore_path)
            lines = text.split("\n")
            if not any([line.strip() == name for line in lines]):
                text = f"{name}\n" + text
                io_.write(gitignore_path, text)
        else:
            text = name
            io_.write(gitignore_path, text)

    def _add_to_dockerignore(self, name: str):
        gitignore_path = disk.join_paths(self.project_root_folder, ".dockerignore")
        if disk.exists(gitignore_path):
            text = io_.read(gitignore_path)
            lines = text.split("\n")
            if not any([line.strip() == name for line in lines]):
                text = f"{name}\n" + text
                io_.write(gitignore_path, text)
        else:
            text = name
            io_.write(gitignore_path, text)

    def _create_virtual_env(self):
        if disk.exists(self.virtual_env_folder):
            return

        print(f"Creating virtual envirnoment by using '{self.host_python_executable_path}'...")

        terminal.run(f"""
        {self.host_python_executable_path} -m venv {self.virtual_env_folder}
                     """)

        # change permission of activate file
        # terminal.run(f"""chmod 777 {self.env_activate_file_path}""")

        # ignore .venv folder
        self._add_to_gitignore(".venv/")
        self._add_to_gitignore("__pycache__/")
        self._add_to_gitignore(".vscode/")
        self._add_to_gitignore(".github/")
        self._add_to_gitignore("*.swp")
        self._add_to_gitignore(".python_modules/")

        self._add_to_dockerignore(".venv/")
        self._add_to_dockerignore("__pycache__/")
        self._add_to_dockerignore("*.swp")

        # create .python_modules directory
        if not disk.exists(self.python_local_modules_folder):
            disk.create_a_folder(self.python_local_modules_folder)

    def _get_virtual_env_python_excutable_path(self):
        self._create_virtual_env()

        return disk.join_paths(self.virtual_env_folder, "bin", "python3")

    def _get_virtual_env_pip_path(self):
        self._create_virtual_env()

        return disk.join_paths(self.virtual_env_folder, "bin", "pip3")

    def _get_virtual_env_program(self, name: str, exact_match: bool = False):
        root_search_folder_list = [
            disk.join_paths(self.virtual_env_folder, "bin"),
            disk.join_paths(self.virtual_env_folder, "Scripts"),
        ]
        for search_folder in root_search_folder_list:
            if not disk.exists(search_folder):
                continue
            files = disk.get_files(search_folder, recursive=True)
            for file in files:
                file_name_without_content_after_dot, suffix = disk.get_stem_and_suffix_of_a_file(file)
                if exact_match == False:
                    if name.lower() in file_name_without_content_after_dot.lower():
                        return disk.get_absolute_path(file)
                else:
                    if name == file_name_without_content_after_dot:
                        return disk.get_absolute_path(file)
        return None

    def _hack_into_virtual_env_bash_command(self):
        self._create_virtual_env()

        the_bin_path = disk.join_paths(self.virtual_env_folder, "bin")

        return f"""
        export PATH="{the_bin_path}:$PATH"
        """.strip()

    def _get_package_json_object(self) -> Any:
        try:
            text = io_.read(self.package_json_file_path)
            lines = []
            for line in text.split("\n"):
                if line.strip().startswith("#") or line.strip().startswith("//"):
                    #ignore comments
                    pass
                else:
                    lines.append(line)
            text = "\n".join(lines)
            json_object = json.loads(text)
            return json_object
        except Exception as e:
            print(e)
            return None

    def _get_local_packages_list(self) -> list[str]:
        try:
            return [disk.join_paths("./.python_modules/", path_) for path_ in os.listdir(self.python_local_modules_folder)]
        except Exception as e:
            print(e)
            return []

    def _make_relative_python_import_work_again(self, python_file_path: str):
        def modify_this_python_code(code_file_path: str, code: str) -> str:
            absolute_code_file_path = disk.get_absolute_path(code_file_path)
            absolute_code_directory_path = disk.get_directory_path(absolute_code_file_path)

            def convert_function(matchobj: re.Match):
                raw_string = matchobj.group().strip()

                match_dict = matchobj.groupdict()
                space = match_dict.get("space")
                file_path = match_dict.get("file_path")
                nickname = match_dict.get("nickname")

                absolute_file_path = disk.get_absolute_path(file_path)
                absolute_directory_path = disk.get_directory_path(absolute_file_path)
                init_file_path_for_a_package = disk.join_paths(absolute_directory_path, "__init__.py")
                files_inside_that_package = disk.get_files(absolute_directory_path, recursive=False, type_limiter=[".py"])
                files_inside_that_package = [disk.get_file_name(one)[:-3] for one in files_inside_that_package]
                files_inside_that_package = [one for one in files_inside_that_package if one != "__init__"]
                the_import_string_in_init_file = "\n".join([f"    import {one}" for one in files_inside_that_package])
                io_.write(init_file_path_for_a_package, f"""
try:
{the_import_string_in_init_file}
except Exception as e:
    pass
                """.strip())

                if disk.is_directory(file_path):
                    if nickname == None:
                        nickname = disk.get_directory_name(file_path)
                else:
                    stem, suffix = disk.get_stem_and_suffix_of_a_file(file_path)
                    if nickname == None:
                        nickname = stem

                import_string = '" "'
                if absolute_file_path.startswith(absolute_code_directory_path):
                    # The target file is a child of the project
                    segments = absolute_file_path[len(absolute_code_directory_path):].strip("/").split("/")
                    if "." in segments[-1]:
                        segments[-1] = ".".join(segments[-1].split(".")[:-1])
                    import_string = ".".join(segments)

                    template = f"""{space}import {import_string} as {nickname}\n#{raw_string}"""
                    return template
                else:
                    if disk.is_directory(file_path):
                        directory_name = disk.get_directory_name(file_path)
                        if nickname == None:
                            nickname = disk.get_directory_name(file_path)
                        template = f"""{space}import sys; sys.path.append("{file_path}"); import {directory_name} as {nickname}\n#{raw_string}"""
                        return template
                    else:
                        stem, suffix = disk.get_stem_and_suffix_of_a_file(file_path)
                        if nickname == None:
                            nickname = stem
                        template = f"""{space}import importlib.machinery; import importlib.util; loader_ = importlib.machinery.SourceFileLoader("{stem}", "{file_path}"); spec_ = importlib.util.spec_from_loader(loader_.name, loader_); {nickname} = importlib.util.module_from_spec(spec_); loader_.exec_module({nickname});\n#{raw_string}"""
                        return template

            new_code = re.sub(r'^(?P<space>\s*)import\ \"(?P<file_path>.*)\"(?:\ as\ (?P<nickname>[^#\s]*))*', convert_function, code, flags=re.MULTILINE)
            return new_code

        if not disk.exists(python_file_path):
            return

        code = io_.read(python_file_path)
        new_code = modify_this_python_code(code_file_path=python_file_path, code=code)
        io_.write(python_file_path, new_code)

    def _make_sure_git_exists(self):
        if "version" not in terminal.run_command("git --version").lower():
            print("git is needed for this operation.\nYou can install it with 'sudo apt install git'")
            exit()

    def todo(self):
        import _todo

    def create_a_new_project(self):
        global default_template_name, default_project_name

        # select teplates
        default_template_name = "basic_python_project"
        default_template_name = terminal_user_interface.selection_box(
            "Which project template you want to use? ", [
                ("basic_python_project", None),
                ("simple_backend_and_frontend_project", None),
                ("question_and_answer_community", None),
            ]
        )

        # handle project name
        default_project_name = ""

        def assign_name(text: str):
            global default_project_name
            text = text.strip()
            if text == "":
                print("You can't give me an empty name!")
                exit()
            default_project_name = text

        terminal_user_interface.input_box(
            f"\n\nPlease give me the new project name: ",
            default_value=default_project_name,
            handle_function=assign_name
        )

        default_project_name = default_project_name.strip().replace(" ", "_").replace("-", "_")

        # copy template folder
        project_path = disk.join_paths(disk.get_current_working_directory(), default_project_name)
        disk.delete_a_folder(project_path)
        if default_template_name == "basic_python_project":
            source_folder_path = disk.join_paths(self.resource_basic_folder_path, default_template_name)
            disk.copy_a_folder(source_folder_path=source_folder_path, target_folder_path=project_path)

            disk.copy_a_folder(source_folder_path=self.auto_everything_basic_folder_path, target_folder_path=disk.join_paths(project_path, "auto_everything"))

            os.chdir(project_path)
            self.__init__()

            self.init(name=default_project_name)

            print(f"\n\nNow you could go to the new project by using: \ncd {default_project_name}")
        elif default_template_name == "simple_backend_and_frontend_project":
            source_folder_path = disk.join_paths(self.resource_basic_folder_path, default_template_name)
            disk.copy_a_folder(source_folder_path=source_folder_path, target_folder_path=project_path)

            disk.copy_a_folder(source_folder_path=self.auto_everything_basic_folder_path, target_folder_path=disk.join_paths(project_path, "back_end", "auto_everything"))

            os.chdir(project_path)
            self.__init__()

            self.init(name=default_project_name)

            print(f"\n\nNow you could go to the new project by using: \ncd {default_project_name}")
        elif default_template_name == "question_and_answer_community":
            source_folder_path = disk.join_paths(self.resource_basic_folder_path, default_template_name)
            disk.copy_a_folder(source_folder_path=source_folder_path, target_folder_path=project_path)

            disk.copy_a_folder(source_folder_path=self.auto_everything_basic_folder_path, target_folder_path=disk.join_paths(project_path, "back_end", "auto_everything"))

            os.chdir(project_path)
            self.__init__()

            self.init(name=default_project_name)

            print(f"\n\nNow you could go to the new project by using: \ncd {default_project_name}")

    def init(self, name: str = ""):
        # create package.json file in current folder if there does not have one
        if disk.exists(self.package_json_file_path):
            print("There already has a 'package.json' file.")
        else:
            json_content = """
            {
                "name": "",
                "version": "",
                "author": "",
                "main": "main.py",
                "scripts": {},
                "dependencies": [
                ]
            }
            """
            package_object = json.loads(json_content)
            print("\n")

            # handle project name
            name = name.strip()
            if name == "":
                default_project_name = disk.get_directory_name(self.project_root_folder)
                name = terminal_user_interface.input_box(
                    f"Please give me a project name (default '{default_project_name}'): ",
                    default_value=default_project_name,
                    handle_function=None
                )

            package_object["name"] = name.strip().replace(" ", "_").replace("-", "_")

            # handle project version
            default_project_version = "0.0.0"
            def assign_version(text: str):
                package_object["version"] = text.strip()
            terminal_user_interface.input_box(
                f"Please give me a project version (default '{default_project_version}'): ",
                default_value=default_project_version,
                handle_function=assign_version
            )

            # handle author name
            default_author = self.git_user_email
            if "@" not in default_author:
                default_author = ""
            def assign_author(text: str):
                package_object["author"] = text.strip()
            terminal_user_interface.input_box(
                f"Please give me your name (default '{default_author}'): ",
                default_value=default_author,
                handle_function=assign_author
            )

            io_.write(self.package_json_file_path, json.dumps(package_object, indent=4))
            self._create_virtual_env()

            self.install()

            main_py_file_path = disk.join_paths(self.project_root_folder, "main.py")
            if not disk.exists(main_py_file_path):
                io_.write(main_py_file_path, 'print("Hello World!")')

    def run(self, script_name: str = ""):
        if not disk.exists(self.package_json_file_path):
            print("You have to run `yppm init` first.")
            return
        self._create_virtual_env()

        package_object = self._get_package_json_object()

        scripts = package_object.get("scripts")
        if scripts == None:
            print('package.json should have a key called {"scripts": {}}')
            return

        entry_point_python_script = package_object.get("main")
        if entry_point_python_script == None:
            print('package.json should have a key called {"main": "main.py"}')
            return

        script_name = script_name.strip()
        if script_name == "":
            # {self.env_activate_file_path}
            try:
                self._make_relative_python_import_work_again(entry_point_python_script)
            except Exception as e:
                print(e)
            terminal.run(f"""
            {self._hack_into_virtual_env_bash_command()}

            {self._get_virtual_env_python_excutable_path()} {entry_point_python_script}
                         """, use_os_system=True)
        elif script_name == "?":
            if len(scripts.keys()) == 0:
                print("There has no scripts to run.")
            else:
                selections = []
                for script_name in scripts.keys():
                    selections.append(
                        (f'{script_name}', lambda: script_name.strip())
                    )
                selection = terminal_user_interface.selection_box(
                    "Which script you want to run?",
                    selections
                )
                if selection in scripts.keys():
                    terminal.run(f"{scripts[selection]}", use_os_system=True)
        else:
            if script_name in scripts.keys():
                # {self.env_activate_file_path}
                terminal.run(f"""
                {self._hack_into_virtual_env_bash_command()}

                {scripts[script_name]}
                            """, use_os_system=True)
            else:
                print(f"Sorry, script '{script_name}' not exists in the package.json")

    def _install_package(self, package_name: str, upgrade: bool = False):
        pip_path = self._get_virtual_env_pip_path()

        yes_exists = terminal.run_command("yes --version")
        if ("copyright" in yes_exists.strip().lower()):
            yes_exists = True
        else:
            yes_exists = False

        if upgrade == False:
            # {self.env_activate_file_path}
            terminal.run(f"""
            {self._hack_into_virtual_env_bash_command()}
            yes | {pip_path} install {package_name}
                        """)
        else:
            # {self.env_activate_file_path}
            terminal.run(f"""
            {self._hack_into_virtual_env_bash_command()}
            yes | {pip_path} install {package_name} --upgrade
                        """)

    def _uninstall_package(self, package_name: str):
        if (package_name.startswith("./.python_modules")):
            target_folder = disk.join_paths(self.project_root_folder, package_name)
            disk.delete_a_folder(target_folder)
        else:
            pip_path = self._get_virtual_env_pip_path()

            # {self.env_activate_file_path}
            terminal.run(f"""
            {self._hack_into_virtual_env_bash_command()}
            {pip_path} uninstall {package_name} -y
                            """)

    def install(self, package_name: str = ""):
        if not disk.exists(self.package_json_file_path):
            print("You have to run `yppm init` first.")
            return
        self._create_virtual_env()

        package_object = self._get_package_json_object()

        dependencies = package_object.get("dependencies")
        if dependencies == None:
            print('package.json should have a key called {"dependencies": []}')
            return

        package_name = package_name.strip()
        if package_name == "":
            # install all package
            for package_name in dependencies:
                self._install_package(package_name=package_name)
        # elif package_name.startswith("http://") or package_name.startswith("https://") or disk.exists(package_name):
        #     # if without pip, we could use `yppm install https://*.tar.gz` and `yppm install *.tar.gz`
        #     # What yppm will do is download, uncompress, put it into .python_modules/
        #     # Add "./.python_modules/*" into package.json file
        #     pass
        else:
            # install one package
            if package_name not in dependencies:
                # install once
                self._install_package(package_name=package_name)
            else:
                # install again
                self._install_package(package_name=package_name, upgrade=True)

            if package_name not in dependencies:
                package_object["dependencies"].append(package_name)
                io_.write(self.package_json_file_path, json.dumps(package_object, indent=4))

    def uninstall(self, package_name: str = ""):
        if not disk.exists(self.package_json_file_path):
            print("You have to run `yppm init` first.")
            return
        self._create_virtual_env()

        package_object = self._get_package_json_object()

        dependencies = package_object.get("dependencies")
        if dependencies == None:
            print('package.json should have a key called {"dependencies": []}')
            return

        package_name = package_name.strip()
        if package_name == "":
            pass
        elif package_name == "?":
            pip_path = self._get_virtual_env_pip_path()
            package_list_from_pip = terminal.run_command(f"""
                {self._hack_into_virtual_env_bash_command()}
                {pip_path} list
                            """).strip()
            package_list_from_pip = package_list_from_pip.split("\n\n")[0]
            package_list_from_pip = package_list_from_pip.strip().split("\n")[2:]
            package_list_from_pip = [package_name for package_name in package_list_from_pip if package_name.strip()[-1].isdigit()]
            package_list_from_pip = [package_name.split(" ")[0].replace("-", "_") for package_name in package_list_from_pip]

            # add json defined packages on the top of the list
            for package_in_json_file in dependencies:
                if package_in_json_file not in package_list_from_pip:
                    package_list_from_pip.insert(0, package_in_json_file)

            # add local packages on the end of the list
            for package_in_local in self._get_local_packages_list():
                if package_in_local not in package_list_from_pip:
                    package_list_from_pip.append(package_in_local)

            package_name = terminal_user_interface.selection_box("Please select the package you want to uninstall: ", [
                (package_name, None) for package_name in package_list_from_pip
            ])

            self._uninstall_package(package_name=package_name)
        else:
            self._uninstall_package(package_name=package_name)

        if package_name in dependencies:
            package_object["dependencies"] = [one for one in package_object["dependencies"] if one != package_name]
            io_.write(self.package_json_file_path, json.dumps(package_object, indent=4))

    def build(self, arguments: str = ""):
        self._create_virtual_env()
        python_path = self._get_virtual_env_python_excutable_path()
        pip_path = self._get_virtual_env_pip_path()

        package_object = self._get_package_json_object()

        name = package_object.get("name")
        if name == None:
            print('package.json should have a key called {"name": "your_app_name"}')
            return

        entry_point_python_script = package_object.get("main")
        if entry_point_python_script == None:
            print('package.json should have a key called {"main": "main.py"}')
            return

        self._add_to_gitignore(".build/")
        self._add_to_gitignore(".dist/")
        self._add_to_gitignore("*.spec")
        self._add_to_gitignore(".yppm_dist/")

        disk.create_a_folder("dist")

        terminal.run(f"""
        {self._hack_into_virtual_env_bash_command()}

        export PIP_BREAK_SYSTEM_PACKAGES=1
        {pip_path} install pyinstaller==5.13.0
        """)

        pyinstaller_path = self._get_virtual_env_program("pyinstaller", exact_match=True)
        if pyinstaller_path == None:
            pyinstaller_path = f"{python_path} -m pyinstaller"

        try:
            hidden_import_list = [one.split("=")[0] for one in package_object.get("dependencies") if not (one.startswith("git") or one.startswith("http"))]
            hidden_import_list = [f"--hidden-import {one}" for one in hidden_import_list]
            hidden_import_list_text = " ".join(hidden_import_list)
        except Exception as e:
            print(e)
            hidden_import_list_text = ""

        terminal.run(f"""
        {self._hack_into_virtual_env_bash_command()}

        {pyinstaller_path} {entry_point_python_script} {arguments} --noconfirm --onefile --add-data "./auto_everything:auto_everything" {hidden_import_list_text} --name {name}
         """)

    def build_with_nuitka(self, arguments: str = ""):
        self._create_virtual_env()
        python_path = self._get_virtual_env_python_excutable_path()
        pip_path = self._get_virtual_env_pip_path()

        package_object = self._get_package_json_object()

        name = package_object.get("name")
        if name == None:
            print('package.json should have a key called {"name": "your_app_name"}')
            return

        entry_point_python_script = package_object.get("main")
        if entry_point_python_script == None:
            print('package.json should have a key called {"main": "main.py"}')
            return

        self._add_to_gitignore("*.dist/")
        self._add_to_gitignore("*.build/")

        disk.create_a_folder("dist")

        terminal.run(f"""
        {self._hack_into_virtual_env_bash_command()}

        export PIP_BREAK_SYSTEM_PACKAGES=1
        {pip_path} install nuitka==1.8.4
        {pip_path} install patchelf==0.17.2.1

        {python_path} -m nuitka {arguments} --static-libpython=yes --standalone --follow-imports {entry_point_python_script} -o {name}
         """)

    def clean(self):
        disk.delete_a_folder(self.virtual_env_folder)
        disk.delete_a_folder("./build")
        disk.delete_a_folder("./dist")
        terminal.run(f"""
        rm -fr *.spec
                     """)

    # def env(self):
    #     print(f""" Please run:\n\n{self.env_activate_file_path} """.strip())

    def about(self):
        terminal.run("clear")
        print("""
YPPM: Yingshaoxo Python Package Manager.

(yingshaoxo is my name)
        """.strip())

    def create_a_global_entry_for_this_project(self):
        if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
            print("Sudo permission is needed for this operation.\n")
            print(f"If you do not have root permission but still want to run this project, do this:\ncd {self.project_root_folder} && yppm run")
            return

        binary_version_of_yppm = "/usr/bin/yppm"
        if not disk.exists(binary_version_of_yppm):
            binary_version_of_yppm = f"{self.host_python_executable_path} -m yppm"

        entry_point_bash_code = f"""
#!/bin/sh
cd {self.project_root_folder} && {binary_version_of_yppm} run
        """

        json_object = self._get_package_json_object()
        if "name" not in json_object:
            print("There should have a name in package.json")
            return

        name = json_object.get("name").strip().replace(" ", "_").replace("-", "_")
        io_.write(f"/usr/bin/{name}", entry_point_bash_code)
        terminal.run(f"chmod 777 /usr/bin/{name}")

        print(f"Now you could run this project by using `{name}`\n")
        print(f"If you want to delete this entry, just try `sudo rm /usr/bin/{name}`")

    def download_never_upgrade_python_and_yppm(self):
        """
        This will download a amd64 static python in /bin/static_python folder
        Then do a link of /bin/python3 and /bin/python to /bin/static_python/data/Python-3.10.4/python
        Then download yppm to /bin/yppm_folder
        Then do a link of /bin/yppm to "/bin/python3 /bin/yppm_folder/yppm/main.py"
        Then ask user to delete old ~/.bashrc yppm entry
        """
        if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
            print("Sudo permission is needed for this operation.\n")
            print(f"You can run this:\n\nsudo yppm download_never_upgrade_python_and_yppm")
            return

        if "version" not in terminal.run_command("git --version").lower():
            print("git is needed for this operation.\nYou can install it with 'sudo apt install git'")
            return

        # download static python
        static_python_folder = "/bin/static_python"
        disk.delete_a_folder(static_python_folder)
        the_static_python_git_url = "https://gitlab.com/yingshaoxo/use_docker_to_build_static_python3_binary_executable.git"
        terminal.run(f"""
        git clone {the_static_python_git_url} {static_python_folder}
        """)

        # check if python binary exists
        the_real_python_path = f"{static_python_folder}/data/Python-3.10.4/python"
        if not disk.exists(the_real_python_path):
            print(f"The python binary file is not in '{the_real_python_path}'")
            print(f"You can download one, and put it into: {the_real_python_path}")
            print(f"You may found it here: {the_static_python_git_url}")
            return

        # install that python binary file
        terminal.run(f"""
        mv /bin/python /bin/python_backup
        mv /bin/python3 /bin/python3_backup

        rm /bin/python
        rm /bin/python3

        chmod 777 {the_real_python_path}
        ln -s {the_real_python_path} /bin/python
        ln -s {the_real_python_path} /bin/python3
        """)

        # download yppm
        yppm_folder = "/bin/yppm_folder"
        disk.delete_a_folder(yppm_folder)
        yppm_git_url = "https://gitlab.com/yingshaoxo/yppm.git"
        terminal.run(f"""
        git clone {yppm_git_url} {yppm_folder}
        """)
        the_real_yppm_path = f"{yppm_folder}/yppm/main.py"
        if not disk.exists(the_real_yppm_path):
            print(f"The yppm file is not in '{the_real_yppm_path}'")
            print(f"You can download one, and put it into: {the_real_yppm_path}")
            print(f"You may found it here: {yppm_git_url}")
            return

        # install that yppm file
        yppm_entry_bash = "/bin/yppm"
        terminal.run(f"""
        rm /bin/yppm
        """)
        io_.write(yppm_entry_bash, f"""
#!/bin/sh
{the_real_python_path} {the_real_yppm_path}
""")
        terminal.run(f"""
        chmod 777 /bin/yppm
        """)

        # notify the user to delete some old file
        print("Great! Now you got the never upgrade python3.10 and yppm installed.")
        print("""Try to use 'vim ~/.bashrc' to delete "alias yppm='python3 -m yppm'" to start use the new yppm software.""")

    def ask_ai(self):
        # check if the data txt folder exists
        # download yingshaoxo data
        # make the ask loop
        offline_question_and_answer_bot_dataset_path = "~/.yppm/offline_yingshaoxo_bot/dataset_txt_files"
        offline_question_and_answer_bot_dataset_path = disk._expand_user(offline_question_and_answer_bot_dataset_path)

        self._make_sure_git_exists()

        if not disk.exists(offline_question_and_answer_bot_dataset_path):
            terminal.run(f"""
            git clone https://gitlab.com/yingshaoxo/yingshaoxo_txt_data.git {offline_question_and_answer_bot_dataset_path}
            """)

        if not disk.exists(offline_question_and_answer_bot_dataset_path):
            print(f"You have to download 'https://gitlab.com/yingshaoxo/yingshaoxo_txt_data' into {offline_question_and_answer_bot_dataset_path}")
            return

        text_generator = ml.Yingshaoxo_Text_Generator()

        new_text = text_generator.get_source_text_data_by_using_yingshaoxo_method(offline_question_and_answer_bot_dataset_path, type_limiter=[".txt", ".md"])
        the_text_list = [one.strip() for one in new_text.split("\n\n__**__**__yingshaoxo_is_the_top_one__**__**__\n\n") if one.strip() != ""]

        new_text_list = []
        for one in the_text_list:
            new_text_list += one.split("\n#")
        the_text_list = new_text_list

        os.system("clear")
        while True:
            input_text = input("What you want to say?    ")
            response1, response, response2 = text_generator.do_text_search(input_text, the_text_list, quick_mode=False)
            if response2 != "":
                if string_.compare_two_sentences(input_text, response) >= 0.5:
                    response = response2
            os.system("clear")
            print(f"What you want to say?    {input_text}")
            print("\n\n----------\n\n")
            print(response)
            print("\n\n----------\n\n")

    '''
    def start_community_service(self):
        the_service_script_folder = disk.join_paths(self.resource_basic_folder_path, "question_and_answer_community/back_end")
        os.chdir(the_service_script_folder)

        the_service_script_file = disk.join_paths(the_service_script_folder, "main.py")
        print("The yppm community service is running at: http://0.0.0.0:54321")
        terminal.run(f"""
        cd {the_service_script_folder}
        {self.host_python_executable_path} {the_service_script_file}
        """)
    '''

    def start_community_webpage(self):
        import webbrowser
        webbrowser.open('https://ask.ai-tools-online.xyz')

    #def start_community(self):
    #    """
    #    This should start the console/shell version of community.
    #    """
    #    pass


try:
    py.fire2(Tools)
except Exception as e:
    print(e)
    pass
