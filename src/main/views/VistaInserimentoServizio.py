from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from controllers.ControlloreClienti import ControlloreClienti


class VistaInserimentoServizio(QtWidgets.QMainWindow):
    controller = ControlloreClienti()
    def __init__(self):
        super(VistaInserimentoServizio, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_servizio.ui', self)  # Load the .ui file
        self.annulla_button.clicked.connect(self.close)
        self.inserisci_button.clicked.connect(self.inserisci)

    def inserisci(self):
        tipo = self.tipo_field.text()
        id = self.controller.get_idclienti()
        for i in range(len(id)):
            self.cliente_combo.addItem(id[i])
        selected_id = self.cliente_combo.selectedItem()
        self.controller.insert_cliente()
        self.close()
        self.parent().update()
