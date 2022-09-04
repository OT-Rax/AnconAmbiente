from PyQt5 import QtWidgets, uic, QtCore
import sys
import xz_rc

from controllers.ControlloreTurni import ControlloreTurni
from controllers.ControlloreServizi import ControlloreServizi
from controllers.ControlloreMezzi import ControlloreMezzo
from controllers.ControlloreOperatori import ControlloreOperatori

from views.VistaListaServizi import VistaListaServizi

class VistaModificaTurno(QtWidgets.QMainWindow):
    def __init__(self,parent,turno):
        super(VistaModificaTurno, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/modifica_turno.ui', self)  # Load the .ui file
        self.turno = turno
        self.controller = ControlloreTurni()
        self.controller_servizi = ControlloreServizi()
        self.controller_mezzi = ControlloreMezzo()
        self.controller_operatori = ControlloreOperatori()
        self.annulla_button.clicked.connect(self.close)
        self.salva_button.clicked.connect(self.salva)
        self.servizi_button.clicked.connect(self.go_listaservizi)
        self.inizio_datetimepicker.setDateTime(QtCore.QDateTime.fromString(turno.get_data_inizio(), "yyyy-MM-dd hh:mm"))
        self.fine_datetimepicker.setDateTime(QtCore.QDateTime.fromString(turno.get_data_fine(), "yyyy-MM-dd hh:mm"))
        self.inizio_datetimepicker.editingFinished.connect(self.inizio_edited)
        self.fine_datetimepicker.setMinimumDateTime(QtCore.QDateTime.currentDateTime())
        self.tabella_servizi.setRowCount(0)
        self.tabella_mezzi.setRowCount(0)
        self.tabella_operatori.setRowCount(0)
        self.update()
        self.combo_servizi.setCurrentText(str(turno.get_servizio().get_id()))
        for row in range(self.tabella_mezzi.rowCount()):
            for mezzo in turno.get_mezzi():
                if self.tabella_mezzi.item(row, 0).text() == str(mezzo.get_id_mezzo()):
                    for i in range(4):
                        self.tabella_mezzi.item(row,i).setSelected(True)
        for row in range(self.tabella_operatori.rowCount()):
            for operatore in turno.get_operatori():
                if self.tabella_operatori.item(row, 0).text() == str(operatore.get_id()):
                    for i in range(4):
                        self.tabella_operatori.item(row,i).setSelected(True)
        
        
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

    def salva(self):
        operatori_validity = self.check_operatori()
        servizio_validity = self.check_servizio()
        if  operatori_validity and servizio_validity:
            self.turno.set_servizio(self.controller_servizi.get_servizio(int(self.combo_servizi.currentText())))
            self.turno.set_data_inizio(self.inizio_datetimepicker.dateTime().toString("yyyy-MM-dd hh:mm"))
            self.turno.set_data_fine(self.fine_datetimepicker.dateTime().toString("yyyy-MM-dd hh:mm"))
            id_operatori = self.get_id_operatori_selezionati()
            operatori=[]
            for id in id_operatori:
                operatori.append(self.controller_operatori.get_operatore(id))
            self.turno.set_operatori(operatori)
            id_mezzi = self.get_id_mezzi_selezionati()
            mezzi=[]
            for id in id_mezzi:
                mezzi.append(self.controller_mezzi.get_mezzo(id))
            self.turno.set_mezzi(mezzi)
            self.controller.modifica_turno(self.turno)
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
        mezzi = self.controller_mezzi.get_mezzi_disponibili_modifica(inizio_turno, fine_turno, self.turno.get_id())
        operatori = self.controller_operatori.get_operatori_disponibili_modifica(inizio_turno, fine_turno, self.turno.get_id())
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
