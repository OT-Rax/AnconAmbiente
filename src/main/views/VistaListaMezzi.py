from PyQt5 import QtWidgets, uic, QtCore, Qt
import os
import sys
import xz_rc

from views.VistaInserimentoMezzo import VistaInserimentoMezzo
from views.VistaModificaMezzo import VistaModificaMezzo
from views.VistaMezzo import VistaMezzo
from controllers.ControlloreMezzi import ControlloreMezzo

class VistaListaMezzi(QtWidgets.QMainWindow):
    controller = ControlloreMezzo()

    def __init__(self):
        super(VistaListaMezzi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/mezzi.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)
        self.indietr_button.clicked.connect(self.close)
        self.search_field.textChanged.connect(self.ricerca)
        self.elimina_button.clicked.connect(self.go_elimina)
        self.id_radio.toggled.connect(self.ordina_tabella)
        self.modello_radio.toggled.connect(self.ordina_tabella)
        self.allestimento_radio.toggled.connect(self.ordina_tabella)
        self.stato_radio.toggled.connect(self.ordina_tabella)
        self.tabella_mezzi.itemDoubleClicked.connect(self.go_visualizza)
        self.update()


    def go_inserisci(self):
        self.vista_inserimentomezzo = VistaInserimentoMezzo(self)
        self.vista_inserimentomezzo.show()

    def go_modifica(self):
        mezzi = self.get_mezzi_selezionati()
        for mezzo in mezzi:
            self.vista_modificamezzo = VistaModificaMezzo(self, mezzo)
            self.vista_modificamezzo.show()

    def go_visualizza(self):
        caselle_selezionate=self.tabella_mezzi.selectedItems()
        righe_selezionate=[]
        for casella in caselle_selezionate:
            righe_selezionate.append(casella.row())
        for riga in set(righe_selezionate):
            mezzo=self.controller.get_mezzo(int(self.tabella_mezzi.item(riga, 0).text()))
            self.vista_mezzo = VistaMezzo(self.parent,mezzo)
            self.vista_mezzo.show()

    def update(self):
        self.tabella_mezzi.setRowCount(0)
        self.inserisci_tabella(self.controller.get_mezzi())

    def ricerca(self):
        text = self.search_field.text()
        if text is not None:
            self.tabella_mezzi.setRowCount(0)
            self.inserisci_tabella(self.controller.ricerca_mezzi(text))
        else:
            self.update()

    def go_elimina(self):
        mezzi=self.get_mezzi_selezionati()
        if len(mezzi) !=0:
            popup=QtWidgets.QDialog()
            uic.loadUi('gui/dialog_elimina.ui', popup)
            if len(mezzi) == 1:
                popup.label_3.setText("Vuoi davvero eliminare questo mezzo?")
            else:
                popup.label_3.setText("Vuoi davvero eliminare " + str(len(mezzi)) + " mezzi?")
            popup.buttonBox.accepted.connect(self.elimina)
            popup.exec()
            self.update()

    def elimina(self):
        mezzi=self.get_mezzi_selezionati()
        self.controller.elimina_mezzi(mezzi)

    def inserisci_tabella(self, mezzi):
        row = self.tabella_mezzi.rowCount()
        for mezzo in mezzi:
            if mezzo.get_stato_mezzo() == 0:
                stato="Disponibile"
            else:
                stato="Non disponibile"
            items = []
            items.append(QtWidgets.QTableWidgetItem(str(mezzo.get_id_mezzo())))
            items.append(QtWidgets.QTableWidgetItem(mezzo.get_tipo_mezzo()))
            items.append(QtWidgets.QTableWidgetItem(mezzo.get_allestimento_mezzo()))
            items.append(QtWidgets.QTableWidgetItem(stato))
            self.tabella_mezzi.insertRow(row)
            column=0
            for item in items:
                item.setFlags(item.flags() &~ QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tabella_mezzi.setItem(row, column, item) 
                column+=1
            row+=1

    def get_mezzi_selezionati(self):
        caselle_selezionate=self.tabella_mezzi.selectedItems()
        mezzi=[]
        if len(caselle_selezionate) == 0:
            self.warning_label.setText("Seleziona almeno un mezzo.")
        else:
            self.warning_label.setText("")
            righe_selezionate=[]
            for casella in caselle_selezionate:
                righe_selezionate.append(casella.row())
            for riga in set(righe_selezionate):
                mezzo=self.controller.get_mezzo(int(self.tabella_mezzi.item(riga, 0).text()))
                mezzi.append(mezzo)
        return mezzi

    def ordina_tabella(self):
        if self.id_radio.isChecked():
            self.tabella_mezzi.sortItems(0)
        elif self.modello_radio.isChecked():
            self.tabella_mezzi.sortItems(1)
        elif self.allestimento_radio.isChecked():
            self.tabella_mezzi.sortItems(2)
        elif self.stato_radio.isChecked():
            self.tabella_mezzi.sortItems(3)