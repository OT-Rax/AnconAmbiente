import os

from PyQt5 import QtWidgets, QtCore, uic
import sys
import xz_rc

from controllers.ControlloreUtenti import ControlloreUtenti

class VistaModificaUtente(QtWidgets.QMainWindow):
    controller = ControlloreUtenti()

    def __init__(self, parent, utente):
        # Costruttore 'VistaModificaCliente'
        # :param parent: Vista che ha richiesto l'utilizzo di questa vista, posso utilizzare i metodi di parent
        # :param utente: Utente che si vuole modificare
        super(VistaModificaUtente, self).__init__(parent)  # Call the inherited classes __init__ method
        dirname = os.path.dirname(__file__)
        gui_file = os.path.join(dirname, '../gui/modifica_utente.ui')
        uic.loadUi(gui_file, self)  # Load the .ui file
        self.utente=utente
        permessi=utente.get_permessi()
        self.annulla_button.clicked.connect(self.close)
        self.salva_button.clicked.connect(self.modifica)
        self.username_field.setText(utente.get_username())
        self.password_field.setText("password")
        self.operatori_check.setChecked(True if permessi[0]==1 else False)
        self.mezzi_check.setChecked(True if permessi[1]==1 else False)
        self.servizi_check.setChecked(True if permessi[2]==1 else False)
        self.turni_check.setChecked(True if permessi[3]==1 else False)
        self.clienti_check.setChecked(True if permessi[4]==1 else False)
        self.utenti_check.setChecked(True if permessi[5]==1 else False)
        self.username_field.editingFinished.connect(self.check_username)
        self.password_field.editingFinished.connect(self.check_password)
        self.password_field.textChanged.connect(self.password_edited)
        self.password_flag=False

    def modifica(self):
        # Metodo che salva i cambiamenti effettuati
        username_validity = self.check_username()
        password_validity = self.check_password()
        if username_validity and password_validity:
            self.utente.set_username(self.username_field.text())
            if self.password_flag:
                self.utente.set_password()
            self.controller.modifica_utente(self.utente)
            self.parent().update()
            self.close()

    def check_username(self):
        # Metodo per controllo campo 'username'
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
        # Metodo per controllo campo 'password'
        if len(self.password_field.text()) == 0:
            self.password_error.setText("Inserire password dell'utente")
            return False
        else:
            self.password_error.setText("")
            return True

    def password_edited(self):
        # Metodo per settare password_flag a true
        self.password_flag=True
