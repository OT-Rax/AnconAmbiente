from PyQt5 import QtWidgets, uic, QtCore
import sys
import xz_rc

from views.VistaInserimentoServizio import VistaInserimentoServizio
from views.VistaModificaServizio import VistaModificaServizio
from views.VistaServizio import VistaServizio
from controllers.ControlloreServizi import ControlloreServizi
from controllers.ControlloreClienti import ControlloreClienti


class VistaListaServizi(QtWidgets.QMainWindow):
    def __init__(self):
        # Costruttore 'VistaListaServizi'
        super(VistaListaServizi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/servizi.ui', self)  # Load the .ui file
        self.controller = ControlloreServizi()
        self.controller_clienti = ControlloreClienti()
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)
        self.indietro_button.clicked.connect(self.close)
        self.search_field.textChanged.connect(self.ricerca)
        self.elimina_button.clicked.connect(self.go_elimina)
        self.tabella_servizi.itemDoubleClicked.connect(self.go_visualizza)
        self.tabella_servizi.horizontalHeader().resizeSection(0, 50)
        self.tabella_servizi.horizontalHeader().resizeSection(2, 70)
        self.tabella_servizi.horizontalHeader().resizeSection(4, 220)
        self.update()

    def go_inserisci(self):
        # Metodo per richiamare la vista 'VistaInserimentoServizio'
        self.vista_inserimentoservizio = VistaInserimentoServizio(self)
        self.vista_inserimentoservizio.show()

    def go_modifica(self):
        # Metodo per richiamare la vista 'VistaModificaServizio'
        servizi = self.get_servizi_selezionati()
        for servizio in servizi:
                self.vista_modificaservizio = VistaModificaServizio(self, servizio)
                self.vista_modificaservizio.show()      
        

    def go_visualizza(self):
        # Metodo per richiamare la vista 'VistaServizio'
        caselle_selezionate = self.tabella_servizi.selectedItems()
        righe_selezionate = []
        for casella in caselle_selezionate:
            righe_selezionate.append(casella.row())
        for riga in set(righe_selezionate):
            servizio = self.controller.get_servizio(int(self.tabella_servizi.item(riga, 0).text()))
            self.vista_servizio = VistaServizio(self, servizio)
            self.vista_servizio.show()

    def update(self):
        # Metodo per aggiornare la tabella che visualizza i servizi
        self.tabella_servizi.setRowCount(0)
        self.inserisci_tabella(self.controller.get_servizi())

    def go_elimina(self):
        # Metodo per eliminare un servizio dalla tabella e dal database
        servizi=self.get_servizi_selezionati()
        if len(servizi) !=0:
            popup=QtWidgets.QDialog()
            uic.loadUi('gui/dialog_elimina.ui', popup)
            if len(servizi) == 1:
                popup.label_3.setText("Vuoi davvero eliminare questo servizio?")
            else:
                popup.label_3.setText("Vuoi davvero eliminare " + str(len(servizi)) + " servizi?")
            popup.buttonBox.accepted.connect(self.elimina)
            popup.exec()
            self.update()

    def elimina(self):
        # Metodo per eliminare un servizio dal database
        servizi=self.get_servizi_selezionati()
        self.controller.elimina_servizi(servizi)

    def ricerca(self):
        # Metodo per cercare nella tabella
        text = self.search_field.text()
        if text is not None:
            self.tabella_servizi.setRowCount(0)
            self.inserisci_tabella(self.controller.ricerca_servizi(text))
        else:
            self.update()

    def inserisci_tabella(self, servizi):
        # Metodo che popola la tabella per visualizzare i servizi salvati nel database
        # :param servizi: Oggetto contente i dati per popolare le colonne della tabella
        row = self.tabella_servizi.rowCount()
        for servizio in servizi:
            items = []
            items.append(QtWidgets.QTableWidgetItem(str(servizio.get_id())))
            items.append(QtWidgets.QTableWidgetItem(servizio.get_tipo()))
            items.append(QtWidgets.QTableWidgetItem(str(servizio.get_id_cliente())))
            items.append(QtWidgets.QTableWidgetItem(self.controller_clienti.get_cliente(servizio.get_id_cliente()).get_nome()+" "+self.controller_clienti.get_cliente(servizio.get_id_cliente()).get_cognome()))
            items.append(QtWidgets.QTableWidgetItem(servizio.get_luogo()))
            ripetizione=servizio.get_ripetizione()
            if servizio.get_periodicita() is None:
                periodicita="Non periodico"
            elif servizio.get_periodicita() == "Giornaliero":
                periodicita=str(ripetizione)+" volte al giorno"
            elif servizio.get_periodicita() == "Settimanale":
                periodicita=str(ripetizione)+" volte a settimana"
            elif servizio.get_periodicita() == "Mensile":
                periodicita=str(ripetizione)+" volte al mese"
            elif servizio.get_periodicita() == "Annuale":
                periodicita=str(ripetizione)+" volte all'anno"
            items.append(QtWidgets.QTableWidgetItem(periodicita))
            self.tabella_servizi.insertRow(row)
            column = 0
            for item in items:
                item.setFlags(item.flags() & ~ QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tabella_servizi.setItem(row, column, item)
                column += 1
            row += 1


    def get_servizi_selezionati(self):
        # Metodo per restiture i servizi attualmente selezionati nela tabella
        caselle_selezionate=self.tabella_servizi.selectedItems()
        servizi=[]
        if len(caselle_selezionate) == 0:
            self.warning_label.setText("Seleziona almeno un servizio.")
        else:
            self.warning_label.setText("")
            righe_selezionate=[]
            for casella in caselle_selezionate:
                righe_selezionate.append(casella.row())
            for riga in set(righe_selezionate):
                servizio=self.controller.get_servizio(int(self.tabella_servizi.item(riga, 0).text()))
                servizi.append(servizio)
        return servizi
