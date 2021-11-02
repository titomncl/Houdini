import os
import sys

from CommonTools.save_load.controller import Controller

if sys.version_info > (3,):
    import typing

    if typing.TYPE_CHECKING:
        from Odin import Asset, Shot
        from typing import Optional, Union

from collections import OrderedDict

from CommonTools.concat import concat

from Houdini.globals import PROJECT_PATH, ROOT_PATH, PROJECT, HOU_EXT
from Houdini.common_ import get_filepath, save_as, open_file, import_filepath, get_main_window


class Core(object):

    @property
    def root(self):
        return ROOT_PATH

    @property
    def project(self):
        return PROJECT

    @property
    def filepath(self):
        try:
            filepath_ = get_filepath()
            if PROJECT_PATH not in filepath_:
                return None
            else:
                return filepath_
        except RuntimeError:
            return None

    @property
    def buttons(self):
        buttons = OrderedDict()

        buttons["Assets"] = ["MOD", "CAMERA"]

        buttons["Shots"] = ["ANIMATION", "LAYOUT", "LIGHTING", "COMPOSITING", "FX"]

        return buttons

    @staticmethod
    def next_version(file_):
        """
        Get the next version from the given file
        Args:
            file_:

        Raises:
            ValueError: if the filename is not correct

        Returns:
            str: file with last version

        """
        split_file = file_.rsplit("_", 1)
        name_file = split_file[0]
        version = split_file[-1]
        padding = len(version)

        if version.isdigit():
            next_version = int(version) + 1
            next_version = str(next_version).zfill(padding)

            return concat(name_file, next_version, separator="_")
        else:
            e = concat(file_, " is incorrect.")
            raise ValueError(e)

    def file_to_load(self, path):

        last_file = self.get_last_file(path)

        filepath = concat(path, last_file, separator="/")

        return filepath

    @staticmethod
    def get_last_file(path):

        files = os.listdir(path)

        if files:

            last_file = files[-1]

            return last_file
        else:
            raise RuntimeError("No files found.")

    def load(self, item, dpt):
        if "FX" in item.paths["PUBLISH"]:
            path = os.path.join(item.paths["PUBLISH"], item.name).replace("\\", "/")
        else:
            path = os.path.join(item.paths["PUBLISH"], item.name, dpt).replace("\\", "/")

        if "MOD" in dpt:
            path = self.glob_recursive(path, "LD")
        else:
            path = self.glob_recursive(path, dpt)

        file_ = self.file_to_load(path)

        import_filepath(file_)

    def glob_recursive(self, path, endswith):
        for dir_path, dirs, _ in os.walk(path):
            for dir in dirs:
                file_path = os.path.join(dir_path, dir).replace("\\", "/")
                if file_path.endswith(endswith):
                    return file_path


def main():
    core = Core()

    _ = Controller(core.load, "Import", get_main_window(),
                          Core().root, Core().project, Core().buttons)
