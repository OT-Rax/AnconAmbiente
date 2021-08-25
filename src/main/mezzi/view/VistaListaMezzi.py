from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaListaMezzi(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaMezzi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/login.ui', self)  # Load the .ui file