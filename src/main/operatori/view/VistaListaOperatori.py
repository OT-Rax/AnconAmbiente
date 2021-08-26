from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from operatori.view.VistaInserimentoOperatore import VistaInserimentoOperatore

class VistaListaOperatori(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaOperatori, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/operatori.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)

    def go_inserisci(self):
        self.vista_inserimentooperatore = VistaInserimentoOperatore()
        self.vista_inserimentooperatore.show()
