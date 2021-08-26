from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from turni.view.VistaInserimentoTurno import VistaInserimentoTurno

class VistaListaTurni(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaTurni, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/turni.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)

    def go_inserisci(self):
        self.vista_inserimentoturno = VistaInserimentoTurno()
        self.vista_inserimentoturno.show()