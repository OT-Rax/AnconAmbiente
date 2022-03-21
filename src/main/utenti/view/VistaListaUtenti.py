from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from utenti.view.VistaInserimentoUtente import VistaInserimentoUtente
from utenti.view.VistaModificaUtente import VistaModificaUtente
from utenti.view.VistaUtente import VistaUtente

class VistaListaUtenti(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaUtenti, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/utenti.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)

    def go_inserisci(self):
        self.vista_inserimentoutente = VistaInserimentoUtente()
        self.vista_inserimentoutente.show()

    def go_modifica(self):
        self.vista_modificautente = VistaModificaUtente()
        self.vista_modificautente.show()

    def go_visualizza(self):
        self.vista_utente = VistaUtente()
        self.vista_utente.show()