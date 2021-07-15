from CommonTools.save_load.controller import Controller

from Houdini.save_load.save_load import SaveLoad
from Houdini.common_ import get_main_window


def main():

    instance = Controller(SaveLoad().load, "Load", get_main_window(),
                          SaveLoad().root, SaveLoad().project, SaveLoad().buttons)
