import os

from PyQt5 import QtWidgets, uic, QtCore
import sys
import xz_rc

from controllers.ControlloreClienti import ControlloreClienti
from controllers.ControlloreServizi import ControlloreServizi
from views.VistaListaClienti import VistaListaClienti

class VistaInserimentoServizio(QtWidgets.QMainWindow):
    controllerClienti = ControlloreClienti()
    controller = ControlloreServizi()

    def __init__(self, parent):
        # Costruttore 'VistaInserimentoServizio'
        # :param parent: Vista che ha richiesto l'utilizzo di questa vista, posso utilizzare i metodi di parent
        super(VistaInserimentoServizio, self).__init__(parent)  # Call the inherited classes __init__ method
        dirname = os.path.dirname(__file__)
        gui_file = os.path.join(dirname, '../gui/inserimento_servizio.ui')
        uic.loadUi(gui_file, self)  # Load the .ui fil
        self.annulla_button.clicked.connect(self.close)
        self.inserisci_button.clicked.connect(self.inserisci)
        self.tipo_field.editingFinished.connect(self.check_tipo)
        self.luogo_field.editingFinished.connect(self.check_luogo)
        self.periodicita_checkbox.stateChanged.connect(self.periodicita_changed)
        self.inizio_datepicker.editingFinished.connect(self.inizio_edited)
        self.inizio_datepicker.setMinimumDate(QtCore.QDate.currentDate())
        self.fine_datepicker.setMinimumDate(QtCore.QDate.currentDate())
        self.clienti_button.clicked.connect(self.go_clienti)
        id = self.controllerClienti.get_idclienti()
        for i in range(len(id)):
            self.cliente_combo.addItem(str(id[i]))

    def periodicita_changed(self):
        # Metodo per abilitare periodicita ad un servizio
        self.ripetizione_box.setEnabled(not self.ripetizione_box.isEnabled())
        self.periodicita_combo.setEnabled(not self.periodicita_combo.isEnabled())

    def inizio_edited(self):
        # Metodo per adeguare data fine servizio in modo tale che non sia inferiore alla data di inizio
        self.fine_datepicker.setMinimumDate(self.inizio_datepicker.date())

    def inserisci(self):
        # Metodo per inserimento nuovo servizio
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
            self.controller.insert_servizio(id_cliente, tipo, luogo, data_inizio, data_fine, ripetizione, periodicita)
            self.close()
            self.parent().update()

    def check_tipo(self):
        # Metodo per controllo correttezza del campo 'tipo'
        if len(self.tipo_field.text()) == 0:
            self.tipo_error.setText("Inserire tipo del servizio")
            return False
        else:
            self.tipo_error.setText("")
            return True

    def check_luogo(self):
        # Metodo per controllo correttezza del campo 'luogo'
        if len(self.luogo_field.text()) == 0:
            self.luogo_error.setText("Inserire luogo del servizio")
            return False
        else:
            self.luogo_error.setText("")
            return True
    
    def check_cliente(self):
        # Metodo per controllo correttezza del campo 'cliente'
        if self.cliente_combo.currentText() == "":
            self.cliente_error.setText("Inserire cliente del servizio")
            return False
        else:
            self.cliente_error.setText("")
            return True

    def go_clienti(self):
        # Metodo per richiamare vista 'VistaListaClienti'
        self.vista_clienti = VistaListaClienti()
        self.vista_clienti.show()
