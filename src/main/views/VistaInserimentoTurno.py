import os

from PyQt5 import QtWidgets, uic, QtCore
import sys
import xz_rc

from controllers.ControlloreServizi import ControlloreServizi
from controllers.ControlloreMezzi import ControlloreMezzi
from controllers.ControlloreOperatori import ControlloreOperatori
from controllers.ControlloreTurni import ControlloreTurni

from views.VistaListaServizi import VistaListaServizi


class VistaInserimentoTurno(QtWidgets.QMainWindow):
    def __init__(self,parent):
        super(VistaInserimentoTurno, self).__init__(parent)  # Call the inherited classes __init__ method
        dirname = os.path.dirname(__file__)
        gui_file = os.path.join(dirname, '../gui/inserimento_turno.ui')
        uic.loadUi(gui_file, self)  # Load the .ui file
        self.controller = ControlloreTurni()
        self.controller_servizi = ControlloreServizi()
        self.controller_mezzi = ControlloreMezzi()
        self.controller_operatori = ControlloreOperatori()
        self.annulla_button.clicked.connect(self.close)
        self.inserisci_button.clicked.connect(self.inserisci)
        self.servizi_button.clicked.connect(self.go_listaservizi)
        self.inizio_datetimepicker.setMinimumDateTime(QtCore.QDateTime.currentDateTime())
        self.inizio_datetimepicker.editingFinished.connect(self.inizio_edited)
        self.fine_datetimepicker.setMinimumDateTime(QtCore.QDateTime.currentDateTime())
        self.tabella_servizi.setRowCount(0)
        self.tabella_mezzi.setRowCount(0)
        self.tabella_operatori.setRowCount(0)
        self.update()
        
    def go_listaservizi(self):
        self.vista_listaservizi=VistaListaServizi()
        self.vista_listaservizi.show()
        
    def inizio_edited(self):
        self.fine_datetimepicker.setMinimumDateTime(self.inizio_datetimepicker.dateTime())
        self.update()

    def inserisci_tabella_servizi(self, servizi):
        row = self.tabella_servizi.rowCount()
        for servizio in servizi:
            items = []
            items.append(QtWidgets.QTableWidgetItem(str(servizio.get_id())))
            items.append(QtWidgets.QTableWidgetItem(servizio.get_tipo()))
            items.append(QtWidgets.QTableWidgetItem(str(servizio.get_luogo())))
            items.append(QtWidgets.QTableWidgetItem("Non periodico" if servizio.get_periodicita() is None else servizio.get_periodicita()))
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
        operatori_validity = self.check_operatori()
        servizio_validity = self.check_servizio()
        if  operatori_validity and servizio_validity:
            id_servizio = self.combo_servizi.currentText()
            data_inizio = self.inizio_datetimepicker.dateTime().toString("yyyy-MM-dd hh:mm")
            data_fine = self.fine_datetimepicker.dateTime().toString("yyyy-MM-dd hh:mm")
            id_operatori = self.get_id_operatori_selezionati()
            id_mezzi = self.get_id_mezzi_selezionati()
            self.controller.insert_turno(id_servizio, data_inizio, data_fine, id_mezzi, id_operatori)
            self.close()
            self.parent().update()
    
    def update(self):
        self.tabella_operatori.setRowCount(0)
        self.tabella_mezzi.setRowCount(0)
        self.tabella_servizi.setRowCount(0)
        self.combo_servizi.clear()
        inizio_turno = self.inizio_datetimepicker.dateTime().toString("yyyy-MM-dd hh:mm")
        fine_turno = self.fine_datetimepicker.dateTime().toString("yyyy-MM-dd hh:mm")
        #riempimento combo box servizi
        servizi_da_inserire = self.controller_servizi.get_servizi_da_inserire(self.inizio_datetimepicker.dateTime())
        servizi = self.controller_servizi.get_servizi_inseribili(self.inizio_datetimepicker.dateTime())
        id_servizi = []
        for servizio in servizi:
            id = servizio.get_id()
            id_servizi.append(str(id))
        self.combo_servizi.addItems(id_servizi)
        mezzi = self.controller_mezzi.get_mezzi_disponibili(inizio_turno, fine_turno)
        operatori = self.controller_operatori.get_operatori_disponibili(inizio_turno, fine_turno)
        self.inserisci_tabella_servizi(servizi_da_inserire)
        #aggiungere il get_tipo servizio per la ricerca dei mezzi
        self.inserisci_tabella_mezzi(mezzi)
        self.inserisci_tabella_operatori(operatori)

    def check_operatori(self):
        if len(self.get_id_operatori_selezionati()) == 0:
            self.operatori_error.setText("Seleziona almeno un operatore")
            self.inserimento_error.setText("Controlla di aver inserito tutti i campi")
            return False
        else:
            self.operatori_error.setText("")
            return True


    def check_servizio(self):
        if self.combo_servizi.currentText() == "":
            self.servizio_error.setText("Seleziona almeno un servizio.")
            self.inserimento_error.setText("Controlla di aver inserito tutti i campi")
            return False
        else:
            self.servizio_error.setText("")
            return True
    

    def get_id_operatori_selezionati(self):
        # Metodo per restiture gli operatori attualmente selezionati nela tabella
        caselle_selezionate=self.tabella_operatori.selectedItems()
        id_operatori=[]
        if len(caselle_selezionate) != 0:
            righe_selezionate=[]
            for casella in caselle_selezionate:
                righe_selezionate.append(casella.row())
            for riga in set(righe_selezionate):
                id_operatori.append(int(self.tabella_operatori.item(riga, 0).text()))
        return id_operatori
     
    def get_id_mezzi_selezionati(self):
        # Metodo per restiture i mezzi attualmente selezionati nela tabella
        caselle_selezionate=self.tabella_mezzi.selectedItems()
        id_mezzi=[]
        if len(caselle_selezionate) != 0:
            righe_selezionate=[]
            for casella in caselle_selezionate:
                righe_selezionate.append(casella.row())
            for riga in set(righe_selezionate):
                id_mezzi.append(int(self.tabella_mezzi.item(riga, 0).text()))
        return id_mezzi
