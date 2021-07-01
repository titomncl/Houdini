from qtpy import QtWidgets as Qw
from qtpy import QtCore as Qc


class UI(Qw.QWidget):
    def __init__(self, controller, parent=None):
        """

        Args:
            controller (Controller):
            parent (Qw.QMainWindow):
        """

        Qw.QWidget.__init__(self, parent)

        self.setParent(parent)
        self.setWindowFlags(Qc.Qt.Tool)

        self.setWindowTitle("Save File")

        self.controller = controller

        self.set_ui()

    def set_ui(self):

        self.setFixedSize(400, 250)

        main_layout = Qw.QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        main_layout.addLayout(self.type_layout())
        main_layout.addSpacerItem(Qw.QSpacerItem(200, 4))
        main_layout.addLayout(self.library_layout())
        main_layout.addSpacerItem(Qw.QSpacerItem(200, 4))
        main_layout.addLayout(self.department_layout())
        main_layout.addSpacerItem(Qw.QSpacerItem(200, 20))
        main_layout.addLayout(self.save_close_layout())

        self.setLayout(main_layout)

    def type_layout(self):

        h_layout = Qw.QHBoxLayout()

        self.chara_btn = Qw.QPushButton("CHARA")
        self.chara_btn.setCheckable(True)
        self.chara_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        self.props_btn = Qw.QPushButton("PROPS")
        self.props_btn.setCheckable(True)
        self.props_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        self.set_btn = Qw.QPushButton("SET")
        self.set_btn.setCheckable(True)
        self.set_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        self.fx_btn = Qw.QPushButton("FX")
        self.fx_btn.setCheckable(True)
        self.fx_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)
        self.fx_btn.setEnabled(False)  # TODO talk with teddy about workflow with cache files

        h_layout.addWidget(self.chara_btn)
        h_layout.addWidget(self.props_btn)
        h_layout.addWidget(self.set_btn)
        h_layout.addWidget(self.fx_btn)

        v_layout = Qw.QVBoxLayout()

        label = Qw.QLabel("Character, Props, Set or FX:")

        v_layout.addWidget(label)
        v_layout.addLayout(h_layout)

        return v_layout

    def department_layout(self):

        h_layout = Qw.QHBoxLayout()

        self.mod_btn = Qw.QPushButton("MOD")
        self.mod_btn.setCheckable(True)
        self.mod_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        self.shd_btn = Qw.QPushButton("SHD")
        self.shd_btn.setCheckable(True)
        self.shd_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        self.rig_btn = Qw.QPushButton("RIG")
        self.rig_btn.setCheckable(True)
        self.rig_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Expanding)

        h_layout.addWidget(self.mod_btn)
        h_layout.addWidget(self.shd_btn)
        h_layout.addWidget(self.rig_btn)

        v_layout = Qw.QVBoxLayout()

        label = Qw.QLabel("Department:")

        v_layout.addWidget(label)
        v_layout.addLayout(h_layout)

        return v_layout

    def library_layout(self):

        v_layout = Qw.QVBoxLayout()

        label = Qw.QLabel("Asset:")

        self.library_combobox = Qw.QComboBox()
        self.library_combobox.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Ignored)
        self.library_combobox.setMinimumSize(0, 25)

        v_layout.addWidget(label)
        v_layout.addWidget(self.library_combobox)

        return v_layout

    def save_close_layout(self):

        h_layout = Qw.QHBoxLayout()

        self.save_btn = Qw.QPushButton("Save")
        self.save_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Fixed)

        self.close_btn = Qw.QPushButton("Close")
        self.close_btn.setSizePolicy(Qw.QSizePolicy.Expanding, Qw.QSizePolicy.Fixed)

        h_layout.addWidget(self.save_btn)
        h_layout.addSpacerItem(Qw.QSpacerItem(10, 1))
        h_layout.addWidget(self.close_btn)

        return h_layout

    def message_box(self):

        save_choice = Qw.QMessageBox.Save

        msg_box = Qw.QMessageBox(self)
        msg_box.setWindowTitle("Save")
        msg_box.setText("The file will be saved.")
        msg_box.setInformativeText("Do you want to continue?")
        msg_box.setStandardButtons(Qw.QMessageBox.Save | Qw.QMessageBox.Cancel)
        msg_box.setDefaultButton(Qw.QMessageBox.Save)

        choice = msg_box.exec_()

        return choice, save_choice
