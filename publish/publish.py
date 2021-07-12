import os

from shutil import copyfile

from CommonTools.concat import concat

from Houdini.globals import PROJECT_PATH, HOU_EXT
from Houdini.common_ import get_filepath, save_as


def filepath():
    try:
        filepath_ = get_filepath()
        if PFE_PATH not in filepath_:
            return None
        return filepath_
    except RuntimeError:
        return None


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
        next_version_ = int(version) + 1
        next_version_ = str(next_version_).zfill(padding)

        return concat(name_file, next_version_, separator="_")
    else:
        e = concat(file_, " is incorrect.")
        raise ValueError(e)


def get_last_file(path):

    files = os.listdir(path)

    if files:

        maya_files = [f for f in files if HOU_EXT in f]

        maya_files.sort()

        last_file = maya_files[-1]

        return last_file
    else:
        raise RuntimeError("No files found.")


def save(filepath_):

    path, _ = os.path.split(filepath_)

    file_ = get_last_file(path)

    last_file, _ = os.path.splitext(file_)

    new_filename = next_version(last_file)
    new_filepath = concat(path, new_filename + HOU_EXT, separator="/")

    save_as(new_filepath)

    return new_filepath


def publish(filepath_):
    path, name = os.path.split(filepath_)

    publish_path = path.rsplit("/", 1)[0]
    publish_path = concat(publish_path, "PUBLISH", separator="/")

    name, ext = os.path.splitext(name)
    publish_name = name.rsplit("_", 1)[0] + ext

    publish_ = concat(publish_path, publish_name, separator="/")

    copyfile(filepath_, publish_)


def save_and_publish():
    filepath_ = get_filepath()

    if filepath_:
        filepath_ = save(filepath_)
        publish(filepath_)
