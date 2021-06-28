import hou

from PySide2 import QtWidgets as Qw

from Houdini.save_file.source.ui import UI
from Houdini.save_file.source.controller import Controller


def main():

    hou.session.mainWindow = main_window = hou.qt.mainWindow()

    for win in main_window.findChildren(Qw.QWidget, "SaveFile"):
        win.close()

    instance = Controller(UI, main_window)


if __name__ == '__main__':
    main()
