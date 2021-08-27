from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaServizio(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaServizio, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/visualizza_servizio.ui', self)  # Load the .ui file