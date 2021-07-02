import hou


def get_main_window():
    """
    Get the main window instance

    Returns:
        PySide2.QtWidgets.QMainWindow: main houdini window instance

    """
    hou.session.mainWindow = main_window = hou.qt.mainWindow()

    return main_window


def kill_instance(title):
    from qtpy.QtWidgets import QWidget

    main_window = get_main_window()

    for win in main_window.findChildren(QWidget, title):
        win.close()


def get_filepath():
    """
    Get the filepath of the scene

    Returns:
        str: filepath

    """
    filepath = hou.hipFile.path()

    if 'untitled' in filepath:
        raise RuntimeError("File not saved")
    else:
        return filepath


def save_as(filepath):
    """

    Args:
        filepath (str): path/filename.hip

    """
    hou.hipFile.save(file_name=filepath)


def open_file(filepath):
    """

    Args:
        filepath (str): path/filename.hip

    Returns:

    """
    hou.hipFile.load(file_name=filepath)
