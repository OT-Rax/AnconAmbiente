from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaModificaCliente(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaModificaCliente, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/modifica_cliente.ui', self)  # Load the .ui file