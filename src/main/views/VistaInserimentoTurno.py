from PyQt5 import QtWidgets, uic, QtCore
import sys
import xz_rc

from controllers.ControlloreServizi import ControlloreServizio
from controllers.ControlloreMezzi import ControlloreMezzo
from controllers.ControlloreOperatori import ControlloreOperatori
from controllers.ControlloreTurni import ControlloreTurni

controller = ControlloreTurni()
controller2 = ControlloreServizio()
controller_mezzi = ControlloreMezzo()
controller_operatori = ControlloreOperatori()

class VistaInserimentoTurno(QtWidgets.QMainWindow):
    def __init__(self,parent):
        super(VistaInserimentoTurno, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_turno.ui', self)  # Load the .ui file
        self.annulla_button.clicked.connect(self.close)
        self.inserisci_button.clicked.connect(self.inserisci)
        self.date_field.setMinimumDate(QtCore.QDate.currentDate())
        self.tabella_servizi.setRowCount(0)
        self.tabella_mezzi.setRowCount(0)
        self.tabella_operatori.setRowCount(0)
        self.inserisci_tabella_servizi(controller2.get_servizi())
        #aggiungere il get_tipo servizio per la ricerca dei mezzi
        self.inserisci_tabella_mezzi(controller_mezzi.get_mezzi())
        self.inserisci_tabella_operatori(controller_operatori.get_operatori())
        
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
        mezzo = self.get_mezzo_selezionato
        operatore = self.get_operatore_selezionato
        mezzo_validity = self.check_mezzo()
        operatore_validity = self.check_operatore()
        if mezzo_validity and operatore_validity:
            #try:
            controller.insert_turno(servizio, data_turno.toString("yyyy-MM-dd"), ora_inizio.toString(), ora_fine.toString(), str(mezzo), str(operatore))
            #finestra pop up a buon fine
            self.close()
            self.parent().update()
            #except:
                #finestra pop up qualcosa e andato storto;
                #print("Qualcosa non va nell'inserimento")
    
    def check_mezzo(self):
        if self.get_mezzo_selezionato == 0:
            self.warning_label2.setText("Seleziona almeno un mezzo.")
            return False
        else:
            self.warning_label2.setText("")
            return True    

    def check_operatore(self):
        if  self.get_operatore_selezionato == 0:
            self.warning_label3.setText("Seleziona almeno un operatore.")
            return False
        else:
            self.warning_label3.setText("")
            return True    

    def get_mezzo_selezionato(self):
        casella = self.tabella_mezzi.selectedItems()
        id_mezzo = None
        id_mezzo = int(self.tabella_mezzi.item(casella, 0).text())
        return id_mezzo

    def get_operatore_selezionato(self):
        casella = self.tabella_operatori.selectedItems()
        id_operatore = None
        operatore = controller_operatori.get_operatore(int(self.tabella_mezzi.item(casella, 0).text()))
        id_operatore = operatore.get_cognome
        return id_operatore