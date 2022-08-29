from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaInserimentoServizio(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaInserimentoServizio, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_servizio.ui', self)  # Load the .ui file
        # self.annulla_button.clicked.connect(self.close)
        # self.inserisci_button.clicked.connect(self.inserisci)

    # def inserisci(self):
    #