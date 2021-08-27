from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaUtente(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaUtente, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/visualizza_utente.ui', self)  # Load the .ui file