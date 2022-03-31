from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaOperatore(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaOperatore, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/visualizza_operatore.ui', self)  # Load the .ui file