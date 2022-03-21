from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from operatori.view.VistaInserimentoOperatore import VistaInserimentoOperatore
from operatori.view.VistaModificaOperatore import VistaModificaOperatore
from operatori.view.VistaOperatore import VistaOperatore

class VistaListaOperatori(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaOperatori, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/operatori.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)

    def go_inserisci(self):
        self.vista_inserimentooperatore = VistaInserimentoOperatore()
        self.vista_inserimentooperatore.show()

    def go_modifica(self):
        self.vista_modificaoperatore = VistaModificaOperatore()
        self.vista_modificaoperatore.show()

    def go_visualizza(self):
        self.vista_operatore = VistaOperatore()
        self.vista_operatore.show()