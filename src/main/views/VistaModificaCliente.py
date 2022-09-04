from PyQt5 import QtWidgets, QtCore, uic
import sys
import xz_rc

from controllers.ControlloreClienti import ControlloreClienti

class VistaModificaCliente(QtWidgets.QMainWindow):
    controller = ControlloreClienti()

    def __init__(self, parent, cliente):
        # Costruttore 'VistaModificaCliente'
        # :param parent: Vista che ha richiesto l'utilizzo di questa vista, posso utilizzare i metodi di parent
        # :param cliente: Cliente che si vuole modificare
        super(VistaModificaCliente, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/modifica_cliente.ui', self)  # Load the .ui file
        self.cliente=cliente
        self.annulla_button.clicked.connect(self.close)
        self.salva_button.clicked.connect(self.modifica)
        self.nome_field.setText(cliente.get_nome())
        self.cognome_field.setText(cliente.get_cognome())
        self.cf_field.setText(cliente.get_cf())
        self.partitaiva_field.setText(cliente.get_partitaiva())
        self.indirizzo_field.setText(cliente.get_indirizzo())
        self.email_field.setText(cliente.get_email())
        self.telefono_field.setText(cliente.get_telefono())
        self.nascita_datepicker.setDateTime(QtCore.QDateTime.fromString(cliente.get_datanascita(),"yyyy-mm-dd"))
        self.nome_field.editingFinished.connect(self.check_nome)
        self.cognome_field.editingFinished.connect(self.check_cognome)
        self.cf_field.textChanged.connect(self.check_cf)
        self.cf_field.setInputMask("AAAAAA00A00A000A")
        self.nascita_datepicker.setMaximumDate(QtCore.QDate.currentDate())

    def modifica(self):
        # Metodo che salva i cambiamenti effettuati
        nome_validity = self.check_nome()
        cognome_validity = self.check_cognome()
        cf_validity = self.check_cf()
        if nome_validity and cognome_validity and cf_validity:
            self.cliente.set_nome(self.nome_field.text())
            self.cliente.set_cognome(self.cognome_field.text())
            self.cliente.set_datanascita(self.nascita_datepicker.date().toString("yyyy-MM-dd"))
            self.cliente.set_cf(self.cf_field.text())
            self.cliente.set_partitaiva(self.partitaiva_field.text())
            self.cliente.set_indirizzo(self.indirizzo_field.text())
            self.cliente.set_email(self.email_field.text())
            self.cliente.set_telefono(self.telefono_field.text())
            self.controller.modifica_cliente(self.cliente)
            self.parent().update()
            self.close()


    def check_nome(self):
        # Metodo per controllo campo 'nome'
        if len(self.nome_field.text()) == 0:
            self.nome_error.setText("Inserire nome dell'cliente")
            return False
        else:
            self.nome_error.setText("")
            return True

    def check_cognome(self):
        # Metodo per controllo campo 'cognome'
        if len(self.cognome_field.text()) == 0:
            self.cognome_error.setText("Inserire cognome dell'cliente")
            return False
        else:
            self.cognome_error.setText("")
            return True

    def check_cf(self):
        # Metodo per controllo campo 'cf'
        if len(self.cf_field.text())!=16:
            self.cf_error.setText("Il codice fiscale deve essere lungo 16 caratteri")
            return False
        else:
            self.cf_error.setText("")
            return True
