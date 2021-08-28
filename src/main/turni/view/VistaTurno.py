from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaTurno(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaTurno, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/visualizza_turno.ui', self)  # Load the .ui file
        self.elimina_button.clicked.connect(self.go_elimina)

    def go_elimina(self):
            self.dialog_elimina = DialogElimina()
            self.dialog_elimina.exec()


class DialogElimina(QtWidgets.QDialog):
    def __init__(self):
        super(DialogElimina, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/dialog_elimina.ui', self)  # Load the .ui file