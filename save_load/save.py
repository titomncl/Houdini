from CommonTools.save_load.controller import Controller

from Houdini.save_load.save_load import SaveLoad
from Houdini.common_ import get_main_window
from Houdini.globals import ROOT_PATH, PROJECT


def main():
    save_load = SaveLoad()
    if save_load.filepath:
        save_load.save()
    else:
        instance = Controller(save_load.save, "Save", get_main_window(), ROOT_PATH, PROJECT)
