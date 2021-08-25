from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaListaOperatori(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaOperatori, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/operatori.ui', self)  # Load the .ui file
