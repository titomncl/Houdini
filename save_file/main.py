import hou

from Houdini.save_file.source.ui import UI
from Houdini.save_file.source.controller import Controller


def main():

    hou.session.mainWindow = main_window = hou.qt.mainWindow()

    for child in main_window.children():
        print(child, child.objectName())

    for win in main_window.findChildren(Qw.QWidget, name):
        win.close()

    instance = Controller(UI, main_window)


if __name__ == '__main__':
    main()
