from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaMezzo(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaMezzo, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/visualizza_mezzo.ui', self)  # Load the .ui file