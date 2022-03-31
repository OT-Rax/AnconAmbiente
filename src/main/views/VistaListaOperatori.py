from PyQt5 import QtWidgets, uic
import sqlite3
import os
import sys
import xz_rc

from views.VistaInserimentoOperatore import VistaInserimentoOperatore
from views.VistaModificaOperatore import VistaModificaOperatore
from views.VistaOperatore import VistaOperatore

class VistaListaOperatori(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaListaOperatori, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/operatori.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)
        print(os.getcwd())
        self.update()

    def go_inserisci(self):
        self.vista_inserimentooperatore = VistaInserimentoOperatore()
        self.vista_inserimentooperatore.show()

    def go_modifica(self):
        self.vista_modificaoperatore = VistaModificaOperatore()
        self.vista_modificaoperatore.show()

    def go_visualizza(self):
        self.vista_operatore = VistaOperatore()
        self.vista_operatore.show()

    def update(self):
        con = sqlite3.connect('db/AAdb')
        cur = con.cursor()
        for row in cur.execute('SELECT ID, Nome, Cognome, Stato FROM Operatori'):
            print(row)
        con.close()
