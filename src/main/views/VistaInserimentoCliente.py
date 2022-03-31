from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaInserimentoCliente(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaInserimentoCliente, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_cliente.ui', self)  # Load the .ui file