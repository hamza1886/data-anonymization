import sys

from PyQt5 import QtWidgets

from Home import Ui_HomeWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    home_window = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setup_ui(home_window)
    home_window.show()
    sys.exit(app.exec())
