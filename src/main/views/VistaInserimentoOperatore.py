from PyQt5 import QtWidgets, uic, QtCore
from datetime import date
import sys
import xz_rc

from controllers.ControlloreOperatori import ControlloreOperatori

class VistaInserimentoOperatore(QtWidgets.QMainWindow):
    controller = ControlloreOperatori()

    def __init__(self, parent):
        # Costruttore 'VistaInserimentoOperatore'
        # :param parent: Vista che ha richiesto l'utilizzo di questa vista, posso utilizzare i metodi di parent
        super(VistaInserimentoOperatore, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/inserimento_operatore.ui', self)  # Load the .ui file
        self.annulla_button.clicked.connect(self.close)
        self.inserisci_button.clicked.connect(self.inserisci)
        self.cf_field.setInputMask("AAAAAA00A00A000A")
        self.indeterminato_checkbox.stateChanged.connect(self.indeterminato_changed)
        self.finecontratto_datepicker.setMinimumDate(QtCore.QDate.currentDate())
        self.nascita_datepicker.setMaximumDate(QtCore.QDate.currentDate())
        self.nome_field.editingFinished.connect(self.check_nome)
        self.cognome_field.editingFinished.connect(self.check_cognome)
        self.cf_field.textChanged.connect(self.check_cf)
        #self.nome_field.setValidator()

    def inserisci(self):
        # Metodo per inserimento nuovo operatore

        #Inserisci controllo validita caratteri, lunghezza e coerenza
        nome=self.nome_field.text()
        cognome=self.cognome_field.text()
        cf=self.cf_field.text()
        data_nascita=self.nascita_datepicker.date()
        patenti=[]
        data_finecontratto = None if self.indeterminato_checkbox.isChecked() else self.finecontratto_datepicker.date().toString("yyyy-MM-dd")
        nome_validity = self.check_nome()
        cognome_validity = self.check_cognome()
        cf_validity = self.check_cf()
        if nome_validity and cognome_validity and cf_validity:
            #try:
            self.controller.insert_operatore(nome, cognome, data_nascita.toString("yyyy-MM-dd"), cf, 0, data_finecontratto)
            #finestra pop up a buon fine
            self.close()
            self.parent().update()
            #except:
                #finestra pop up qualcosa e andato storto;
                #print("Qualcosa non va nell'inserimento")

    def indeterminato_changed(self):
        # Metodo per rendere campo fine contratto abilitato
        self.finecontratto_datepicker.setEnabled(not self.finecontratto_datepicker.isEnabled())

    def check_nome(self):
        # Metodo per controllo correttezza del campo 'nome'
        if len(self.nome_field.text()) == 0:
            self.nome_error.setText("Inserire nome dell'operatore")
            return False
        else:
            self.nome_error.setText("")
            return True

    def check_cognome(self):
        # Metodo per controllo correttezza del campo 'cognome'
        if len(self.cognome_field.text()) == 0:
            self.cognome_error.setText("Inserire cognome dell'operatore")
            return False
        else:
            self.cognome_error.setText("")
            return True

    def check_cf(self):
        # Metodo per controllo correttezza del campo 'cf'
        if len(self.cf_field.text())!=16:
            self.cf_error.setText("Il codice fiscale deve essere lungo 16 caratteri")
            return False
        else:
            self.cf_error.setText("")
            return True
