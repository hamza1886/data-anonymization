# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import binascii
import os

import pbkdf2
from Crypto.Cipher import AES
from PyQt5 import Qt, QtCore, QtGui, QtWidgets


class Ui_HomeWindow(object):
    def __init__(self, HomeWindow):
        self.home_window = HomeWindow

    def setup_ui(self):
        self.home_window.setObjectName("home_window")
        self.home_window.resize(859, 706)
        self.central_widget = QtWidgets.QWidget(self.home_window)
        self.central_widget.setObjectName("central_widget")

        font = QtGui.QFont()
        font.setPointSize(12)

        self.radio_button_1 = QtWidgets.QRadioButton(self.central_widget)
        self.radio_button_1.setGeometry(QtCore.QRect(130, 260, 401, 31))
        self.radio_button_1.setObjectName("radio_button_1")
        self.radio_button_1.input_type = 'sequence'
        self.radio_button_1.setChecked(True)
        self.radio_button_1.toggled.connect(self.on_clicked)

        self.input_path = QtWidgets.QLabel(self.central_widget)
        self.input_path.setGeometry(QtCore.QRect(130, 460, 321, 51))
        self.input_path.setObjectName("input_path")
        self.input_path.setDisabled(True)

        self.radio_button_2 = QtWidgets.QRadioButton(self.central_widget)
        self.radio_button_2.setGeometry(QtCore.QRect(130, 440, 401, 31))
        self.radio_button_2.setObjectName('radio_button_2')
        self.radio_button_2.input_type = 'file'
        self.radio_button_2.toggled.connect(self.on_clicked)

        self.choose_input_file = QtWidgets.QPushButton(self.central_widget)
        self.choose_input_file.setGeometry(QtCore.QRect(630, 460, 131, 31))
        self.choose_input_file.setObjectName("choose_input_file")
        self.choose_input_file.clicked.connect(self.choose_file)
        self.choose_input_file.setDisabled(True)

        self.encrypt_text = QtWidgets.QPushButton(self.central_widget)
        self.encrypt_text.setGeometry(QtCore.QRect(270, 580, 131, 31))
        self.encrypt_text.setObjectName("encrypt_text")
        self.encrypt_text.clicked.connect(self.encrypt)
        self.encrypt_text.setDisabled(True)

        self.decrypt_text = QtWidgets.QPushButton(self.central_widget)
        self.decrypt_text.setGeometry(QtCore.QRect(470, 580, 131, 31))
        self.decrypt_text.setObjectName("decrypt_text")
        self.decrypt_text.clicked.connect(self.decrypt)
        self.decrypt_text.setDisabled(True)

        self.clear_form = QtWidgets.QPushButton(self.central_widget)
        self.clear_form.setGeometry(QtCore.QRect(130, 520, 131, 31))
        self.clear_form.setObjectName("clear_form")
        self.clear_form.clicked.connect(self.clear)
        self.clear_form.setDisabled(True)

        self.example_input = QtWidgets.QPushButton(self.central_widget)
        self.example_input.setGeometry(QtCore.QRect(630, 250, 131, 31))
        self.example_input.setObjectName("example_input")
        self.example_input.clicked.connect(self.example)

        fixed_width_font = QtGui.QFont()
        fixed_width_font.setPointSize(10)
        fixed_width_font.setFamily('Courier New')

        self.input_text = QtWidgets.QTextEdit(self.central_widget)
        self.input_text.setGeometry(QtCore.QRect(130, 290, 641, 141))
        self.input_text.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.input_text.setFont(fixed_width_font)
        self.input_text.setObjectName("input_text")
        self.input_text.textChanged.connect(self.on_text_changed)

        self.help_button = QtWidgets.QPushButton(self.central_widget)
        self.help_button.setGeometry(QtCore.QRect(780, 10, 70, 23))
        self.help_button.setObjectName("help_button")
        self.help_button.clicked.connect(self.help_button_click_handler)

        self.menu_bar = QtWidgets.QMenuBar(self.home_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 859, 20))
        self.menu_bar.setObjectName("menubar")
        self.home_window.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(self.home_window)
        self.status_bar.setObjectName("statusbar")
        self.home_window.setStatusBar(self.status_bar)

        self.home_window.setCentralWidget(self.central_widget)
        self.translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.home_window)

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.home_window.setWindowTitle(_translate("home_window", "home_window"))
        self.radio_button_1.setText(_translate("home_window", "Input text to encrypt"))
        self.radio_button_2.setText(_translate("home_window", "Upload file from your computer"))
        self.choose_input_file.setText(_translate("home_window", "Choose File"))
        self.encrypt_text.setToolTip(_translate("home_window", "Click to encrypt data"))
        self.encrypt_text.setText(_translate("home_window", "Encrypt"))
        self.decrypt_text.setToolTip(_translate("home_window", "Click to decrypt data"))
        self.decrypt_text.setText(_translate("home_window", "Decrypt"))
        self.clear_form.setText(_translate("home_window", "Clear form"))
        self.example_input.setText(_translate("home_window", "Example input"))
        self.help_button.setText(_translate("home_window", "Help"))

    def on_text_changed(self):
        is_disabled = self.input_text.toPlainText().strip() == '' and self.input_path.text().strip() == ''
        self.encrypt_text.setDisabled(is_disabled)
        self.decrypt_text.setDisabled(is_disabled)

        has_content = self.input_text.toPlainText().strip() != '' or self.input_path.text().strip() != ''
        self.clear_form.setDisabled(not has_content)

    def on_clicked(self):
        if self.radio_button_1.isChecked():
            self.input_text.setDisabled(False)
            self.input_path.setDisabled(True)
            self.choose_input_file.setDisabled(True)
        elif self.radio_button_2.isChecked():
            self.input_text.setDisabled(True)
            self.input_path.setDisabled(False)
            self.choose_input_file.setDisabled(False)

    def help_button_click_handler(self):
        # TODO: replace with GitHub wiki url
        url = Qt.QUrl('https://www.google.com')
        Qt.QDesktopServices.openUrl(url)

    def example(self):
        self.input_text.setText('hello')

    def clear(self):
        self.input_text.setText('')
        self.input_path.setText('')

    def choose_file(self):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(caption='Select .txt file containing input text', filter='*.txt')
        self.input_path.setText(filename)

        if not filename:
            QtWidgets.QMessageBox.about(QtWidgets.QMessageBox(), "Warning", "Please select a valid .txt file")
            return

        with open(filename, 'r') as f:
            sequence = f.read()
            self.input_text.setText(sequence)

    def encrypt(self):
        scale = 16
        otp = ''
        num_of_bits = 8

        text = self.input_text.toPlainText().strip()
        if not text:
            QtWidgets.QMessageBox.about(QtWidgets.QMessageBox(), "Warning", "Please input data to encrypt")
            return

        text = text.encode()

        # changing the plaintext into hex encoded
        plaintext = binascii.hexlify(text).decode('ascii')
        plaintext_binary = bin(int(plaintext, scale))[2:].zfill(num_of_bits)

        # random 16-byte salt
        passwordSalt = os.urandom(16)

        # 100 iterations (about 100 ms), 32-byte output 32*8=256
        key_generate = pbkdf2.PBKDF2(text, passwordSalt, 100).read(32)

        # changing the key into hexadecimal value
        key = binascii.hexlify(key_generate).decode('ascii')
        key_binary = bin(int(key, scale))[2:].zfill(num_of_bits)
        aes_key = key[0:32].encode()

        for i in range(1, len(plaintext_binary) + 1):
            f = plaintext_binary[0:i - 1] + '' + key_binary[128:256 - i + 1]
            decimal_representation = int(f, 2)
            hexadecimal_string = hex(decimal_representation)
            hexadecimal_string = hexadecimal_string.encode()

            cipher = AES.new(aes_key, AES.MODE_EAX)
            rs = cipher.encrypt(hexadecimal_string)
            a = binascii.b2a_hex(rs).decode()
            k = bin(int(a, scale))[2:].zfill(num_of_bits)
            lsb_string = k[len(k) - 1]
            otp = otp + str(int(lsb_string) ^ (int(plaintext_binary[i - 1])))

        n = int(otp, 2)
        hexadecimal = hex(n)
        hexadecimal = hexadecimal.replace('0x', '')

        print('Hex value of ciphertext is', hexadecimal)

    def decrypt(self):
        self.window = QtWidgets.QMainWindow()
        # self.ui = Ui_SearchTemplate(self.window, seq_id)
        self.ui.setup_ui()
        self.home_window.hide()
        self.window.setWindowTitle('Search Template - Bio-GATS')
        self.window.show()