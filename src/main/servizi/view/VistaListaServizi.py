from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from servizi.view.VistaInserimentoServizio import VistaInserimentoServizio
from servizi.view.VistaModificaServizio import VistaModificaServizio
from servizi.view.VistaServizio import VistaServizio

class VistaListaServizi(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaServizi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/servizi.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)

    def go_inserisci(self):
        self.vista_inserimentoservizio = VistaInserimentoServizio()
        self.vista_inserimentoservizio.show()

    def go_modifica(self):
        self.vista_modificaservizio = VistaModificaServizio()
        self.vista_modificaservizio.show()

    def go_visualizza(self):
        self.vista_servizio = VistaServizio()
        self.vista_servizio.show()