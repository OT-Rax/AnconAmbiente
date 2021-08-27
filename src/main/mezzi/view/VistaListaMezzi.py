from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from mezzi.view.VistaInserimentoMezzo import VistaInserimentoMezzo
from mezzi.view.VistaModificaMezzo import VistaModificaMezzo
from mezzi.view.VistaMezzo import VistaMezzo

class VistaListaMezzi(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaMezzi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/mezzi.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)


    def go_inserisci(self):
        self.vista_inserimentomezzo = VistaInserimentoMezzo()
        self.vista_inserimentomezzo.show()

    def go_modifica(self):
        self.vista_modificamezzo = VistaModificaMezzo()
        self.vista_modificamezzo.show()

    def go_visualizza(self):
        self.vista_mezzo = VistaMezzo()
        self.vista_mezzo.show()