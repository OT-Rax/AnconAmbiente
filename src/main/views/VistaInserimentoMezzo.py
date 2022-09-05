import os

from PyQt5 import QtWidgets, uic
from datetime import date
import sys
import xz_rc

from controllers.ControlloreMezzi import ControlloreMezzi

class VistaInserimentoMezzo(QtWidgets.QMainWindow):
    controller = ControlloreMezzi()

    def __init__(self, parent):
        # Costruttore 'VistaInserimentoMezzo'
        # :param parent: Vista che ha richiesto l'utilizzo di questa vista, posso utilizzare i metodi di parent
        super(VistaInserimentoMezzo, self).__init__(parent)  # Call the inherited classes __init__ method
        dirname = os.path.dirname(__file__)
        gui_file = os.path.join(dirname, '../gui/inserimento_mezzo.ui')
        uic.loadUi(gui_file, self)  # Load the .ui file
        self.annulla_button.clicked.connect(self.close)
        self.inserisci_button.clicked.connect(self.inserisci)
        #print(self.parent().children())

    def inserisci(self):
        # Metodo per inserimento nuovo mezzo
        targa=self.targa_field.text()
        modello=self.modello_field.text()
        allestimento=self.allestimento_field.text()
        data_iscrizione=self.iscrizione_datepicker.date()
        patente=self.patente_combo.currentText()
        targa_validity = self.check_targa()
        modello_validity = self.check_modello()
        allestimento_validity = self.check_allestimento()
        if targa_validity and modello_validity and allestimento_validity:
            #try:
            self.controller.insert_mezzo(targa, modello, allestimento, data_iscrizione.toString("yyyy-MM-dd"), patente, 0)
            #finestra pop up a buon fine
            self.close()
            self.parent().update()
            #except:
                #finestra pop up qualcosa e andato storto;
                #print("Qualcosa non va nell'inserimento")

    def check_targa(self):
        # Metodo per controllo correttezza del campo 'targa'
        if len(self.targa_field.text()) == 0:
            self.targa_error.setText("Inserire targa del mezzo")
            return False
        else:
            self.targa_error.setText("")
            return True

    def check_modello(self):
        # Metodo per controllo correttezza del campo 'modello'
        if len(self.modello_field.text()) == 0:
            self.modello_error.setText("Inserire modello del mezzo")
            return False
        else:
            self.modello_error.setText("")
            return True

    def check_allestimento(self):
        # # Metodo per controllo correttezza del campo 'allestimento'
        if len(self.allestimento_field.text()) == 0:
            self.allestimento_error.setText("Inserire l'allestimento del mezzo")
            return False
        else:
            self.allestimento_error.setText("")
            return True
