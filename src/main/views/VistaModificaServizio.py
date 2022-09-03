from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from controllers.ControlloreServizi import ControlloreServizio

class VistaModificaServizio(QtWidgets.QMainWindow):
    controller = ControlloreServizio() 

    def __init__(self, servizio):
        super(VistaModificaServizio, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/modifica_servizio.ui', self)  # Load the .ui file
        self.servizio = servizio
        self.tipo_field.setText(self.servizio.get_tipo())
        self.cliente_combo.setCurrentIndex(self.servizio.get_id_cliente())
        self.luogo_field.setText(self.servizio.get_luogo())
        self.stato_combo.setCurrentIndex(self.servizio.get_stato())
        self.annulla_button.clicked.connect(self.close)
        self.salva_button.clicked.connect(self.modifica)


