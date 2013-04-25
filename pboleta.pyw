#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from boletas import Ui_Form
import os
import shutil
from readxls import Readxls
from readxlsold import Readxlsold

class Principal(QtGui.QWidget):
	"""docstring for Principal"""
	def __init__(self):
		QtGui.QWidget.__init__(self)

		self.ventana = Ui_Form()
		self.ventana.setupUi(self)
		#self.ventana.setWindowTitle("Titulo de ventana")

		self.lista = []
		#Eventos
		self.connect(self.ventana.btnsalir, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'))
		self.connect(self.ventana.btnopen, QtCore.SIGNAL('clicked()'), self.open)
		self.connect(self.ventana.btnconvertir, QtCore.SIGNAL('clicked()'), self.read)
		self.connect(self.ventana.btnimprimir, QtCore.SIGNAL('clicked()'), self.imprimir)
		self.connect(self.ventana.btnformtold, QtCore.SIGNAL('clicked()'), self.read_old)
		#super(Principal, self).__init__()


	def open(self):
		filename = QtGui.QFileDialog.getOpenFileNames(self, 'Open File', 'F:\\')
		#listWidget = self.ventana.listarchivo
		if filename.isEmpty():
			#reply = QtGui.QMessageBox.question(self, 'Confirmacion de cierre de aplicacion',"Desea cerrar la aplicacion?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
			QMessageBox.warning(self, "Mensaje","No se ha seleccionado un archivo!!!")
		else:
			self.ventana.listarchivo.clear()
			cstatus = ""
			ar = ""
			listaf = []
			dst = os.getcwd()
			dst = dst+"/file-v1/"
			for fn in filename:
				listaf.append(str(fn))
				cstatus += fn +'\r\n'

			for f in listaf:
				dst = dst+os.path.basename(f)
				shutil.copyfile(f,dst)
				dst = os.getcwd()
				dst = dst+"/file-v1/"
				item = QListWidgetItem("%s" % os.path.basename(f))
				self.lista.append(os.path.basename(f))
				self.ventana.listarchivo.addItem(item)
				ar += os.path.basename(f)+", "

			self.ventana.txtstatus.setText(cstatus)
			self.ventana.txtarchivos.setText(ar)
			del listaf
		#print type(filename)

	def read(self):
		if len(self.lista) > 0:
			cadpre = ''
			cadpre = self.ventana.txtstatus.toPlainText()
			cadpre = cadpre + '\r\n' + 'Iniciando la lectura de los archivos ....'
			self.ventana.txtstatus.setText(cadpre)
			self.readxls = Readxls()
			self.readxls.read_xls(self.lista)
			cadpost = self.ventana.txtstatus.toPlainText() + '\r\n' + 'Se termino de leer los archivos ....'
			self.ventana.txtstatus.setText(cadpost)
			self.lista = []
		else:
			QMessageBox.warning(self, "Mensaje","No existe un archivo para ser recorrido!!")
			pass

	def read_old(self):
		if len(self.lista) > 0:
			cadpre = ''
			cadpre = self.ventana.txtstatus.toPlainText()
			cadpre = cadpre + '\r\n' + 'Iniciando la lectura de los archivos ....'
			self.ventana.txtstatus.setText(cadpre)
			self.readxls = Readxlsold()
			self.readxls.read_xls(self.lista)
			cadpost = self.ventana.txtstatus.toPlainText() + '\r\n' + 'Se termino de leer los archivos ....'
			self.ventana.txtstatus.setText(cadpost)
			self.lista = []
		else:
			QMessageBox.warning(self, "Mensaje","No existe un archivo para ser recorrido!!")
			pass

	def imprimir(self):
		self.ventana.txtstatus.setText(self.ventana.txtstatus.toPlainText()+'\r\n'+'salio del dialogo de impresion')
		rjava = -1
		rjava = os.system('java -version')
		if rjava == 0:
			#QtGui.QMessageBox.information(self, 'Mensaje',"Bien de vuelta a Java", QtGui.QMessageBox.Ok)
			path_mod = os.getcwd()
			path_mod += '/module/'
			self.ventana.txtstatus.setText(self.ventana.txtstatus.toPlainText()+'\r\n'+'salio del dialogo de impresion')
			java = os.system("java -jar "+path_mod+'PrinterFiles.jar')
		else:
			QtGui.QMessageBox.information(self, 'Mensaje',"La maquina virtual de Java no esta instalada\r\n y es necesaria.", QtGui.QMessageBox.Ok)
			pass


def main():
	app = QtGui.QApplication(sys.argv)
	ventana = Principal()
	ventana.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()