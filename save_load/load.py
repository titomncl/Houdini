from CommonTools.save_load.controller import Controller
from Houdini.save_load.save_load import SaveLoad
from Houdini.common_ import get_main_window
from Houdini.globals import ROOT_PATH, PROJECT


def main():

    instance = Controller(SaveLoad().load, "Load", get_main_window(), ROOT_PATH, PROJECT)
