from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from views.VistaInserimentoCliente import VistaInserimentoCliente
from views.VistaModificaCliente import VistaModificaCliente
from views.VistaCliente import VistaCliente

class VistaListaClienti(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaClienti, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/clienti.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)

    def go_inserisci(self):
        self.vista_inserimentocliente=VistaInserimentoCliente()
        self.vista_inserimentocliente.show()

    def go_modifica(self):
        self.vista_modificacliente=VistaModificaCliente()
        self.vista_modificacliente.show()

    def go_visualizza(self):
        self.vista_cliente=VistaCliente()
        self.vista_cliente.show()
