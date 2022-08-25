from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from views.VistaInserimentoServizio import VistaInserimentoServizio
from views.VistaModificaServizio import VistaModificaServizio
from views.VistaServizio import VistaServizio

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

    def inserisci_tabella(self, servizi):
        row = self.tabella_servizi.rowCount()
        for servizio in servizi:
            items = []
            items.append(QtWidgets.QTableWidgetItem(str(servizio.get_id_mezzo())))
            items.append(QtWidgets.QTableWidgetItem(mezzo.get_targa_mezzo()))
            items.append(QtWidgets.QTableWidgetItem(mezzo.get_tipo_mezzo()))
            items.append(QtWidgets.QTableWidgetItem(stato))
            self.tabella_mezzi.insertRow(row)
            column=0
            for item in items:
                item.setFlags(item.flags() &~ QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tabella_mezzi.setItem(row, column, item)
                column+=1
            row+=1
