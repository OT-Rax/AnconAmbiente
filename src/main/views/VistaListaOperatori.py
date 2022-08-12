from PyQt5 import QtWidgets, uic
import os
import sys
import xz_rc

from views.VistaInserimentoOperatore import VistaInserimentoOperatore
from views.VistaModificaOperatore import VistaModificaOperatore
from views.VistaOperatore import VistaOperatore
from controllers.ControlloreOperatori import ControlloreOperatori

class VistaListaOperatori(QtWidgets.QMainWindow):
    controller = ControlloreOperatori()

    def __init__(self):
        super(VistaListaOperatori, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/operatori.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)
        self.indietro_button.clicked.connect(self.close)
        self.search_field.textChanged.connect(self.ricerca)
        print(os.getcwd())
        self.update()

    def go_inserisci(self):
        self.vista_inserimentooperatore = VistaInserimentoOperatore()
        self.vista_inserimentooperatore.show()

    def go_modifica(self):
        self.vista_modificaoperatore = VistaModificaOperatore()
        self.vista_modificaoperatore.show()

    def go_visualizza(self):
        caselle_selezionate=self.tabella_operatori.selectedItems()
        righe_selezionate=[]
        for casella in caselle_selezionate:
            righe_selezionate.append(casella.row())
        for riga in set(righe_selezionate):
            operatore=self.controller.get_operatore(int(self.tabella_operatori.item(riga, 0).text()))
            self.vista_operatore = VistaOperatore(operatore)
            self.vista_operatore.show()

    def update(self):
        self.tabella_operatori.setRowCount(0)
        self.inserisci_tabella(self.controller.get_operatori())

    def ricerca(self):
        text = self.search_field.text()
        if text is not None:
            self.tabella_operatori.setRowCount(0)
            self.inserisci_tabella(self.controller.ricerca_operatori(text))

    def inserisci_tabella(self, operatori):
        rows = self.tabella_operatori.rowCount()
        for operatore in operatori:
            print(operatore.get_id())
            self.tabella_operatori.insertRow(rows)
            self.tabella_operatori.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(operatore.get_id())))
            self.tabella_operatori.setItem(rows, 1, QtWidgets.QTableWidgetItem(operatore.get_nome()))
            self.tabella_operatori.setItem(rows, 2, QtWidgets.QTableWidgetItem(operatore.get_cognome()))
            self.tabella_operatori.setItem(rows, 3, QtWidgets.QTableWidgetItem(str(operatore.get_stato())))
            rows+=1


