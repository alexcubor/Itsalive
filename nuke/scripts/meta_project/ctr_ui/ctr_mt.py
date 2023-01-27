from PySide2.QtWidgets import QWidget

from prg_ui.wui_mt import Ui_Form
class bah_mt(QWidget):
    def __init__(self, parent=None):
        super(bah_mt, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        print(self.ui.widget)
        # self.ui.label_task.setStyleSheet("QLabel{border: None;}")