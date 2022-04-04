from PyQt5 import QtWidgets, uic
import sqlite3
import os
import sys
import xz_rc

from views.VistaInserimentoOperatore import VistaInserimentoOperatore
from views.VistaModificaOperatore import VistaModificaOperatore
from views.VistaOperatore import VistaOperatore
from controllers.ControlloreListaOperatori import ControlloreListaOperatori

class VistaListaOperatori(QtWidgets.QMainWindow):
    controller = ControlloreListaOperatori()

    def __init__(self):
        super(VistaListaOperatori, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/operatori.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)
        self.indietr_button.clicked.connect(self.close)
        print(os.getcwd())
        self.update()

    def go_inserisci(self):
        self.vista_inserimentooperatore = VistaInserimentoOperatore()
        self.vista_inserimentooperatore.show()

    def go_modifica(self):
        self.vista_modificaoperatore = VistaModificaOperatore()
        self.vista_modificaoperatore.show()

    def go_visualizza(self):
        self.vista_operatore = VistaOperatore()
        self.vista_operatore.show()

    def update(self):
        for operatore in self.controller.get_operatori():
            numRows = self.tabella_operatori.rowCount()
            self.tabella_operatori.insertRow(numRows)
            self.tabella_operatori.setItem(numRows, 0, QtWidgets.QTableWidgetItem(operatore.get_id()))
            self.tabella_operatori.setItem(numRows, 1, QtWidgets.QTableWidgetItem(operatore.get_nome()))
            self.tabella_operatori.setItem(numRows, 2, QtWidgets.QTableWidgetItem(operatore.get_cognome()))
            self.tabella_operatori.setItem(numRows, 3, QtWidgets.QTableWidgetItem(operatore.get_stato()))

    
