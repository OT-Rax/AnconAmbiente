from PyQt5 import QtWidgets, uic, QtCore
import sys
import xz_rc

from views.VistaInserimentoServizio import VistaInserimentoServizio
from views.VistaModificaServizio import VistaModificaServizio
from views.VistaServizio import VistaServizio
from controllers.ControlloreServizi import ControlloreServizio


class VistaListaServizi(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaServizi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/servizi.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)

    def go_inserisci(self):
        self.vista_inserimentoservizio = VistaInserimentoServizio()
        self.vista_inserimentoservizio.show()

    def go_modifica(self):
        self.vista_modificaservizio = VistaModificaServizio()
        self.vista_modificaservizio.show()

    def go_visualizza(self):
        self.vista_servizio = VistaServizio()
        self.vista_servizio.show()

    def update(self):
        self.tabella_servizi.setRowCount(0)
        self.inserisci_tabella(self.controller.get_servizi())

    def inserisci_tabella(self, servizi):
        row = self.tabella_servizi.rowCount()
        for servizio in servizi:
            items = []
            items.append(QtWidgets.QTableWidgetItem(str(servizio.get_id())))
            items.append(QtWidgets.QTableWidgetItem(servizio.get_tipo()))
            items.append(QtWidgets.QTableWidgetItem(servizio.get_id_cliente()))
            items.append(QtWidgets.QTableWidgetItem(servizio.get_periodicita()))
            self.tabella_servizi.insertRow(row)
            column = 0
            for item in items:
                item.setFlags(item.flags() & ~ QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tabella_servizi.setItem(row, column, item)
                column += 1
            row += 1
