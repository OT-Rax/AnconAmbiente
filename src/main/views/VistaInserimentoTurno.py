from PyQt5 import QtWidgets, uic, QtCore
import sys
import xz_rc

from controllers.ControlloreServizi import ControlloreServizio
from models.Servizio import Servizio

controller2 = ControlloreServizio(Servizio)

class VistaInserimentoTurno(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaInserimentoTurno, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_turno.ui', self)  # Load the .ui file
        self.annulla_button.clicked.connect(self.close)
        self.inserisci_button.clicked.connect(self.inserisci)
        self.date_field.setMinimumDate(QtCore.QDate.currentDate())
        self.update()

    def update(self):
        self.tabella_servizi.setRowCount(0)
        self.inserisci_tabella(controller2.get_servizi())


    def inserisci_tabella(self, servizi):
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

    def inserisci(self):
        #Inserisci controllo validita caratteri, lunghezza e coerenza
        servizio = self.tabella_servizi.itemDoubleClicked
        data = self.date_field.data()
        ora_inizio = self.time_start_field.time()
        ora_fine = self.time_end_field.time()
        mezzo = self.mezzo1_combo.currentText()
        operatore = self.operatore1_combo.currentText()
        self.controller.insert_operatore(servizio, data, ora_inizio, ora_fine, mezzo, operatore)       
        self.close()
        self.parent().update()

