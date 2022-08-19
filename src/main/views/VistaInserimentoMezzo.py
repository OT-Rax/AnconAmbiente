from PyQt5 import QtWidgets, uic
from datetime import date
import sys
import xz_rc

from controllers.ControlloreMezzi import ControlloreMezzo

class VistaInserimentoMezzo(QtWidgets.QMainWindow):
    controller = ControlloreMezzo()

    def __init__(self, parent):
        super(VistaInserimentoMezzo, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_mezzo.ui', self)  # Load the .ui file
        self.annulla_button.clicked.connect(self.close)
        self.inserisci_button.clicked.connect(self.inserisci)
        #print(self.parent().children())

    def inserisci(self):
        #Inserisci controllo validita caratteri, lunghezza e coerenza
        targa=self.targa_field.text()
        modello=self.modello_field.text()
        funzione=self.funzione_field.text()
        data_iscrizione=self.iscrizione_datepicker.date()
        patente=self.patente_combo.currentText()
        self.controller.insert_mezzo(targa, modello, funzione, data_iscrizione.toString("yyyy-MM-dd"), patente , 0)
        #finestra pop up a buon fine
        self.close
        self.parent().update()