from PyQt5 import QtWidgets, uic, QtCore, Qt
import os
import sys
import xz_rc

from views.VistaInserimentoUtente import VistaInserimentoUtente
from views.VistaModificaUtente import VistaModificaUtente
from views.VistaUtente import VistaUtente
from controllers.ControlloreUtenti import ControlloreUtenti

class VistaListaUtenti(QtWidgets.QMainWindow):
    controller = ControlloreUtenti()

    def __init__(self):
        super(VistaListaUtenti, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/utenti.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)
        self.indietro_button.clicked.connect(self.close)
        self.search_field.textChanged.connect(self.ricerca)
        self.elimina_button.clicked.connect(self.go_elimina)
        self.id_radio.toggled.connect(self.ordina_tabella)
        self.username_radio.toggled.connect(self.ordina_tabella)
        self.tabella_utenti.itemDoubleClicked.connect(self.go_visualizza)
        self.update()

    def go_inserisci(self):
        self.warning_label.setText("")
        self.vista_inserimentoutente = VistaInserimentoUtente(self)
        self.vista_inserimentoutente.show()

    def go_modifica(self):
        utenti = self.get_utenti_selezionati()
        for utente in utenti:
            self.vista_modificautente = VistaModificaUtente(self, utente)
            self.vista_modificautente.show()

    def go_visualizza(self):
        utenti = self.get_utenti_selezionati()
        for utente in utenti:
            self.vista_utente = VistaUtente(self, utente)
            self.vista_utente.show()

    def update(self):
        self.tabella_utenti.setRowCount(0)
        self.inserisci_tabella(self.controller.get_utenti())

    def ricerca(self):
        text = self.search_field.text()
        if text is not None:
            self.tabella_utenti.setRowCount(0)
            self.inserisci_tabella(self.controller.ricerca_utenti(text))
        else:
            self.update()

    def go_elimina(self):
        utenti=self.get_utenti_selezionati()
        if len(utenti) !=0:
            popup=QtWidgets.QDialog()
            uic.loadUi('gui/dialog_elimina.ui', popup)
            if len(utenti) == 1:
                popup.label_3.setText("Vuoi davvero eliminare questo utente?")
            else:
                popup.label_3.setText("Vuoi davvero eliminare " + str(len(utenti)) + " utenti?")
            popup.buttonBox.accepted.connect(self.elimina)
            popup.exec()
            self.update()

    def elimina(self):
        utenti=self.get_utenti_selezionati()
        self.controller.elimina_utenti(utenti)

    def inserisci_tabella(self, utenti):
        row = self.tabella_utenti.rowCount()
        for utente in utenti:
            items = []
            items.append(QtWidgets.QTableWidgetItem(str(utente.get_id())))
            items.append(QtWidgets.QTableWidgetItem(utente.get_username()))
            permessi=utente.get_permessi()
            items.append(QtWidgets.QTableWidgetItem(str(permessi[0])))
            items.append(QtWidgets.QTableWidgetItem(str(permessi[1])))
            items.append(QtWidgets.QTableWidgetItem(str(permessi[2])))
            items.append(QtWidgets.QTableWidgetItem(str(permessi[3])))
            items.append(QtWidgets.QTableWidgetItem(str(permessi[4])))
            items.append(QtWidgets.QTableWidgetItem(str(permessi[5])))
            self.tabella_utenti.insertRow(row)
            column=0
            for item in items:
                item.setFlags(item.flags() &~ QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tabella_utenti.setItem(row, column, item) 
                column+=1
            row+=1
        self.ordina_tabella()

    def ordina_tabella(self):
        if self.id_radio.isChecked():
            self.tabella_utenti.sortItems(0)
        elif self.username_radio.isChecked():
            self.tabella_utenti.sortItems(1)

    def get_utenti_selezionati(self):
        caselle_selezionate=self.tabella_utenti.selectedItems()
        utenti=[]
        if len(caselle_selezionate) == 0:
            self.warning_label.setText("Seleziona almeno un utente.")
        else:
            self.warning_label.setText("")
            righe_selezionate=[]
            for casella in caselle_selezionate:
                righe_selezionate.append(casella.row())
            for riga in set(righe_selezionate):
                utente=self.controller.get_utente(int(self.tabella_utenti.item(riga, 0).text()))
                utenti.append(utente)
        return utenti
