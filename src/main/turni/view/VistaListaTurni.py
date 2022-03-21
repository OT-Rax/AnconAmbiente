from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from turni.view.VistaInserimentoTurno import VistaInserimentoTurno
from turni.view.VistaModificaTurno import VistaModificaTurno
from turni.view.VistaTurno import VistaTurno

class VistaListaTurni(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaTurni, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/turni.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)
        self.elimina_button.clicked.connect(self.go_elimina)

    def go_inserisci(self):
        self.vista_inserimentoturno = VistaInserimentoTurno()
        self.vista_inserimentoturno.show()

    def go_modifica(self):
        self.vista_modificaturno = VistaModificaTurno()
        self.vista_modificaturno.show()

    def go_visualizza(self):
        self.vista_turno = VistaTurno()
        self.vista_turno.show()

    def go_elimina(self):
        self.dialog_elimina = DialogElimina()
        self.dialog_elimina.exec()


class DialogElimina(QtWidgets.QDialog):
    def __init__(self):
        super(DialogElimina, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/dialog_elimina.ui', self)  # Load the .ui file