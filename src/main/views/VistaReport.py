from PyQt5 import QtWidgets, uic, QtCore, Qt
import os
import sys
import xz_rc
import datetime

from controllers.ControlloreReport import ControlloreReport
from controllers.ControlloreOperatori import ControlloreOperatori
from controllers.ControlloreMezzi import ControlloreMezzi
from controllers.ControlloreServizi import ControlloreServizi
from controllers.ControlloreClienti import ControlloreClienti
from controllers.ControlloreTurni import ControlloreTurni

class VistaReport(QtWidgets.QMainWindow):
    def __init__(self):
        # Costruttore 'VistaReport'
        super(VistaReport, self).__init__()  # Call the inherited classes __init__ method
        dirname = os.path.dirname(__file__)
        gui_file = os.path.join(dirname, '../gui/report.ui')
        uic.loadUi(gui_file, self)  # Load the .ui file
        self.entita_combo.currentIndexChanged.connect(self.entita_changed)
        self.report_button.clicked.connect(self.crea_report)
        self.indietro_button.clicked.connect(self.close)

        self.controller = ControlloreReport()
        self.controller_operatori = ControlloreOperatori()
        self.controller_mezzi = ControlloreMezzi()
        self.controller_servizi = ControlloreServizi()
        self.controller_clienti = ControlloreClienti()
        self.controller_turni = ControlloreTurni()
        
        self.da_datepicker.setDate(QtCore.QDate.currentDate())
        self.a_datepicker.setMinimumDate(QtCore.QDate.currentDate())
        self.da_datepicker.editingFinished.connect(self.inizio_edited)

        self.entita_changed()

    def inizio_edited(self):
        self.a_datepicker.setMinimumDate(self.da_datepicker.date())

    def entita_changed(self):
        # Metodo attivato dalla prima combobox
        if(self.entita_combo.currentText() == 'Operatori'):
            self.id_combo.clear()
            for operatore in self.controller_operatori.get_operatori():
                self.id_combo.addItem(str(operatore.get_id()))
        elif(self.entita_combo.currentText() == 'Mezzi'):
            self.id_combo.clear()
            for mezzo in self.controller_mezzi.get_mezzi():
                self.id_combo.addItem(str(mezzo.get_id_mezzo()))
        elif (self.entita_combo.currentText() == 'Servizi'):
            self.id_combo.clear()
            for servizio in self.controller_servizi.get_servizi():
                self.id_combo.addItem(str(servizio.get_id()))
        elif (self.entita_combo.currentText() == 'Clienti'):
            self.id_combo.clear()
            for cliente in self.controller_clienti.get_clienti():
                self.id_combo.addItem(str(cliente.get_id()))

    def crea_report(self):
        self.risultato_textedit.clear()
        self.risultato_textedit.append("--------------------Report creato il " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "--------------------")
        data_inizio=self.da_datepicker.date().toString("yyyy-MM-dd")
        data_fine=self.a_datepicker.date().toString("yyyy-MM-dd")
        if(self.entita_combo.currentText() == 'Operatori'):
            id_operatore=self.id_combo.currentText()
            operatore=self.controller_operatori.get_operatore(id_operatore)
            turni_operatore=self.controller_turni.get_turni_operatore(id_operatore, data_inizio, data_fine)
            self.risultato_textedit.append("L'operatore con ID " + str(id_operatore) + " dal " + data_inizio + " a " + data_fine + " ha svolto " + str(len(turni_operatore)) + " turni.")
            self.risultato_textedit.append("I turni svolti sono i seguenti:")
            for turno in turni_operatore:
                self.risultato_textedit.append("----------------------------------------------------------------------------------------------------")
                self.risultato_textedit.append("ID Turno:"+str(turno.get_id())+" | ID Servizio:"+str(turno.get_servizio().get_id())+" | Luogo:"+turno.get_servizio().get_luogo()+\
                        " | Da:"+turno.get_data_inizio()+" | A:"+turno.get_data_fine())
                self.risultato_textedit.append("----------------------------------------------------------------------------------------------------")
        elif(self.entita_combo.currentText() == 'Mezzi'):
            id_mezzo=self.id_combo.currentText()
            mezzo=self.controller_mezzi.get_mezzo(id_mezzo)
            turni_mezzo=self.controller_turni.get_turni_mezzo(id_mezzo, data_inizio, data_fine)
            self.risultato_textedit.append("Il mezzo con ID " + str(id_mezzo) + " dal " + data_inizio + " a " + data_fine + " ha svolto " + str(len(turni_mezzo)) + " turni.")
            self.risultato_textedit.append("I turni svolti sono i seguenti:")
            for turno in turni_mezzo:
                self.risultato_textedit.append("----------------------------------------------------------------------------------------------------")
                self.risultato_textedit.append("ID Turno:"+str(turno.get_id())+" | ID Servizio:"+str(turno.get_servizio().get_id())+" | Luogo:"+turno.get_servizio().get_luogo()+\
                        " | Da:"+turno.get_data_inizio()+" | A:"+turno.get_data_fine())
                self.risultato_textedit.append("----------------------------------------------------------------------------------------------------")
        elif (self.entita_combo.currentText() == 'Servizi'):
            id_servizio=self.id_combo.currentText()
            servizio=self.controller_servizi.get_servizio(id_servizio)
            turni_servizio=self.controller_turni.get_turni_servizio(id_servizio, data_inizio, data_fine)
            self.risultato_textedit.append("Per il servizio con ID " + str(id_servizio) + " dal " + data_inizio + " a " + data_fine + " sono stati svolti " + str(len(turni_servizio)) + " turni.")
            self.risultato_textedit.append("I turni svolti sono i seguenti:")
            for turno in turni_servizio:
                self.risultato_textedit.append("----------------------------------------------------------------------------------------------------")
                self.risultato_textedit.append("ID Turno:"+str(turno.get_id())+" | Luogo:"+turno.get_servizio().get_luogo()+" | Da:"+turno.get_data_inizio()+" | A:"+turno.get_data_fine())
                self.risultato_textedit.append("Operatori coinvolti:")
                for operatore in turno.get_operatori():
                    self.risultato_textedit.append("ID Operatore:" + str(operatore.get_id()) + " | Nome:"+operatore.get_nome()+" | Cognome:"+operatore.get_cognome())
                self.risultato_textedit.append("Mezzi coinvolti:")
                for mezzo in turno.get_mezzi():
                    self.risultato_textedit.append("ID Mezzo:" + str(mezzo.get_id_mezzo()) + " | Targa:"+mezzo.get_targa_mezzo()+" | Tipo:"+mezzo.get_tipo_mezzo()+\
                            " | Allestimento:"+mezzo.get_allestimento_mezzo())
                self.risultato_textedit.append("----------------------------------------------------------------------------------------------------")
        elif (self.entita_combo.currentText() == 'Clienti'):
            id_cliente=self.id_combo.currentText()
            cliente=self.controller_clienti.get_cliente(id_cliente)
            turni_cliente=self.controller_turni.get_turni_cliente(id_cliente, data_inizio, data_fine)
            self.risultato_textedit.append("Per il cliente con ID " + str(id_cliente) + " dal " + data_inizio + " a " + data_fine + " sono stati svolti " + str(len(turni_cliente)) + " turni.")
            self.risultato_textedit.append("I turni svolti sono i seguenti:")
            for turno in turni_cliente:
                self.risultato_textedit.append("----------------------------------------------------------------------------------------------------")
                self.risultato_textedit.append("ID Turno:"+str(turno.get_id())+" | ID Servizio:"+str(turno.get_servizio().get_id())+" | Luogo:"+turno.get_servizio().get_luogo()+\
                        " | Da:"+turno.get_data_inizio()+" | A:"+turno.get_data_fine())
                self.risultato_textedit.append("Operatori coinvolti:")
                for operatore in turno.get_operatori():
                    self.risultato_textedit.append("ID Operatore:" + str(operatore.get_id()) + " | Nome:"+operatore.get_nome()+" | Cognome:"+operatore.get_cognome())
                self.risultato_textedit.append("Mezzi coinvolti:")
                for mezzo in turno.get_mezzi():
                    self.risultato_textedit.append("ID Mezzo:" + str(mezzo.get_id_mezzo()) + " | Targa:"+mezzo.get_targa_mezzo()+" | Tipo:"+mezzo.get_tipo_mezzo()+\
                            " | Allestimento:"+mezzo.get_allestimento_mezzo())
                self.risultato_textedit.append("----------------------------------------------------------------------------------------------------")
