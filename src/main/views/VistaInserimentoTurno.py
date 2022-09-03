from PyQt5 import QtWidgets, uic, QtCore
import sys
import xz_rc

from controllers.ControlloreServizi import ControlloreServizi
from controllers.ControlloreMezzi import ControlloreMezzo
from controllers.ControlloreOperatori import ControlloreOperatori
from controllers.ControlloreTurni import ControlloreTurni


class VistaInserimentoTurno(QtWidgets.QMainWindow):
    def __init__(self,parent):
        super(VistaInserimentoTurno, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_turno.ui', self)  # Load the .ui file
        self.controller = ControlloreTurni()
        self.controller2 = ControlloreServizi()
        self.controller_mezzi = ControlloreMezzo()
        self.controller_operatori = ControlloreOperatori()
        self.annulla_button.clicked.connect(self.close)
        self.inserisci_button.clicked.connect(self.inserisci)
        self.date_field.setMinimumDate(QtCore.QDate.currentDate())
        self.tabella_servizi.setRowCount(0)
        self.tabella_mezzi.setRowCount(0)
        self.tabella_operatori.setRowCount(0)
        self.update()
        
    def inserisci_tabella_servizi(self, servizi):
        row = self.tabella_servizi.rowCount()
        for servizio in servizi:
            items = []
            items.append(QtWidgets.QTableWidgetItem(str(servizio.get_id())))
            items.append(QtWidgets.QTableWidgetItem(servizio.get_tipo()))
            items.append(QtWidgets.QTableWidgetItem(str(servizio.get_id_cliente())))
            items.append(QtWidgets.QTableWidgetItem(servizio.get_periodicita()))
            self.tabella_servizi.insertRow(row)
            column = 0
            for item in items:
                item.setFlags(item.flags() & ~ QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tabella_servizi.setItem(row, column, item)
                column += 1
            row += 1

    def inserisci_tabella_mezzi(self, mezzi):
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

    def inserisci_tabella_operatori(self, operatori):
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

    def inserisci(self):
        servizio = 45
        data_turno = self.date_field.date()
        ora_inizio = self.time_start_field.time()
        ora_fine = self.time_end_field.time()
        mezzo = self.combo_mezzi.currentText()
        operatore = self.combo_operatori.currentText()
        self.controller.insert_turno(servizio, data_turno.toString("yyyy-MM-dd"), ora_inizio.toString(), ora_fine.toString(), str(mezzo), str(operatore))
        self.close()
        self.parent().update()

    def get_mezzo_selezionato(self):
        casella = self.tabella_mezzi.selectedItems()
        id_mezzo = None
        id_mezzo = int(self.tabella_mezzi.item(casella, 0).text())
        return id_mezzo

    def get_operatore_selezionato(self):
        casella = self.tabella_operatori.selectedItems()
        id_operatore = None
        operatore = self.controller_operatori.get_operatore(int(self.tabella_mezzi.item(casella, 0).text()))
        id_operatore = operatore.get_cognome
        return id_operatore
    
    def update(self):
        #riembimento combo box mezzi
        mezzi = self.controller_mezzi.get_mezzi()
        id_mezzi = []
        for mezzo in mezzi:
            id = mezzo.get_id_mezzo()
            id_mezzi.append(str(id))
        self.combo_mezzi.addItems(id_mezzi)
        #riempimento combo box operatori
        operatori = self.controller_operatori.get_operatori()
        id_operatori = []
        for operatore in operatori:
            id = operatore.get_id()
            id_operatori.append(str(id))
        self.combo_operatori.addItems(id_operatori)
        self.inserisci_tabella_servizi(self.controller2.get_servizi())
        #aggiungere il get_tipo servizio per la ricerca dei mezzi
        self.inserisci_tabella_mezzi(self.controller_mezzi.get_mezzi())
        self.inserisci_tabella_operatori(self.controller_operatori.get_operatori())
