from PyQt5 import QtWidgets, uic, QtCore
import os
import sys
import xz_rc

from views.VistaInserimentoMezzo import VistaInserimentoMezzo
from views.VistaModificaMezzo import VistaModificaMezzo
from views.VistaMezzo import VistaMezzo
from controllers.ControlloreMezzi import ControlloreMezzo

class VistaListaMezzi(QtWidgets.QMainWindow):
    controller = ControlloreMezzo()

    def __init__(self):
        super(VistaListaMezzi, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/mezzi.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)
        self.indietr_button.clicked.connect(self.close)

        print(os.getcwd())
        self.update()


    def go_inserisci(self):
        self.vista_inserimentomezzo = VistaInserimentoMezzo(self)
        self.vista_inserimentomezzo.show()

    def go_modifica(self):
        self.vista_modificamezzo = VistaModificaMezzo()
        self.vista_modificamezzo.show()

    def go_visualizza(self):
        caselle_selezionate=self.tabella_mezzi.selectedItems()
        righe_selezionate=[]
        for casella in caselle_selezionate:
            righe_selezionate.append(casella.row())
        for riga in set(righe_selezionate):
            mezzo=self.controller.get_mezzo(int(self.tabella_mezzi.item(riga, 0).text()))
            self.vista_mezzo = VistaMezzo(mezzo)
            self.vista_mezzo.show()
