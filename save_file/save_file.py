import os

from CommonTools.concat import concat

from Houdini.globals import PFE_PATH, ROOT_PATH, PROJECT, HOU_EXT
from Houdini.common_ import get_filepath, save_as, get_main_window


class SaveFile(object):

    def __init__(self):
        pass

    @property
    def root(self):
        return ROOT_PATH

    @property
    def project(self):
        return PROJECT

    @property
    def ui_instance(self):
        return get_main_window()

    @property
    def filepath(self):
        return self.__filepath()

    def __filepath(self):
        try:
            filepath_ = get_filepath()
            if PFE_PATH not in filepath_:
                return None
            else:
                return filepath_
        except RuntimeError:
            return None

    def save(self):

        path, _ = os.path.split(self.filepath)

        files = os.listdir(path)

        hou_files = [f for f in files if HOU_EXT in files]

        hou_files.sort()

        last_file, _ = os.path.splitext(files[-1])

        new_filename = self.next_version(last_file)
        new_filepath = concat(path, new_filename + HOU_EXT, separator="/")

        save_as(new_filepath)

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

    @staticmethod
    def first_save(type, name, task):
        """

        Args:
            type (str): chara, props, set
            name (str): name of the asset
            task (str): departement of the file: MOD, RIG, SHD, ANIM

        Returns:
            str, str: versionned and published filepath

        """
        filename = concat(name, task, "001.hip", separator="_")

        # if task is "FX":
        #     filepath = concat(PFE_PATH, "DATA/LIB", type, name, "SCENE/OLD", filename, separator="/")
        # else:
        #     filepath = concat(PFE_PATH, "DATA/LIB", type, name, task, "SCENE/OLD", filename, separator="/")
        filepath = concat(PFE_PATH, "DATA/LIB", type, name, task, "SCENE/VERSION", filename, separator="/")

        save_as(filepath)
