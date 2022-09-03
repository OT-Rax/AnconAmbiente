from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from controllers.ControlloreClienti import ControlloreClienti
from controllers.ControlloreServizi import ControlloreServizi


class VistaInserimentoServizio(QtWidgets.QMainWindow):
    controllerClienti = ControlloreClienti()
    controller = ControlloreServizi()

    def __init__(self, parent):
        super(VistaInserimentoServizio, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_servizio.ui', self)  # Load the .ui file
        self.annulla_button.clicked.connect(self.close)
        self.inserisci_button.clicked.connect(self.inserisci)
        self.tipo_field.editingFinished.connect(self.check_tipo)
        self.luogo_field.editingFinished.connect(self.check_luogo)
        id = self.controller.get_idclienti()
        for i in range(len(id)):
            self.cliente_combo.addItem(id[i])


    def inserisci(self):
        tipo = self.tipo_field.text()
        id_cliente = self.cliente_combo.selectedItem()
        luogo = self.luogo_field.text()
        tipo_validity = self.check_tipo()
        luogo_validity = self.check_luogo()
        if tipo_validity and luogo_validity and id_cliente is not None:
            self.controller.insert_servizio(tipo, id_cliente, luogo)
            self.close()
            self.parent().update()

    def check_tipo(self):
        if len(self.nome_field.text()) == 0:
            self.tipo_error.setText("Inserire tipo del servizio")
            return False
        else:
            self.tipo_error.setText("")
            return True

    def check_luogo(self):
        if len(self.nome_field.text()) == 0:
            self.luogo_error.setText("Inserire luogo del servizio")
            return False
        else:
            self.luogo_error.setText("")
            return True
