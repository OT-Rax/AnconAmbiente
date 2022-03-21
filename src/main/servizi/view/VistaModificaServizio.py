from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaModificaServizio(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaModificaServizio, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/modifica_servizio.ui', self)  # Load the .ui file