from PyQt5 import QtWidgets, uic, QtCore, Qt
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
        # Costruttore 'VistaListaOperatori'
        super(VistaListaOperatori, self).__init__()  # Call the inherited classes __init__ method
        dirname = os.path.dirname(__file__)
        gui_file = os.path.join(dirname, '../gui/operatori.ui')
        uic.loadUi(gui_file, self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)
        self.indietro_button.clicked.connect(self.close)
        self.search_field.textChanged.connect(self.ricerca)
        self.elimina_button.clicked.connect(self.go_elimina)
        self.id_radio.toggled.connect(self.ordina_tabella)
        self.nome_radio.toggled.connect(self.ordina_tabella)
        self.cognome_radio.toggled.connect(self.ordina_tabella)
        self.stato_radio.toggled.connect(self.ordina_tabella)
        self.tabella_operatori.itemDoubleClicked.connect(self.go_visualizza)
        #print(os.getcwd())
        self.update()

    def go_inserisci(self):
        # Metodo per richiamare la vista 'VistaInserimentoOperatore'
        self.warning_label.setText("")
        self.vista_inserimentooperatore = VistaInserimentoOperatore(self)
        self.vista_inserimentooperatore.show()

    def go_modifica(self):
        # Metodo per richiamare la vista 'VistaModificaOperatore'
        operatori = self.get_operatori_selezionati()
        for operatore in operatori:
            self.vista_modificaoperatore = VistaModificaOperatore(self, operatore)
            self.vista_modificaoperatore.show()

    def go_visualizza(self):
        # Metodo per richiamare la vista 'VistaOperatore'
        operatori = self.get_operatori_selezionati()
        for operatore in operatori:
            self.vista_operatore = VistaOperatore(self, operatore)
            self.vista_operatore.show()

    def update(self):
        # Metodo per aggiornare la tabella che visualizza gli operatori
        self.tabella_operatori.setRowCount(0)
        self.inserisci_tabella(self.controller.get_operatori())

    def ricerca(self):
        # Metodo per cercare nella tabella
        text = self.search_field.text()
        if text is not None:
            self.tabella_operatori.setRowCount(0)
            self.inserisci_tabella(self.controller.ricerca_operatori(text))
        else:
            self.update()

    def go_elimina(self):
        # Metodo per eliminare un operatore dalla tabella e dal database
        operatori=self.get_operatori_selezionati()
        if len(operatori) !=0:
            popup=QtWidgets.QDialog()
            uic.loadUi('gui/dialog_elimina.ui', popup)
            if len(operatori) == 1:
                popup.label_3.setText("Vuoi davvero eliminare questo operatore?")
            else:
                popup.label_3.setText("Vuoi davvero eliminare " + str(len(operatori)) + " operatori?")
            popup.buttonBox.accepted.connect(self.elimina)
            popup.exec()
            self.update()

    def elimina(self):
        # Metodo per eliminare un operatore dal database
        operatori=self.get_operatori_selezionati()
        self.controller.elimina_operatori(operatori)

    def inserisci_tabella(self, operatori):
        # Metodo che popola la tabella per visualizzare gli operatori salvati nel database
        # :param operatori: Oggetto contente i dati per popolare le colonne della tabella
        row = self.tabella_operatori.rowCount()
        for operatore in operatori:
            if operatore.get_stato() == 0:
                stato="Disponibile"
            elif operatore.get_stato() == 1:
                stato="In malattia"
            else:   
                stato="In ferie"
            items = []
            items.append(QtWidgets.QTableWidgetItem(str(operatore.get_id())))
            items.append(QtWidgets.QTableWidgetItem(operatore.get_nome()))
            items.append(QtWidgets.QTableWidgetItem(operatore.get_cognome()))
            items.append(QtWidgets.QTableWidgetItem(stato))
            self.tabella_operatori.insertRow(row)
            column=0
            for item in items:
                item.setFlags(item.flags() &~ QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tabella_operatori.setItem(row, column, item) 
                column+=1
            row+=1
        self.ordina_tabella()

    def ordina_tabella(self):
        # Metodo per ordinare la tabella in base alla selezione dell'utente
        if self.id_radio.isChecked():
            self.tabella_operatori.sortItems(0)
        elif self.nome_radio.isChecked():
            self.tabella_operatori.sortItems(1)
        elif self.cognome_radio.isChecked():
            self.tabella_operatori.sortItems(2)
        elif self.stato_radio.isChecked():
            self.tabella_operatori.sortItems(3)

    def get_operatori_selezionati(self):
        # Metodo per restiture gli operatori attualmente selezionati nela tabella
        caselle_selezionate=self.tabella_operatori.selectedItems()
        operatori=[]
        if len(caselle_selezionate) == 0:
            self.warning_label.setText("Seleziona almeno un operatore.")
        else:
            self.warning_label.setText("")
            righe_selezionate=[]
            for casella in caselle_selezionate:
                righe_selezionate.append(casella.row())
            for riga in set(righe_selezionate):
                operatore=self.controller.get_operatore(int(self.tabella_operatori.item(riga, 0).text()))
                operatori.append(operatore)
        return operatori
