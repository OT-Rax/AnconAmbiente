from PyQt5 import QtWidgets, QtCore, uic
import sys
import xz_rc

from controllers.ControlloreOperatori import ControlloreOperatori

class VistaModificaOperatore(QtWidgets.QMainWindow):
    controller = ControlloreOperatori()

    def __init__(self, parent, operatore):
        super(VistaModificaOperatore, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/modifica_operatore.ui', self)  # Load the .ui file
        self.operatore=operatore
        self.annulla_button.clicked.connect(self.close)
        self.salva_button.clicked.connect(self.modifica)
        self.nome_field.setText(operatore.get_nome())
        self.cognome_field.setText(operatore.get_cognome())
        self.cf_field.setText(operatore.get_cf())
        self.nascita_datepicker.setDateTime(QtCore.QDateTime.fromString(operatore.get_datanascita(),"yyyy-mm-dd"))
        self.stato_combo.setCurrentIndex(operatore.get_stato())
        self.nome_field.editingFinished.connect(self.check_nome)
        self.cognome_field.editingFinished.connect(self.check_cognome)
        self.cf_field.textChanged.connect(self.check_cf)
        self.cf_field.setInputMask("AAAAAA00A00A000A")
        self.finecontratto_datepicker.setMinimumDate(QtCore.QDate.currentDate())
        self.nascita_datepicker.setMaximumDate(QtCore.QDate.currentDate())

    def modifica(self):
        nome_validity = self.check_nome()
        cognome_validity = self.check_cognome()
        cf_validity = self.check_cf()
        if nome_validity and cognome_validity and cf_validity:
            self.operatore.set_nome(self.nome_field.text())
            self.operatore.set_cognome(self.cognome_field.text())
            self.operatore.set_datanascita(self.nascita_datepicker.date().toString("yyyy-MM-dd"))
            self.operatore.set_datacontratto(None if self.indeterminato_checkbox.isChecked() else self.finecontratto_datepicker.date().toString("yyyy-MM-dd"))
            self.operatore.set_stato(self.stato_combo.currentIndex())
            self.controller.modifica_operatore(self.operatore)
            self.parent().update()
            self.close()


    def check_nome(self):
        if len(self.nome_field.text()) == 0:
            self.nome_error.setText("Inserire nome dell'operatore")
            return False
        else:
            self.nome_error.setText("")
            return True

    def check_cognome(self):
        if len(self.cognome_field.text()) == 0:
            self.cognome_error.setText("Inserire cognome dell'operatore")
            return False
        else:
            self.cognome_error.setText("")
            return True

    def check_cf(self):
        if len(self.cf_field.text())!=16:
            self.cf_error.setText("Il codice fiscale deve essere lungo 16 caratteri")
            return False
        else:
            self.cf_error.setText("")
            return True
