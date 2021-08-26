from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaInserimentoUtente(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaInserimentoUtente, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_utente.ui', self)  # Load the .ui file