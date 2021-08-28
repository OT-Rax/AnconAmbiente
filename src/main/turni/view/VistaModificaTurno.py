from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaModificaTurno(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaModificaTurno, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/modifica_turno.ui', self)  # Load the .ui file
        self.salva_button.clicked.connect(self.salva)

    def salva(self):
        self.modifica_dialog=DialogModifica()
        self.modifica_dialog.exec()

class DialogModifica(QtWidgets.QDialog):
    def __init__(self):
        super(DialogModifica, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/dialog_modifica.ui', self)  # Load the .ui file
