from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaHome(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaHome, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/home.ui', self)  # Load the .ui file

