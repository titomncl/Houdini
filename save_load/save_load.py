import os

from CommonTools.concat import concat

from Houdini.globals import PFE_PATH, ROOT_PATH, PROJECT, HOU_EXT
from Houdini.common_ import get_filepath, save_as, open_file


class SaveLoad(object):

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
            if PFE_PATH not in filepath_:
                return None
            else:
                return filepath_
        except RuntimeError:
            return None

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

    def file_to_load(self, type_, name, task):

        filepath = concat(PFE_PATH, "DATA/LIB", type_, name, task, "SCENE/VERSION", separator="/")

        last_file = self.get_last_file(filepath)

        filepath = concat(filepath, last_file, separator="/")

        return filepath

    @staticmethod
    def get_last_file(path):

        files = os.listdir(path)

        if files:

            maya_files = [f for f in files if HOU_EXT in f]

            maya_files.sort()

            last_file = maya_files[-1]

            return last_file
        else:
            raise RuntimeError("No files found.")

    def save(self, type_, name_, task_):
        """
        Args:
            type_ (str): chara, props, set
            name_ (str): name of the asset
            task_ (str): departement of the file: MOD, RIG, SHD, ANIM

        Returns:
            str, str: versionned and published filepath

        """

        if self.filepath:
            path, _ = os.path.split(self.filepath)

            files = os.listdir(path)

            file = self.get_last_file(files)

            last_file, _ = os.path.splitext(file)

            new_filename = self.next_version(last_file)
            new_filepath = concat(path, new_filename + HOU_EXT, separator="/")

            save_as(new_filepath)
        else:
            filename = concat(name_, task_, "001" + HOU_EXT, separator="_")

            # if task is "FX":
            #     filepath = concat(PFE_PATH, "DATA/LIB", type, name, "SCENE/OLD", filename, separator="/")
            # else:
            #     filepath = concat(PFE_PATH, "DATA/LIB", type, name, task, "SCENE/OLD", filename, separator="/")
            filepath = concat(PFE_PATH, "DATA/LIB", type_, name_, task_, "SCENE/VERSION", filename, separator="/")

            save_as(filepath)

    def load(self, type_, name_, task_):
        file = self.file_to_load(type_, name_, task_)

        open_file(file)
