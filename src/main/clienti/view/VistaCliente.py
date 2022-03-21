from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaCliente(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaCliente, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/visualizza_cliente.ui', self)  # Load the .ui file