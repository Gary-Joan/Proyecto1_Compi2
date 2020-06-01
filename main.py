# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Augus.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow


class Ui_MainWindow(QMainWindow):

    def __init__(self):
       QMainWindow.__init__(self)
       self.filename = ""

    def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 981, 401))
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 410, 91, 16))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 430, 981, 161))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 26))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuEjecutar = QtWidgets.QMenu(self.menubar)
        self.menuEjecutar.setObjectName("menuEjecutar")
        self.menuEjecutar_Ascedente = QtWidgets.QMenu(self.menuEjecutar)
        self.menuEjecutar_Ascedente.setObjectName("menuEjecutar_Ascedente")
        self.menuOpciones = QtWidgets.QMenu(self.menubar)
        self.menuOpciones.setObjectName("menuOpciones")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_Como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionCerrar = QtWidgets.QAction(MainWindow)
        self.actionCerrar.setObjectName("actionCerrar")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCopiar = QtWidgets.QAction(MainWindow)
        self.actionCopiar.setObjectName("actionCopiar")
        self.actionCortar = QtWidgets.QAction(MainWindow)
        self.actionCortar.setObjectName("actionCortar")
        self.actionPegar = QtWidgets.QAction(MainWindow)
        self.actionPegar.setObjectName("actionPegar")
        self.actionBuscar = QtWidgets.QAction(MainWindow)
        self.actionBuscar.setObjectName("actionBuscar")
        self.actionReemplazar = QtWidgets.QAction(MainWindow)
        self.actionReemplazar.setObjectName("actionReemplazar")
        self.actionEjecutar = QtWidgets.QAction(MainWindow)
        self.actionEjecutar.setObjectName("actionEjecutar")
        self.actionEjecutar_Paso_a_Paso = QtWidgets.QAction(MainWindow)
        self.actionEjecutar_Paso_a_Paso.setObjectName("actionEjecutar_Paso_a_Paso")
        self.actionCambiar_Fondo = QtWidgets.QAction(MainWindow)
        self.actionCambiar_Fondo.setObjectName("actionCambiar_Fondo")
        self.actionQuitar_Numeros = QtWidgets.QAction(MainWindow)
        self.actionQuitar_Numeros.setObjectName("actionQuitar_Numeros")
        self.actionAyuda = QtWidgets.QAction(MainWindow)
        self.actionAyuda.setObjectName("actionAyuda")
        self.actionAcerca_De = QtWidgets.QAction(MainWindow)
        self.actionAcerca_De.setObjectName("actionAcerca_De")

        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionCerrar)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuEditar.addAction(self.actionCopiar)
        self.menuEditar.addAction(self.actionCortar)
        self.menuEditar.addAction(self.actionPegar)
        self.menuEditar.addAction(self.actionBuscar)
        self.menuEditar.addAction(self.actionReemplazar)
        self.menuEjecutar_Ascedente.addAction(self.actionEjecutar)
        self.menuEjecutar_Ascedente.addAction(self.actionEjecutar_Paso_a_Paso)
        self.menuEjecutar.addAction(self.menuEjecutar_Ascedente.menuAction())
        self.menuOpciones.addAction(self.actionCambiar_Fondo)
        self.menuOpciones.addAction(self.actionQuitar_Numeros)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuAyuda.addAction(self.actionAcerca_De)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuEjecutar.menuAction())
        self.menubar.addAction(self.menuOpciones.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Augus Intepreter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label.setText(_translate("MainWindow", "Consola/Output"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))
        self.menuEjecutar.setTitle(_translate("MainWindow", "Ejecutar"))
        self.menuEjecutar_Ascedente.setTitle(_translate("MainWindow", "Ejecutar Ascedente"))
        self.menuOpciones.setTitle(_translate("MainWindow", "Opciones"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))

        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))

        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionAbrir.setShortcut("Ctrl+O")
        self.actionAbrir.triggered.connect(self.open)

        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar.setStatusTip("Save document")
        self.actionGuardar.setShortcut("Ctrl+S")
        self.actionGuardar.triggered.connect(self.save)

        self.actionGuardar_Como.setText(_translate("MainWindow", "Guardar Como.."))
        self.actionCerrar.setText(_translate("MainWindow", "Cerrar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionCopiar.setText(_translate("MainWindow", "Copiar"))
        self.actionCortar.setText(_translate("MainWindow", "Cortar"))
        self.actionPegar.setText(_translate("MainWindow", "Pegar"))
        self.actionBuscar.setText(_translate("MainWindow", "Buscar"))
        self.actionReemplazar.setText(_translate("MainWindow", "Reemplazar"))
        self.actionEjecutar.setText(_translate("MainWindow", "Ejecutar"))
        self.actionEjecutar_Paso_a_Paso.setText(_translate("MainWindow", "Ejecutar Paso a Paso"))
        self.actionCambiar_Fondo.setText(_translate("MainWindow", "Cambiar Fondo"))
        self.actionQuitar_Numeros.setText(_translate("MainWindow", "Quitar Numeros"))
        self.actionAyuda.setText(_translate("MainWindow", "Ayuda"))
        self.actionAcerca_De.setText(_translate("MainWindow", "Acerca De.."))

    def open(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.txt)")

        if self.filename[0]:
            # Read a file
            with open(self.filename[0], "rt") as in_file:
               print(in_file.read())

    def save(self):

        # Only open dialog if there is no filename yet
        if not self.filename:
          self.filename = QFileDialog.getSaveFileName(self, 'Save File')

        # Append extension if not there yet
        if not self.filename.endswith(".txt"):
          self.filename += ".txt"

        # We just store the contents of the text file along with the
        # format in html, which Qt does in a very nice way for us
        with open(self.filename,"wt") as file:
            file.write(self.text.toHtml())

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
