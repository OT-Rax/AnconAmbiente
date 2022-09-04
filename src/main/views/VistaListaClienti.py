from PyQt5 import QtWidgets, uic, QtCore, Qt
import os
import sys
import xz_rc

from views.VistaInserimentoCliente import VistaInserimentoCliente
from views.VistaModificaCliente import VistaModificaCliente
from views.VistaCliente import VistaCliente
from controllers.ControlloreClienti import ControlloreClienti

class VistaListaClienti(QtWidgets.QMainWindow):
    controller = ControlloreClienti()

    def __init__(self):
        # Costruttore 'VistaListaClienti'
        super(VistaListaClienti, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/clienti.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)
        self.indietro_button.clicked.connect(self.close)
        self.search_field.textChanged.connect(self.ricerca)
        self.elimina_button.clicked.connect(self.go_elimina)
        self.id_radio.toggled.connect(self.ordina_tabella)
        self.nome_radio.toggled.connect(self.ordina_tabella)
        self.cognome_radio.toggled.connect(self.ordina_tabella)
        self.partitaiva_radio.toggled.connect(self.ordina_tabella)
        self.tabella_clienti.itemDoubleClicked.connect(self.go_visualizza)
        #print(os.getcwd())
        self.update()

    def go_inserisci(self):
        # Metodo per richiamare la vista 'VistaInserimentoCliente'
        self.warning_label.setText("")
        self.vista_inserimentocliente = VistaInserimentoCliente(self)
        self.vista_inserimentocliente.show()

    def go_modifica(self):
        # Metodo per richiamare la vista 'VistaModificaCliente'
        clienti = self.get_clienti_selezionati()
        for cliente in clienti:
            self.vista_modificacliente = VistaModificaCliente(self, cliente)
            self.vista_modificacliente.show()

    def go_visualizza(self):
        # Metodo per richiamare la vista 'VistaCliente'
        clienti = self.get_clienti_selezionati()
        for cliente in clienti:
            self.vista_cliente = VistaCliente(self, cliente)
            self.vista_cliente.show()

    def update(self):
        # Metodo per aggiornare la tabella che visualizza i clienti
        self.tabella_clienti.setRowCount(0)
        self.inserisci_tabella(self.controller.get_clienti())

    def ricerca(self):
        # Metodo per cercare nella tabella
        text = self.search_field.text()
        if text is not None:
            self.tabella_clienti.setRowCount(0)
            self.inserisci_tabella(self.controller.ricerca_clienti(text))
        else:
            self.update()

    def go_elimina(self):
        # Metodo per eliminare un cliente dalla tabella e dal database
        clienti=self.get_clienti_selezionati()
        if len(clienti) !=0:
            popup=QtWidgets.QDialog()
            uic.loadUi('gui/dialog_elimina.ui', popup)
            if len(clienti) == 1:
                popup.label_3.setText("Vuoi davvero eliminare questo cliente?")
            else:
                popup.label_3.setText("Vuoi davvero eliminare " + str(len(clienti)) + " clienti?")
            popup.buttonBox.accepted.connect(self.elimina)
            popup.exec()
            self.update()

    def elimina(self):
        # Metodo che elimina cliente dal database
        clienti=self.get_clienti_selezionati()
        self.controller.elimina_clienti(clienti)

    def inserisci_tabella(self, clienti):
        # Metodo che popola la tabella per visualizzare i clienti salvati nel database
        # :param clienti: Oggetto contente i dati per popolare le colonne della tabella
        row = self.tabella_clienti.rowCount()
        for cliente in clienti:
            items = []
            items.append(QtWidgets.QTableWidgetItem(str(cliente.get_id())))
            items.append(QtWidgets.QTableWidgetItem(cliente.get_nome()))
            items.append(QtWidgets.QTableWidgetItem(cliente.get_cognome()))
            items.append(QtWidgets.QTableWidgetItem(cliente.get_partitaiva()))
            self.tabella_clienti.insertRow(row)
            column=0
            for item in items:
                item.setFlags(item.flags() &~ QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tabella_clienti.setItem(row, column, item) 
                column+=1
            row+=1
        self.ordina_tabella()

    def ordina_tabella(self):
        # Metodo per ordinare la tabella in base alla selezione dell'utente
        if self.id_radio.isChecked():
            self.tabella_clienti.sortItems(0)
        elif self.nome_radio.isChecked():
            self.tabella_clienti.sortItems(1)
        elif self.cognome_radio.isChecked():
            self.tabella_clienti.sortItems(2)
        elif self.partitaiva_radio.isChecked():
            self.tabella_clienti.sortItems(3)

    def get_clienti_selezionati(self):
        # Metodo per restiture i clienti attualmente selezionati nela tabella
        caselle_selezionate=self.tabella_clienti.selectedItems()
        clienti=[]
        if len(caselle_selezionate) == 0:
            self.warning_label.setText("Seleziona almeno un cliente.")
        else:
            self.warning_label.setText("")
            righe_selezionate=[]
            for casella in caselle_selezionate:
                righe_selezionate.append(casella.row())
            for riga in set(righe_selezionate):
                cliente=self.controller.get_cliente(int(self.tabella_clienti.item(riga, 0).text()))
                clienti.append(cliente)
        return clienti
