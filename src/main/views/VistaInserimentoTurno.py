from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaInserimentoTurno(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaInserimentoTurno, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_turno.ui', self)  # Load the .ui file