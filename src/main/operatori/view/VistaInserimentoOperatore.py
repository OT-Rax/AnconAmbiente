from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaInserimentoOperatore(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaInserimentoOperatore, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_operatore.ui', self)  # Load the .ui file