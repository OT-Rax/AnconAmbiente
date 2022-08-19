from PyQt5 import QtWidgets, uic
from datetime import date
import sys
import xz_rc

from controllers.ControlloreOperatori import ControlloreOperatori

class VistaInserimentoOperatore(QtWidgets.QMainWindow):
    controller = ControlloreOperatori()

    def __init__(self, parent):
        super(VistaInserimentoOperatore, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_operatore.ui', self)  # Load the .ui file
        self.annulla_button.clicked.connect(self.close)
        self.inserisci_button.clicked.connect(self.inserisci)
        self.cf_field.setInputMask("AAAAAA00A00A000A")
        print(self.parent().children())
        #self.nome_field.setValidator()

    def inserisci(self):
        #Inserisci controllo validita caratteri, lunghezza e coerenza
        nome=self.nome_field.text()
        cognome=self.cognome_field.text()
        cf=self.cf_field.text()
        data_nascita=self.nascita_datepicker.date()
        patenti=[]
        data_fine_contratto = self.finecontratto_datepicker.date().toString()
        if  nome is None or cognome is None or len(cf)!=16 or data_nascita >= date.today():
            print("Qualcosa non va")
        else:
            #try:
                self.controller.insert_operatore(nome, cognome, data_nascita.toString("yyyy-MM-dd"), cf, None , 0)
                #finestra pop up a buon fine
                self.close()
                self.parent().update()
            #except:
                #finestra pop up qualcosa e andato storto;
                #print("Qualcosa non va nell'inserimento")
