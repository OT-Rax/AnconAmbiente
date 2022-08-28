from PyQt5 import QtWidgets, uic, QtCore
import sys
import xz_rc

from controllers.ControlloreTurni import ControlloreTurni
from controllers.ControlloreMezzi import ControlloreMezzo
from controllers.ControlloreOperatori import ControlloreOperatori

class VistaModificaTurno(QtWidgets.QMainWindow):
    def __init__(self, parent, turno):
        super(VistaModificaTurno, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/modifica_turno.ui', self)  # Load the .ui file
        self.turno = turno
        self.controller = ControlloreTurni()
        self.controllore_mezzo = ControlloreMezzo()
        self.controllore_operatori = ControlloreOperatori()
        self.annulla_button.clicked.connect(self.close)
        self.salva_button.clicked.connect(self.salva)
        self.date_field.setDateTime(QtCore.QDateTime.fromString(turno.get_data(),"yyyy-mm-dd"))
        self.time_start_field.setDateTime(QtCore.QDateTime.fromString(turno.get_ora_inizio()))
        self.time_end_field.setDateTime(QtCore.QDateTime.fromString(turno.get_ora_fine()))
        self.update()

    def salva(self):
        self.turno.set_servizio(45)
        self.turno.set_data(self.date_field.date().toString("yyyy-MM-dd"))
        self.turno.set_ora_inizio(self.time_start_field.time().toString()) 
        self.turno.set_ora_fine(self.time_end_field.time().toString())
        self.turno.set_mezzo(self.combo_mezzi.currentText())
        self.turno.set_operatore(self.combo_operatori.currentText())
        self.controller.modifica_turno(self.turno)  
        self.modifica_dialog=DialogModifica()
        self.modifica_dialog.exec() 
        self.close()
        self.parent().update()
        
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

    def update(self):
        mezzi = self.controllore_mezzo.get_mezzi()
        id_mezzi = []
        for mezzo in mezzi:
            id = mezzo.get_id_mezzo()
            id_mezzi.append(str(id))
        self.combo_mezzi.addItems(id_mezzi)
        operatori = self.controllore_operatori.get_operatori()
        id_operatori = []
        for operatore in operatori:
            id = operatore.get_id()
            id_operatori.append(str(id))
        self.combo_operatori.addItems(id_operatori)
        self.tabella_mezzi.setRowCount(0)
        self.tabella_operatori.setRowCount(0)
        self.inserisci_tabella_mezzi(self.controllore_mezzo.get_mezzi())
        self.inserisci_tabella_operatori(self.controllore_operatori.get_operatori())
        

class DialogModifica(QtWidgets.QDialog):
    def __init__(self):
        super(DialogModifica, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/dialog_modifica.ui', self)  # Load the .ui file
