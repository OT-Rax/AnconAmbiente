from PyQt5 import QtWidgets, uic, QtCore
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
        self.elimina_button.clicked.connect(self.go_elimina)
        print(os.getcwd())
        self.update()

    def go_inserisci(self):
        self.vista_inserimentooperatore = VistaInserimentoOperatore(self)
        self.vista_inserimentooperatore.show()

    def go_modifica(self):
        caselle_selezionate=self.tabella_operatori.selectedItems()
        righe_selezionate=[]
        for casella in caselle_selezionate:
            righe_selezionate.append(casella.row())
        for riga in set(righe_selezionate):
            operatore=self.controller.get_operatore(int(self.tabella_operatori.item(riga, 0).text()))
            self.vista_modificaoperatore = VistaModificaOperatore(self, operatore)
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

    def go_elimina(self):
        caselle_selezionate=self.tabella_operatori.selectedItems()
        righe_selezionate=[]
        operatori=[]
        for casella in caselle_selezionate:
            righe_selezionate.append(casella.row())
        for riga in set(righe_selezionate):
            operatore=self.controller.get_operatore(int(self.tabella_operatori.item(riga, 0).text()))
            operatori.append(operatore)
        popup=QtWidgets.QDialog()
        uic.loadUi('gui/dialog_elimina.ui', popup)
        popup.label_3.setText("Vuoi davvero eliminare " + str(len(operatori)) + " operatori?")
        popup.buttonBox.accepted.connect(self.elimina)
        popup.exec()
        self.update()

    def elimina(self):
        caselle_selezionate=self.tabella_operatori.selectedItems()
        righe_selezionate=[]
        operatori=[]
        for casella in caselle_selezionate:
            righe_selezionate.append(casella.row())
        for riga in set(righe_selezionate):
            operatore=self.controller.get_operatore(int(self.tabella_operatori.item(riga, 0).text()))
            operatori.append(operatore)
        self.controller.elimina_operatori(operatori)

    def inserisci_tabella(self, operatori):
        row = self.tabella_operatori.rowCount()
        for operatore in operatori:
            items = []
            items.append(QtWidgets.QTableWidgetItem(str(operatore.get_id())))
            items.append(QtWidgets.QTableWidgetItem(operatore.get_nome()))
            items.append(QtWidgets.QTableWidgetItem(operatore.get_cognome()))
            items.append(QtWidgets.QTableWidgetItem(str(operatore.get_stato())))
            self.tabella_operatori.insertRow(row)
            column=0
            for item in items:
                item.setFlags(item.flags() &~ QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tabella_operatori.setItem(row, column, item) 
                column+=1
            row+=1
