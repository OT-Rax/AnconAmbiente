from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaModificaOperatore(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaModificaOperatore, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/modifica_operatore.ui', self)  # Load the .ui file