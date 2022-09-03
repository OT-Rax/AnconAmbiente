from PyQt5 import QtWidgets, uic, QtCore
import sys
import xz_rc

from controllers.ControlloreServizi import ControlloreServizi
from controllers.ControlloreClienti import ControlloreClienti
from views.VistaListaClienti import VistaListaClienti

class VistaModificaServizio(QtWidgets.QMainWindow):
    controller = ControlloreServizi() 
    controllerClienti = ControlloreClienti()

    def __init__(self,parent, servizio):
        super(VistaModificaServizio, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/modifica_servizio.ui', self)  # Load the .ui file
        self.servizio = servizio
        self.annulla_button.clicked.connect(self.close)
        self.salva_button.clicked.connect(self.modifica)
        self.tipo_field.editingFinished.connect(self.check_tipo)
        self.luogo_field.editingFinished.connect(self.check_luogo)
        self.periodicita_checkbox.stateChanged.connect(self.periodicita_changed)
        self.inizio_datepicker.editingFinished.connect(self.inizio_edited)
        self.fine_datepicker.setMinimumDate(QtCore.QDate.currentDate())
        self.clienti_button.clicked.connect(self.go_clienti)
        id = self.controllerClienti.get_idclienti()
        for i in range(len(id)):
            self.cliente_combo.addItem(str(id[i]))
        self.tipo_field.setText(self.servizio.get_tipo())
        self.cliente_combo.setCurrentText(str(self.servizio.get_id_cliente()))
        self.luogo_field.setText(self.servizio.get_luogo())
        self.inizio_datepicker.setDateTime(QtCore.QDateTime.fromString(servizio.get_datainizio(),"yyyy-mm-dd"))
        self.fine_datepicker.setDateTime(QtCore.QDateTime.fromString(servizio.get_datafine(),"yyyy-mm-dd"))
        if servizio.get_periodicita() is None:
            self.periodicita_checkbox.setChecked(True)
            self.ripetizione_box.setEnabled(False)
            self.periodicita_combo.setEnabled(False)
        else:
            self.ripetizione_box.setValue(servizio.get_ripetizione())
            if servizio.get_periodicita() == "Giornaliero":
                self.periodicita_combo.setCurrentIndex(0)
            elif servizio.get_periodicita() == "Settimanale":
                self.periodicita_combo.setCurrentIndex(1)
            elif servizio.get_periodicita() == "Mensile":
                self.periodicita_combo.setCurrentIndex(2)
            elif servizio.get_periodicita() == "Annuale":
                self.periodicita_combo.setCurrentIndex(3)


    def periodicita_changed(self):
        self.ripetizione_box.setEnabled(not self.ripetizione_box.isEnabled())
        self.periodicita_combo.setEnabled(not self.periodicita_combo.isEnabled())

    def inizio_edited(self):
        self.fine_datepicker.setMinimumDate(self.inizio_datepicker.date())

    def modifica(self):
        id_cliente = self.cliente_combo.currentText()
        tipo = self.tipo_field.text()
        luogo = self.luogo_field.text()
        data_inizio = self.inizio_datepicker.date().toString("yyyy-MM-dd")
        data_fine = self.fine_datepicker.date().toString("yyyy-MM-dd")
        if self.periodicita_checkbox.isChecked():
            ripetizione = None
            periodicita = None
        else:
            ripetizione = self.ripetizione_box.value()
            if self.periodicita_combo.currentIndex() == 0:
                periodicita = "Giornaliero"
            elif self.periodicita_combo.currentIndex() == 1:
                periodicita = "Settimanale"
            elif self.periodicita_combo.currentIndex() == 2:
                periodicita = "Mensile"
            elif self.periodicita_combo.currentIndex() == 3:
                periodicita = "Annuale"
        tipo_validity = self.check_tipo()
        luogo_validity = self.check_luogo()
        cliente_validity = self.check_cliente()
        if tipo_validity and luogo_validity and cliente_validity:
            self.servizio.set_id_cliente(id_cliente)
            self.servizio.set_tipo(tipo)
            self.servizio.set_luogo(luogo)
            self.servizio.set_datainizio(data_inizio)
            self.servizio.set_datafine(data_fine)
            self.servizio.set_ripetizione(ripetizione)
            self.servizio.set_periodicita(periodicita)
            self.controller.update_servizio(self.servizio)
            self.close()
            self.parent().update()

    def check_tipo(self):
        if len(self.tipo_field.text()) == 0:
            self.tipo_error.setText("Inserire tipo del servizio")
            return False
        else:
            self.tipo_error.setText("")
            return True

    def check_luogo(self):
        if len(self.luogo_field.text()) == 0:
            self.luogo_error.setText("Inserire luogo del servizio")
            return False
        else:
            self.luogo_error.setText("")
            return True
    
    def check_cliente(self):
        if self.cliente_combo.currentText() == "":
            self.cliente_error.setText("Inserire cliente del servizio")
            return False
        else:
            self.cliente_error.setText("")
            return True

    def go_clienti(self):
        self.vista_clienti = VistaListaClienti()
        self.vista_clienti.show()


