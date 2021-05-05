import sys
from PyQt5 import QtWidgets

from Home import Ui_HomeWindow


if __name__ == '__main__':
    # input_str = input('Enter text to encrypt: ')
    # encrypt_str(input_str)

    app = QtWidgets.QApplication(sys.argv)
    HomeWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow(HomeWindow)
    ui.setup_ui()
    HomeWindow.show()
    HomeWindow.setWindowTitle('Data Anonymization')
    sys.exit(app.exec())
