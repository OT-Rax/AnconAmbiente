from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from utenti.view.VistaInserimentoUtente import VistaInserimentoUtente

class VistaListaUtenti(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaUtenti, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/utenti.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)

    def go_inserisci(self):
        self.vista_inserimentoutente = VistaInserimentoUtente()
        self.vista_inserimentoutente.show()
