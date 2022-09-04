from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from views.VistaHome import VistaHome
from controllers.ControlloreUtenti import ControlloreUtenti

class VistaLogin(QtWidgets.QMainWindow):
    def __init__(self):
        # Costruttore 'VistaLogin'
        super(VistaLogin, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/login.ui', self)  # Load the .ui file
        self.login_button.clicked.connect(self.go_home)
        self.controller = ControlloreUtenti()

    def login(self):
        # Metodo che controlla i campi di testo per effettuare il login
        if self.user_field.text() and self.password_field.text():
            if self.controller.check_password(self.user_field.text(), self.password_field.text()):
                self.go_home()  
            else:
                self.warning_label.setText('Username or password is incorrect.')
        else:
            self.warning_label.setText('Please insert username and password')

    def go_home(self):
        # Metodo per visualizzare 'VistaHome'
        self.vista_home=VistaHome()
        self.vista_home.show()
        self.close()
