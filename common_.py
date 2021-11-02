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


def add_abc_node(node_name):
    network_editor = hou.ui.curDesktop().paneTabOfType(hou.paneTabType.NetworkEditor)

    return network_editor.pwd().createNode("rop_alembic", node_name)


def get_frame_range():
    frame_in, frame_out = hou.playbar.frameRange()
    return int(frame_in), int(frame_out)


def set_frame_range(frame_in, frame_out):
    hou.playbar.setFrameRange(int(frame_in), int(frame_out))
    hou.playbar.setPlaybackRange(int(frame_in), int(frame_out))


def import_filepath(path):
    network_editor = hou.ui.curDesktop().paneTabOfType(hou.paneTabType.NetworkEditor)
    import_node = network_editor.currentNode()

    import_node.parm("filepath").set(path)
