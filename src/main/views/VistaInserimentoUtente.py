from PyQt5 import QtWidgets, uic, QtCore
from datetime import date
import sys
import xz_rc

from controllers.ControlloreUtenti import ControlloreUtenti
from models.Utente import Utente

class VistaInserimentoUtente(QtWidgets.QMainWindow):
    controller = ControlloreUtenti()

    def __init__(self, parent):
        # Costruttore 'VistaInserimentoUtente'
        # :param parent: Vista che ha richiesto l'utilizzo di questa vista, posso utilizzare i metodi di parent
        super(VistaInserimentoUtente, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_utente.ui', self)  # Load the .ui file
        self.annulla_button.clicked.connect(self.close)
        self.inserisci_button.clicked.connect(self.inserisci)
        print(self.parent().children())
        self.username_field.textChanged.connect(self.check_username)
        self.password_field.textChanged.connect(self.check_password)
        #self.nome_field.setValidator()

    def inserisci(self):
        # Metodo per inserimento nuovo utente

        #Inserisci controllo validita caratteri, lunghezza e coerenza
        username=self.username_field.text()
        password=self.password_field.text()
        username_validity = self.check_username()
        password_validity = self.check_password()
        accesso_operatori = 1 if self.operatori_check.isChecked() else 0
        accesso_mezzi = 1 if self.mezzo_check.isChecked() else 0
        accesso_servizi = 1 if self.servizi_check.isChecked() else 0
        accesso_turni = 1 if self.turni_check.isChecked() else 0
        accesso_clienti = 1 if self.clienti_check.isChecked() else 0
        accesso_utenti = 1 if self.utenti_check.isChecked() else 0
        permessi = [accesso_operatori, accesso_mezzi, accesso_servizi, accesso_turni, accesso_clienti, accesso_utenti]
        if username_validity and password_validity:
            self.controller.insert_utente(Utente(0, username, password, permessi))
            self.close()
            self.parent().update()

    def check_username(self):
        # Metodo per controllo correttezza del campo 'username'
        if len(self.username_field.text()) == 0:
            self.username_error.setText("Inserire username dell'utente")
            return False
        elif(self.controller.get_utente_by_username(self.username_field.text()) is not None):
            self.username_error.setText("Username già in uso da un altro utente")
            return False
        else:
            self.username_error.setText("")
            return True

    def check_password(self):
        # Metodo per controllo correttezza del campo 'password'
        if len(self.password_field.text()) == 0:
            self.password_error.setText("Inserire password dell'utente")
            return False
        else:
            self.password_error.setText("")
            return True
