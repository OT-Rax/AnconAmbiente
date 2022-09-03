from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from views.VistaModificaServizio import VistaModificaServizio


class VistaServizio(QtWidgets.QMainWindow):
    def __init__(self, parent, servizio):
        super(VistaServizio, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/visualizza_servizio.ui', self)  # Load the .ui file
        self.servizio = servizio
        self.parent = parent
        self.id_label.setText(str(servizio.get_id()))
        self.tipo_label.setText(servizio.get_tipo())
        self.cliente_label.setText(str(servizio.get_id_cliente()))
        self.luogo_label.setText(str(servizio.get_luogo())) 
        self.periodicita_label.setText("Non periodico" if servizio.get_periodicita() is None else str(servizio.get_ripetizione())+" volte "+servizio.get_periodicita())
        self.indietro_button.clicked.connect(self.close)
        self.modifica_button.clicked.connect(self.go_modifica)

    def go_modifica(self):
        self.vista_modificaservizio = VistaModificaServizio(self, self.servizio)
        self.vista_modificaservizio.show()
        self.close()
