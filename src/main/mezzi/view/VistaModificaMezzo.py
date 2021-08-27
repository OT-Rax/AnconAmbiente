from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaModificaMezzo(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaModificaMezzo, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/modifica_mezzo.ui', self)  # Load the .ui file