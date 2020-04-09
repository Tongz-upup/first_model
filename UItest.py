
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from modelone import Ui_MainWindow
#from export import  login


class MyDesiger(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyDesiger, self).__init__(parent)
        self.setupUi(self)
        #self.Button_export.clicked.connect(self.display)
    #def display(self):
        #self.textBrowser.setText("成功？")
        #login()
    def export_test(self):
        #export.login()
        self.textBrowser.setText("成功？")


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)#保证qt designer预览界面和运行结果一致
    app = QApplication(sys.argv)
    ui = MyDesiger()
    ui.show()
    sys.exit(app.exec_())


