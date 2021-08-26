from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from servizi.view.VistaInserimentoServizio import VistaInserimentoServizio

class VistaListaServizi(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaServizi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/servizi.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)

    def go_inserisci(self):
        self.vista_inserimentoservizio = VistaInserimentoServizio()
        self.vista_inserimentoservizio.show()