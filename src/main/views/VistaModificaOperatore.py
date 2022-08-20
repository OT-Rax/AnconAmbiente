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
        #self.datanascita_datepicker.setCalendarPopup(True) ---- Not needed anymore, put it into ui file
        print(operatore.get_datanascita())
        self.datanascita_datepicker.setDateTime(QtCore.QDateTime.fromString(operatore.get_datanascita(),"yyyy-mm-dd"))
        self.stato_combo.setCurrentIndex(operatore.get_stato())

    def modifica(self):
        self.operatore.set_nome(self.nome_field.text())
        self.operatore.set_cognome(self.cognome_field.text())
        self.operatore.set_datanascita(self.datanascita_datepicker.date().toString("yyyy-MM-dd"))
        self.operatore.set_datacontratto(None if self.indeterminato_checkbox.isChecked() else self.finecontratto_datepicker.date().toString("yyyy-MM-dd"))
        self.operatore.set_stato(self.stato_combo.currentIndex())
        self.controller.modifica_operatore(self.operatore)
        self.parent().update()
        self.close()
