from PyQt5 import QtWidgets, uic, QtCore
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
        self.indeterminato_checkbox.stateChanged.connect(self.indeterminato_changed)
        print(self.parent().children())
        self.finecontratto_datepicker.setMinimumDate(QtCore.QDate.currentDate())
        self.nascita_datepicker.setMaximumDate(QtCore.QDate.currentDate())
        #self.nome_field.setValidator()

    def inserisci(self):
        #Inserisci controllo validita caratteri, lunghezza e coerenza
        nome=self.nome_field.text()
        cognome=self.cognome_field.text()
        cf=self.cf_field.text()
        data_nascita=self.nascita_datepicker.date()
        patenti=[]
        data_finecontratto = None if self.indeterminato_checkbox.isChecked() else self.finecontratto_datepicker.date().toString("yyyy-MM-dd")
        print(data_finecontratto)
        if  nome is None or cognome is None or len(cf)!=16 or data_nascita >= date.today():
            print("Qualcosa non va")
        else:
            #try:
            self.controller.insert_operatore(nome, cognome, data_nascita.toString("yyyy-MM-dd"), cf, 0, data_finecontratto)
            #finestra pop up a buon fine
            self.close()
            self.parent().update()
            #except:
                #finestra pop up qualcosa e andato storto;
                #print("Qualcosa non va nell'inserimento")

    def indeterminato_changed(self):
        self.finecontratto_datepicker.setEnabled(not self.finecontratto_datepicker.isEnabled())
