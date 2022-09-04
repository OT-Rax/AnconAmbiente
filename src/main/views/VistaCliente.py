from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from models.Cliente import Cliente
from views.VistaModificaCliente import VistaModificaCliente

class VistaCliente(QtWidgets.QMainWindow):
    def __init__(self, parent, cliente):
        # Costruttore 'VistaCliente'
        # :param parent: Vista che ha richiesto l'utilizzo di questa vista, posso utilizzare i metodi di parent
        super(VistaCliente, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/visualizza_cliente.ui', self)  # Load the .ui file
        self.cliente=cliente
        self.parent=parent
        self.id_label.setText(str(cliente.get_id()))
        self.nome_label.setText(cliente.get_nome())
        self.cognome_label.setText(cliente.get_cognome())
        self.datanascita_label.setText(cliente.get_datanascita())
        self.cf_label.setText(cliente.get_cf())
        self.partitaiva_label.setText(cliente.get_partitaiva())
        self.indirizzo_label.setText(cliente.get_indirizzo())
        self.email_label.setText(cliente.get_email())
        self.telefono_label.setText(cliente.get_telefono())
        self.indietro_button.clicked.connect(self.close)
        self.modifica_button.clicked.connect(self.go_modifica)

    def go_modifica(self):
        # Metodo che ci permette di passare alla vista di modifica
        self.vista_modificacliente = VistaModificaCliente(self.parent, self.cliente)
        self.vista_modificacliente.show()
        self.close()
