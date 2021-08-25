from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from operatori.view.VistaListaOperatori import VistaListaOperatori
from mezzi.view.VistaListaMezzi import VistaListaMezzi

class VistaHome(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaHome, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/home.ui', self)  # Load the .ui file
        self.mezzi_button.clicked.connect(self.go_listamezzi())
        self.operatori_button.clicked.connect(self.go_listaoperatori())

    def go_listaoperatori(self):
        self.vista_listaoperatori=VistaListaOperatori()
        self.vista_listaoperatori.show()

    def go_listamezzi(self):
        self.vista_listamezzi=VistaListaMezzi()
        self.vista_listamezzi.show()