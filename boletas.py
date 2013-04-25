# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boletas.ui'
#
# Created: Tue Apr 23 10:52:16 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(642, 409)
        Form.setMinimumSize(QtCore.QSize(642, 409))
        Form.setMaximumSize(QtCore.QSize(642, 409))
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Peru))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 621, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtarchivos = QtGui.QLineEdit(self.groupBox)
        self.txtarchivos.setGeometry(QtCore.QRect(80, 30, 421, 20))
        self.txtarchivos.setObjectName(_fromUtf8("txtarchivos"))
        self.btnopen = QtGui.QPushButton(self.groupBox)
        self.btnopen.setGeometry(QtCore.QRect(510, 20, 101, 32))
        self.btnopen.setObjectName(_fromUtf8("btnopen"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 481, 201))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.listarchivo = QtGui.QListWidget(self.groupBox_2)
        self.listarchivo.setGeometry(QtCore.QRect(10, 20, 461, 171))
        self.listarchivo.setObjectName(_fromUtf8("listarchivo"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 300, 481, 101))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.txtstatus = QtGui.QTextEdit(self.groupBox_3)
        self.txtstatus.setEnabled(False)
        self.txtstatus.setGeometry(QtCore.QRect(10, 12, 471, 80))
        self.txtstatus.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);"))
        self.txtstatus.setObjectName(_fromUtf8("txtstatus"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(500, 100, 131, 301))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.btnconvertir = QtGui.QPushButton(self.groupBox_4)
        self.btnconvertir.setGeometry(QtCore.QRect(10, 30, 111, 32))
        self.btnconvertir.setObjectName(_fromUtf8("btnconvertir"))
        self.btnimprimir = QtGui.QPushButton(self.groupBox_4)
        self.btnimprimir.setGeometry(QtCore.QRect(10, 110, 111, 32))
        self.btnimprimir.setObjectName(_fromUtf8("btnimprimir"))
        self.btnclear = QtGui.QPushButton(self.groupBox_4)
        self.btnclear.setEnabled(False)
        self.btnclear.setGeometry(QtCore.QRect(10, 150, 111, 32))
        self.btnclear.setObjectName(_fromUtf8("btnclear"))
        self.btnsalir = QtGui.QPushButton(self.groupBox_4)
        self.btnsalir.setGeometry(QtCore.QRect(10, 260, 111, 32))
        self.btnsalir.setObjectName(_fromUtf8("btnsalir"))
        self.btnformtold = QtGui.QPushButton(self.groupBox_4)
        self.btnformtold.setGeometry(QtCore.QRect(10, 70, 111, 32))
        self.btnformtold.setObjectName(_fromUtf8("btnformtold"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Convertir Boletas de Pago", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Datos Generales", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Seleccione:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnopen.setText(QtGui.QApplication.translate("Form", "Abrir Archivos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Boletas de Pago", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Archivos Agregados", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Consola", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "Actiones", None, QtGui.QApplication.UnicodeUTF8))
        self.btnconvertir.setText(QtGui.QApplication.translate("Form", "Formato Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.btnimprimir.setText(QtGui.QApplication.translate("Form", "Imprimir", None, QtGui.QApplication.UnicodeUTF8))
        self.btnclear.setText(QtGui.QApplication.translate("Form", "Limpiar tmp", None, QtGui.QApplication.UnicodeUTF8))
        self.btnsalir.setText(QtGui.QApplication.translate("Form", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.btnformtold.setText(QtGui.QApplication.translate("Form", "Formato Antiguo", None, QtGui.QApplication.UnicodeUTF8))

