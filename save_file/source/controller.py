from Houdini.save_file.source import core
from Houdini.common_ import clean_mode
from Houdini.globals import PROJECT, ROOT_PATH

from Odin.source.core import assets
# try:
#     import ipm_v2
# except ImportError:
#     import sys
#     sys.path.append(USER_PATH + '/ISART_PROJECT_MANAGER/PY/')
#
#     import ipm_v2

class Controller(object):

    def __init__(self, ui, parent=None):

        self.filepath = core.filepath()

        self.ui = ui(self, parent)

        self.asset_type = "CHARA"
        self.asset_name = ""
        self.dpt = "MOD"

        self.chara_btn = self.ui.chara_btn
        self.props_btn = self.ui.props_btn
        self.mod_btn = self.ui.mod_btn
        self.shd_btn = self.ui.shd_btn
        self.set_btn = self.ui.set_btn
        self.save_btn = self.ui.save_btn
        self.close_btn = self.ui.close_btn

        self.library_box = self.ui.library_combobox

        self.get_asset(self.asset_type)
        self.update_asset_name()

        self.chara_btn.setChecked(True)
        self.props_btn.setChecked(False)
        self.mod_btn.setChecked(True)
        self.shd_btn.setChecked(False)
        self.set_btn.setChecked(False)

        self.init_btn_connections()

        self.first_save_or_not()

    def first_save_or_not(self):
        if not self.filepath:
            self.show()
        else:
            self.save_file(first_save=False)

    def show(self):
        self.ui.show()

    def save_file(self, first_save=True):

        choice, save_choice = self.ui.message_box()
        if choice == save_choice:
            clean_mode()
            if first_save:
                self.filepath = core.first_save(self.asset_type, self.asset_name, self.dpt)
            else:
                self.filepath = core.save(self.filepath)
            self.ui.close()

    def init_btn_connections(self):
        self.chara_btn.clicked.connect(self.chara_action)
        self.props_btn.clicked.connect(self.props_action)
        self.mod_btn.clicked.connect(self.mod_action)
        self.shd_btn.clicked.connect(self.shd_action)
        self.set_btn.clicked.connect(self.set_action)

        self.library_box.currentTextChanged.connect(self.update_asset_name)

        self.save_btn.clicked.connect(self.save_file)
        self.close_btn.clicked.connect(self.close_action)

    def chara_action(self):
        self.chara_btn.setChecked(True)
        self.props_btn.setChecked(False)
        self.asset_type = "CHARA"
        self.get_asset(self.asset_type)

    def props_action(self):
        self.props_btn.setChecked(True)
        self.chara_btn.setChecked(False)
        self.asset_type = "PROPS"
        self.get_asset(self.asset_type)

    def get_asset(self, asset_type):
        assets = assets.find_assets(ROOT_PATH, PROJECT, asset_type)
        if assets:
            assets.sort()

            self.library_box.clear()
            self.library_box.addItems(assets)


    def mod_action(self):
        self.mod_btn.setChecked(True)
        self.shd_btn.setChecked(False)
        self.set_btn.setChecked(False)

        self.dpt = "MOD"

    def shd_action(self):
        self.shd_btn.setChecked(True)
        self.mod_btn.setChecked(False)
        self.set_btn.setChecked(False)

        self.dpt = "SHD"

    def set_action(self):
        self.set_btn.setChecked(True)
        self.shd_btn.setChecked(False)
        self.mod_btn.setChecked(False)

        self.dpt = "SET"

    def update_asset_name(self):
        self.asset_name = self.library_box.currentText()

    def close_action(self):
        self.ui.close()
