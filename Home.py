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
    def setup_ui(self, window):
        self.home_window = window
        if not self.home_window.objectName():
            self.home_window.setObjectName("home_window")

        self.home_window.resize(681, 536)
        self.central_widget = QtWidgets.QWidget(self.home_window)
        self.central_widget.setObjectName("central_widget")

        fixed_width_font = QtGui.QFont()
        fixed_width_font.setPointSize(8)
        fixed_width_font.setFamily('Courier New')

        self.help_button = QtWidgets.QPushButton(self.central_widget)
        self.help_button.setGeometry(QtCore.QRect(580, 10, 80, 25))
        self.help_button.setObjectName("help_button")
        self.help_button.clicked.connect(self.help_button_click_handler)

        self.example_input_button = QtWidgets.QPushButton(self.central_widget)
        self.example_input_button.setGeometry(QtCore.QRect(550, 60, 111, 25))
        self.example_input_button.setObjectName("example_input_button")
        self.example_input_button.clicked.connect(self.example_input_button_click_handler)

        self.radio_button_1 = QtWidgets.QRadioButton(self.central_widget)
        self.radio_button_1.setGeometry(QtCore.QRect(20, 60, 401, 25))
        self.radio_button_1.setObjectName("radio_button_1")
        self.radio_button_1.input_type = 'sequence'
        self.radio_button_1.setChecked(True)
        self.radio_button_1.toggled.connect(self.radio_button_click_handler)

        self.radio_button_2 = QtWidgets.QRadioButton(self.central_widget)
        self.radio_button_2.setGeometry(QtCore.QRect(20, 250, 401, 25))
        self.radio_button_2.setObjectName('radio_button_2')
        self.radio_button_2.input_type = 'file'
        self.radio_button_2.toggled.connect(self.radio_button_click_handler)

        self.input_text = QtWidgets.QTextEdit(self.central_widget)
        self.input_text.setGeometry(QtCore.QRect(20, 90, 641, 141))
        self.input_text.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.input_text.setFont(fixed_width_font)
        self.input_text.setObjectName("input_text")
        self.input_text.textChanged.connect(self.input_text_changed_handler)

        self.input_path = QtWidgets.QLabel(self.central_widget)
        self.input_path.setGeometry(QtCore.QRect(20, 280, 641, 25))
        self.input_path.setObjectName("input_path")

        self.choose_file_button = QtWidgets.QPushButton(self.central_widget)
        self.choose_file_button.setGeometry(QtCore.QRect(550, 250, 111, 25))
        self.choose_file_button.setObjectName("choose_input_file")
        self.choose_file_button.clicked.connect(self.choose_file_button_click_handler)
        self.choose_file_button.setDisabled(True)

        self.output_label = QtWidgets.QLabel(self.central_widget)
        self.output_label.setGeometry(QtCore.QRect(20, 310, 641, 25))
        self.output_label.setObjectName("output_label")

        self.output_text = QtWidgets.QTextEdit(self.central_widget)
        self.output_text.setGeometry(QtCore.QRect(20, 340, 641, 141))
        self.output_text.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.output_text.setFont(fixed_width_font)
        self.output_text.setObjectName("output_text")
        self.output_text.setReadOnly(True)

        self.clear_form_button = QtWidgets.QPushButton(self.central_widget)
        self.clear_form_button.setGeometry(QtCore.QRect(20, 490, 111, 25))
        self.clear_form_button.setObjectName("clear_form_button")
        self.clear_form_button.clicked.connect(self.clear_form_button_click_handler)
        self.clear_form_button.setDisabled(True)

        self.encrypt_button = QtWidgets.QPushButton(self.central_widget)
        self.encrypt_button.setGeometry(QtCore.QRect(420, 490, 111, 25))
        self.encrypt_button.setObjectName("encrypt_button")
        self.encrypt_button.clicked.connect(self.encrypt_button_click_handler)
        self.encrypt_button.setDisabled(True)

        self.decrypt_button = QtWidgets.QPushButton(self.central_widget)
        self.decrypt_button.setGeometry(QtCore.QRect(550, 490, 111, 25))
        self.decrypt_button.setObjectName("decrypt_button")
        self.decrypt_button.clicked.connect(self.decrypt_button_click_handler)
        self.decrypt_button.setDisabled(True)

        self.menu_bar = QtWidgets.QMenuBar(self.home_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 681, 20))
        self.menu_bar.setObjectName("menu_bar")
        self.home_window.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(self.home_window)
        self.status_bar.setObjectName("status_bar")
        self.home_window.setStatusBar(self.status_bar)

        self.home_window.setCentralWidget(self.central_widget)
        self.translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.home_window)

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate

        self.home_window.setWindowTitle(_translate("home_window", "Data Anonymization"))
        self.help_button.setText(_translate("home_window", "Help"))
        self.example_input_button.setText(_translate("home_window", "Example input"))
        self.radio_button_1.setText(_translate("home_window", "Input text to encrypt"))
        self.radio_button_2.setText(_translate("home_window", "Upload file from your computer"))
        self.choose_file_button.setText(_translate("home_window", "Choose File"))
        self.output_label.setText(_translate("home_window", "Output"))
        self.clear_form_button.setText(_translate("home_window", "Clear form"))
        self.encrypt_button.setToolTip(_translate("home_window", "Click to encrypt data"))
        self.encrypt_button.setText(_translate("home_window", "Encrypt"))
        self.decrypt_button.setToolTip(_translate("home_window", "Click to decrypt data"))
        self.decrypt_button.setText(_translate("home_window", "Decrypt"))

    def input_text_changed_handler(self):
        is_disabled = self.input_text.toPlainText().strip() == '' and self.input_path.text().strip() == ''
        self.encrypt_button.setDisabled(is_disabled)
        self.decrypt_button.setDisabled(is_disabled)

        has_content = self.input_text.toPlainText().strip() != '' or self.input_path.text().strip() != ''
        self.clear_form_button.setDisabled(not has_content)

    def radio_button_click_handler(self):
        if self.radio_button_1.isChecked():
            self.input_text.setDisabled(False)
            self.input_path.setDisabled(True)
            self.choose_file_button.setDisabled(True)
        elif self.radio_button_2.isChecked():
            self.input_text.setDisabled(True)
            self.input_path.setDisabled(False)
            self.choose_file_button.setDisabled(False)

    def help_button_click_handler(self):
        # TODO: replace with GitHub wiki url
        url = Qt.QUrl('https://www.google.com')
        Qt.QDesktopServices.openUrl(url)

    def example_input_button_click_handler(self):
        self.input_text.setText('hello')

    def clear_form_button_click_handler(self):
        self.input_text.setText('')
        self.input_path.setText('')
        self.output_text.setText('')

    def choose_file_button_click_handler(self):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(caption='Select .txt file containing input text', filter='*.txt')
        self.input_path.setText(filename)

        if not filename:
            QtWidgets.QMessageBox.about(QtWidgets.QMessageBox(), "Warning", "Please select a valid .txt file")
            return

        with open(filename, 'r') as f:
            sequence = f.read()
            self.input_text.setText(sequence)

    def encrypt_button_click_handler(self):
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

        self.output_text.setText(hexadecimal)

    def decrypt_button_click_handler(self):
        self.window = QtWidgets.QMainWindow()
        # self.ui = Ui_SearchTemplate(self.window, seq_id)
        self.ui.setup_ui()
        self.home_window.hide()
        self.window.setWindowTitle('Search Template - Bio-GATS')
        self.window.show()
