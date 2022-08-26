from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaTurno(QtWidgets.QMainWindow):
    def __init__(self,parent,turno):
        super(VistaTurno, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/visualizza_turno.ui', self)  # Load the .ui file
        self.turno = turno
        self.parent = parent
        self.id_label.setText(str(turno.get_id()))
        self.ora_inizio_label.setText(turno.get_ora_inizio())
        self.ora_fine_label.setText(turno.get_ora_fine())
        self.servizio_label.setText(turno.get_servizio())
        self.mezzo1_label.setText(turno.get_mezzo)
        self.operatore1_label.setText(turno.get_operatore())
        self.elimina_button.clicked.connect(self.go_elimina)

    def go_elimina(self):
            self.dialog_elimina = DialogElimina()
            self.dialog_elimina.exec()

class DialogElimina(QtWidgets.QDialog):
    def __init__(self):
        super(DialogElimina, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/dialog_elimina.ui', self)  # Load the .ui file