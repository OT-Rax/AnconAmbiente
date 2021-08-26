from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from clienti.view.VistaInserimentoCliente import VistaInserimentoCliente

class VistaListaClienti(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaClienti, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/clienti.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)

    def go_inserisci(self):
        self.vista_inserimentocliente=VistaInserimentoCliente()
        self.vista_inserimentocliente.show()