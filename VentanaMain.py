# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from QcoderEditor import *
from PyQt5.Qsci import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtGui import QColor, QFont, QTextCursor
import re
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox
import webbrowser as wb
import gramatica_asc as gr
import tablasimbolo as TS
import gramatica_descendente.gramatica_desc as gr_desc

from acciones import acciones
import sys
sys.setrecursionlimit(10**6)

class MyLexer(QsciLexerCustom):
    def __init__(self, parent):
        super(MyLexer, self).__init__(parent)
        # Default text settings
        # ----------------------
        self.setDefaultColor(QColor("#ff000000"))
        self.setDefaultPaper(QColor("#ffffffff"))
        self.setDefaultFont(QFont("Consolas", 8))

        # Initialize colors per style
        # ----------------------------
        self.setColor(QColor("#ff000000"), 0)   # Style 0: black
        self.setColor(QColor("#ff7f0000"), 1)   # Style 1: red
        self.setColor(QColor("#ff0000bf"), 2)   # Style 2: blue
        self.setColor(QColor("#ff007f00"), 3)   # Style 3: green

        # Initialize paper colors per style
        # ----------------------------------
        self.setPaper(QColor("#ffffffff"), 0)   # Style 0: white
        self.setPaper(QColor("#ffffffff"), 1)   # Style 1: white
        self.setPaper(QColor("#ffffffff"), 2)   # Style 2: white
        self.setPaper(QColor("#ffffffff"), 3)   # Style 3: white

        # Initialize fonts per style
        # ---------------------------
        self.setFont(QFont("Consolas", 8, weight=QFont.Bold), 0)   # Style 0: Consolas 14pt
        self.setFont(QFont("Consolas", 8, weight=QFont.Bold), 1)   # Style 1: Consolas 14pt
        self.setFont(QFont("Consolas", 8, weight=QFont.Bold), 2)   # Style 2: Consolas 14pt
        self.setFont(QFont("Consolas", 8, weight=QFont.Bold), 3)   # Style 3: Consolas 14pt

    def language(self):
        return "SimpleLanguage"

    def description(self, style):
        if style == 0:
            return "myStyle_0"
        elif style == 1:
            return "myStyle_1"
        elif style == 2:
            return "myStyle_2"
        elif style == 3:
            return "myStyle_3"
        ###
        return ""

    def styleText(self, start, end):
        # 1. Initialize the styling procedure
        # ------------------------------------
        self.startStyling(start)

        # 2. Slice out a part from the text
        # ----------------------------------
        text = self.parent().text()[start:end]

        # 3. Tokenize the text
        # ---------------------
        p = re.compile(r"\/[#]\s+|\s+|\w+|\W")

        # 'token_list' is a list of tuples: (token_name, token_len)
        token_list = [ (token, len(bytearray(token, "utf-8"))) for token in p.findall(text)]

        # 4. Style the text
        # ------------------
        # 4.1 Check if multiline comment
        multiline_comm_flag = False
        editor = self.parent()
        if start > 0:
            previous_style_nr = editor.SendScintilla(editor.SCI_GETSTYLEAT, start - 1)
            if previous_style_nr == 3:
                multiline_comm_flag = True
        # 4.2 Style the text in a loop
        for i, token in enumerate(token_list):
            if multiline_comm_flag:
                self.setStyling(token[1], 3)

            else:
                if token[0] in ["array", "print", "abs", "goto", "include","main","exit","unset"]:
                    # Red style
                    self.setStyling(token[1], 1)
                elif token[0] in ["(", ")", "{", "}", "[", "]"]:
                    # Blue style
                    self.setStyling(token[1], 2)
                elif token[0] == "#":
                    
                    self.setStyling(token[1], 3)
                else:
                    # Default style
                    self.setStyling(token[1], 0)



class Ui_MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.filename = ""
    #def __init__(self):
       #QMainWindow.__init__(self)
       
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(992, 645)
        self.filename = ""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 410, 91, 16))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 430, 951, 161))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(610, 40, 351, 371))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(850, 390, 111, 16))
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 591, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_ejecutar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ejecutar.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.btn_ejecutar.setObjectName("btn_ejecutar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 26))
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
        self.menuReportes = QtWidgets.QMenu(self.menubar)
        self.menuReportes.setObjectName("menuReportes")


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
        self.actionEjecutar_Descedente = QtWidgets.QAction(MainWindow)
        self.actionEjecutar_Descedente.setObjectName("actionEjecutar_Descedente")



        self.actionReporteAST = QtWidgets.QAction(MainWindow)
        self.actionReporteAST.setObjectName("actionReporteAST")
        self.actionReporteAST_desc = QtWidgets.QAction(MainWindow)
        self.actionReporteAST_desc.setObjectName("actionReporteAST_desc")
        self.actionLexico = QtWidgets.QAction(MainWindow)
        self.actionLexico.setObjectName("actionLexico")
        self.actionSintactico = QtWidgets.QAction(MainWindow)
        self.actionSintactico.setObjectName("actionSintactico")
        self.actionGramatical = QtWidgets.QAction(MainWindow)
        self.actionGramatical.setObjectName("actionGramatical")
        self.actionGramatical_desc = QtWidgets.QAction(MainWindow)
        self.actionGramatical_desc.setObjectName("actionGramatical_desc")


        self.menuReportes.addAction(self.actionReporteAST)
        self.menuReportes.addAction(self.actionReporteAST_desc)
        self.menuReportes.addAction(self.actionLexico)
        self.menuReportes.addAction(self.actionSintactico)
        self.menuReportes.addAction(self.actionGramatical)
        self.menuReportes.addAction(self.actionGramatical_desc)
        
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
        self.menuEjecutar.addAction(self.menuEjecutar_Ascedente.menuAction())
        self.menuEjecutar.addAction(self.actionEjecutar_Descedente)
        self.menuOpciones.addAction(self.actionCambiar_Fondo)
        self.menuOpciones.addAction(self.actionQuitar_Numeros)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuAyuda.addAction(self.actionAcerca_De)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuEjecutar.menuAction())
        self.menubar.addAction(self.menuOpciones.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_ejecutar.clicked.connect(lambda: self.ejecutar())
        self.actionAbrir.triggered.connect(lambda :self.open())
        self.actionGuardar.triggered.connect(lambda :self.save())
        self.actionReporteAST.triggered.connect(lambda :self.action_abrir_imagen())
        self.actionGramatical.triggered.connect(lambda :self.action_abrir_reporte_Gramatical())
        self.actionSintactico.triggered.connect(lambda :self.action_abrir_reporte_Sintactico())
        self.actionLexico.triggered.connect(lambda :self.action_abrir_reporte_lexico())
        self.actionNuevo.triggered.connect(lambda :self.nuevo_archivo())
        self.actionReporteAST_desc.triggered.connect(lambda :self.action_abrir_imgen_ast_desc())
        self.actionGramatical_desc.triggered.connect(lambda :self.action_abrir_reporte_gramatical_desc())
        self.actionEjecutar_Descedente.triggered.connect(lambda :self.ejecutar_desc())
        self.actionAyuda.triggered.connect(lambda :self.action_abrir_manual_usuario())
        self.actionAcerca_De.triggered.connect(lambda :self.showmessagebox())


        self.__myFont = QFont()
        self.__myFont.setPointSize(8)
        self.__editor = QsciScintilla()
        #self.__editor.setText(myCodeSample) 
        # 'myCodeSample' is a string containing some C-code
        self.__editor.setLexer(None)            # We install lexer later
        self.__editor.setUtf8(True)             # Set encoding to UTF-8
        self.__editor.setFont(self.__myFont)    # Gets overridden by lexer later on

        # 1. Text wrapping
        # -----------------
        self.__editor.setWrapMode(QsciScintilla.WrapWord)
        self.__editor.setWrapVisualFlags(QsciScintilla.WrapFlagByText)
        self.__editor.setWrapIndentMode(QsciScintilla.WrapIndentIndented)

        # 2. End-of-line mode
        # --------------------
        self.__editor.setEolMode(QsciScintilla.EolWindows)
        self.__editor.setEolVisibility(False)

        # 3. Indentation
        # ---------------
        self.__editor.setIndentationsUseTabs(False)
        self.__editor.setTabWidth(4)
        self.__editor.setIndentationGuides(True)
        self.__editor.setTabIndents(True)
        self.__editor.setAutoIndent(True)

        # 4. Caret
        # ---------
        self.__editor.setCaretForegroundColor(QColor("#ff0000ff"))
        self.__editor.setCaretLineVisible(True)
        self.__editor.setCaretLineBackgroundColor(QColor("#1f0000ff"))
        self.__editor.setCaretWidth(2)

        # 5. Margins
        # -----------
        # Margin 0 = Line nr margin
        self.__editor.setMarginType(0, QsciScintilla.NumberMargin)
        self.__editor.setMarginWidth(0, "0000")
        self.__editor.setMarginsForegroundColor(QColor("#ff888888"))

        # -------------------------------- #
        #          Install lexer           #
        # -------------------------------- #
        self.__lexer = MyLexer(self.__editor)
        self.__editor.setLexer(self.__lexer)
        self.gridLayout.addWidget(self.__editor)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Augus Intepreter"))
        self.label.setText(_translate("MainWindow", "Consola/Output"))
        self.label_2.setText(_translate("MainWindow", "Tabla de Simbolos"))
        self.btn_ejecutar.setText(_translate("MainWindow", "Ejecutar"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))
        self.menuEjecutar.setTitle(_translate("MainWindow", "Ejecutar"))
        self.menuEjecutar_Ascedente.setTitle(_translate("MainWindow", "Ejecutar Ascedente"))
        self.menuOpciones.setTitle(_translate("MainWindow", "Opciones"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.menuReportes.setTitle(_translate("MainWindow", "Reportes"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
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
        self.actionEjecutar_Descedente.setText(_translate("MainWindow", "Ejecutar Descedente"))

        self.actionReporteAST.setText(_translate("MainWindow", "Reporte AST ASC"))
        self.actionReporteAST_desc.setText(_translate("MainWindows","Reporte AST DESC"))
        self.actionLexico.setText(_translate("MainWindow", "Lexico"))
        self.actionSintactico.setText(_translate("MainWindow", "Sintactico"))
        self.actionGramatical.setText(_translate("MainWindow", "Gramatical"))
        self.actionGramatical_desc.setText(_translate("MainWindow", "Gramatical DESC"))

    def nuevo_archivo(self):
        if(self.filename!=''):
                  # S_File will get the directory path and extension.
            S__File = QtWidgets.QFileDialog.getSaveFileName(None,'GuardarArchivo','/', "Text Files (*.txt)")

            # This will let you access the test in your QTextEdit
            Text = self.__editor.text()

            # This will prevent you from an error if pressed cancel on file dialog.
            if S__File[0]: 
            # Finally this will Save your file to the path selected.
                with open(S__File[0], 'w') as file:
                     file.write(Text)
        else:  
            self.__editor.clear()

    def ejecutar(self):
        
        #f = open("./prueba.txt", "r")
        #input = f.read()
        input = self.__editor.text()
        Raiz = gr.parse(input)
        #print(Raiz.produccion)

        acciones_parser=acciones(Raiz)
        acciones_parser.ejecutar(self.plainTextEdit)
        gr.reporte_de_errores_sintacticos()
        gr.reportegramatica()
        gr.reporte_de_errores_lexicos()
        self.plainTextEdit.appendPlainText(acciones_parser.error)
        #print(acciones_parser.imprimir)
        #self.plainTextEdit.setPlainText(acciones_parser.imprimir)
        #self.plainTextEdit.appendPlainText("PRUEBA APE")
        self.plainTextEdit_2.setHtml (acciones_parser.imprimir_tabla_simbolos())
    
    def ejecutar_desc(self):
        
        #f = open("./prueba.txt", "r")
        #input = f.read()
        input = self.__editor.text()
        Raiz = gr_desc.parse(input)
        #print(Raiz.produccion)

        #acciones_parser=acciones(Raiz)
        #acciones_parser.ejecutar(self.plainTextEdit)
        gr_desc.reporte_de_errores_sintacticos()
        gr_desc.reportegramatica()
        gr_desc.reporte_de_errores_lexicos()
        #self.plainTextEdit.appendPlainText(acciones_parser.error)
        #print(acciones_parser.imprimir)
        #self.plainTextEdit.setPlainText(acciones_parser.imprimir)
        #self.plainTextEdit.appendPlainText("PRUEBA APE")
        #self.plainTextEdit_2.setHtml (acciones_parser.imprimir_tabla_simbolos())
        
    def open(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.*)")

        if self.filename[0]:
            # Read a file
            with open(self.filename[0], "rt") as in_file:
               self.__editor.setText(in_file.read())
    
    def save(self):
        # S_File will get the directory path and extension.
            S__File = QtWidgets.QFileDialog.getSaveFileName(None,'SaveTextFile','/', "Text Files (*.txt)")

            # This will let you access the test in your QTextEdit
            Text = self.__editor.text()

            # This will prevent you from an error if pressed cancel on file dialog.
            if S__File[0]: 
            # Finally this will Save your file to the path selected.
                with open(S__File[0], 'w') as file:
                     file.write(Text)

    def action_abrir_imagen(self):
        wb.open_new(r'AST_asc.dot.png')
    def action_abrir_reporte_lexico(self):
        wb.open_new(r'ReporteErroresLexicos.pdf')

    def action_abrir_reporte_Sintactico(self):
        wb.open_new(r'ReporteErroresSintacticos.pdf')
    def action_abrir_reporte_Gramatical(self):
        wb.open_new(r'ReporteGramatical.pdf')

    def action_abrir_reporte_gramatical_desc(self):
        wb.open_new(r'ReporteGramatical_desc.pdf')
    
    def action_abrir_imgen_ast_desc(self):       
        wb.open_new(r'AST_Desc.dot.png')
    def action_abrir_manual_usuario(self):       
        wb.open_new(r'MANUAL DE USUARIO.pdf')

    def showmessagebox(self):
        wb.open_new(r'acercade.pdf')

            
      
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
