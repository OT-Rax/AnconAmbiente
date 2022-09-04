from PyQt5 import QtWidgets, uic, QtCore
from datetime import date
import sys
import xz_rc

from controllers.ControlloreClienti import ControlloreClienti

class VistaInserimentoCliente(QtWidgets.QMainWindow):
    controller = ControlloreClienti()

    def __init__(self, parent):
        # Costruttore 'VistaInserimentoCliente'
        # :param parent: Vista che ha richiesto l'utilizzo di questa vista, posso utilizzare i metodi di parent
        super(VistaInserimentoCliente, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_cliente.ui', self)  # Load the .ui file
        self.annulla_button.clicked.connect(self.close)
        self.inserisci_button.clicked.connect(self.inserisci)
        self.cf_field.setInputMask("AAAAAA00A00A000A")
        self.nascita_datepicker.setMaximumDate(QtCore.QDate.currentDate())
        self.nome_field.editingFinished.connect(self.check_nome)
        self.cognome_field.editingFinished.connect(self.check_cognome)
        self.cf_field.textChanged.connect(self.check_cf)
        #self.nome_field.setValidator()

    def inserisci(self):
        # Metodo per inserire un nuovo cliente

        #Inserisci controllo validita caratteri, lunghezza e coerenza
        nome=self.nome_field.text()
        cognome=self.cognome_field.text()
        data_nascita=self.nascita_datepicker.date()
        cf=self.cf_field.text()
        partitaiva=self.partitaiva_field.text()
        indirizzo=self.indirizzo_field.text()
        email=self.email_field.text()
        telefono=self.telefono_field.text()
        nome_validity = self.check_nome()
        cognome_validity = self.check_cognome()
        cf_validity = self.check_cf()
        if nome_validity and cognome_validity and cf_validity:
            #try:
            self.controller.insert_cliente(nome, cognome, data_nascita.toString("yyyy-MM-dd"), cf, partitaiva, indirizzo, email, telefono)
            #finestra pop up a buon fine
            self.close()
            self.parent().update()
            #except:
                #finestra pop up qualcosa e andato storto;
                #print("Qualcosa non va nell'inserimento")

    def check_nome(self):
        # Metodo per controllo correttezza del campo 'nome'

        if len(self.nome_field.text()) == 0:
            self.nome_error.setText("Inserire nome dell'cliente")
            return False
        else:
            self.nome_error.setText("")
            return True

    def check_cognome(self):
        # Metodo per controllo correttezza del campo 'cognome'

        if len(self.cognome_field.text()) == 0:
            self.cognome_error.setText("Inserire cognome dell'cliente")
            return False
        else:
            self.cognome_error.setText("")
            return True

    def check_cf(self):
        # Metodo per controllo correttezza del campo 'cf'

        if len(self.cf_field.text())!=16:
            self.cf_error.setText("Il codice fiscale deve essere lungo 16 caratteri")
            return False
        else:
            self.cf_error.setText("")
            return True
