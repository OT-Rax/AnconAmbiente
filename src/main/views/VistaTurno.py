from PyQt5 import QtWidgets, uic, QtCore
import sys
import xz_rc

from views.VistaModificaTurno import VistaModificaTurno
from controllers.ControlloreServizi import ControlloreServizi
from controllers.ControlloreClienti import ControlloreClienti

class VistaTurno(QtWidgets.QMainWindow):
    def __init__(self,parent,turno):
        super(VistaTurno, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/visualizza_turno.ui', self)  # Load the .ui file

        #Dati Servizio
        #controllore Servizi
        self.controller_servizi = ControlloreServizi()
        #Controllore Clienti
        self.controller_clienti = ControlloreClienti()
        self.turno = turno
        self.parent = parent
        #id, data/ora inizio e data/ora fine  
        self.id_label.setText(str(self.turno.get_id()))
        self.ora_inizio_label.setText(self.turno.get_data_inizio())
        self.ora_fine_label.setText(self.turno.get_data_fine())

        #pulsanti
        self.modifica_button.clicked.connect(self.go_modifica)
        self.annulla_button.clicked.connect(self.close)
        
        #Dati Servizio
        self.servizio = self.controller_servizi.get_servizio(self.turno.get_servizio().get_id())
        self.id_servizio_label.setText(str(self.servizio.get_id()))
        self.tipo_label.setText(self.servizio.get_tipo())
        self.cliente_label.setText(self.controller_clienti.get_cliente(self.servizio.get_id_cliente()).get_nome()+" "+self.controller_clienti.get_cliente(self.servizio.get_id_cliente()).get_cognome())
        self.luogo_label.setText(str(self.servizio.get_luogo()))
        self.data_inizio_label.setText(str(self.servizio.get_datainizio()))
        self.data_fine_label.setText(str(self.servizio.get_datafine()))
        ripetizione=self.servizio.get_ripetizione()
        if self.servizio.get_periodicita() is None:
            self.periodicita="Non periodico"
        elif self.servizio.get_periodicita() == "Giornaliero":
            self.periodicita=str(ripetizione)+" volte al giorno"
        elif self.servizio.get_periodicita() == "Settimanale":
            self.periodicita=str(ripetizione)+" volte a settimana"
        elif self.servizio.get_periodicita() == "Mensile":
            self.periodicita=str(ripetizione)+" volte al mese"
        elif self.servizio.get_periodicita() == "Annuale":
            self.periodicita=str(ripetizione)+" volte all'anno"
        self.periodicita_label.setText(self.periodicita)

        #Dati Mezzi e Dati Operatori
        self.tabella_mezzi.setRowCount(0)
        self.tabella_operatori.setRowCount(0)
        self.update()

        

    def go_modifica(self):
        self.modifica = VistaModificaTurno(self, self.turno)
        self.modifica.show()
        self.close()

    def update(self):
        #get mezzi
        mezzi = self.turno.get_mezzi()
        self.inserisci_tabella_mezzi(mezzi)

        #get operatori
        operatori = self.turno.get_operatori()
        self.inserisci_tabella_operatori(operatori)


    #creazione tabella mezzi
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

    #creazione tabella operatori
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


class DialogElimina(QtWidgets.QDialog):
    def __init__(self):
        super(DialogElimina, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/dialog_elimina.ui', self)  # Load the .ui file