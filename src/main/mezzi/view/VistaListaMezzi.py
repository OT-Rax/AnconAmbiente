from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from mezzi.view.VistaInserimentoMezzo import VistaInserimentoMezzo

class VistaListaMezzi(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaMezzi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/mezzi.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)

    def go_inserisci(self):
        self.vista_inserimentomezzo = VistaInserimentoMezzo()
        self.vista_inserimentomezzo.show()