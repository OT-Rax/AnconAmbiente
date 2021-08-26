from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaInserimentoMezzo(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaInserimentoMezzo, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_mezzo.ui', self)  # Load the .ui file