from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaListaOperatori(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/login.ui', self)  # Load the .ui file
