from PyQt5 import QtWidgets, QtCore, uic
import sys
import xz_rc

class VistaModificaOperatore(QtWidgets.QMainWindow):
    def __init__(self, operatore):
        super(VistaModificaOperatore, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/modifica_operatore.ui', self)  # Load the .ui file
        self.annulla_button.clicked.connect(self.close)
        self.nome_field.setText(operatore.get_nome())
        self.cognome_field.setText(operatore.get_cognome())
        self.cf_field.setText(operatore.get_cf())
        self.datanascita_datepicker.setCalendarPopup(True)
        print(operatore.get_datanascita())
        self.datanascita_datepicker.setDateTime(QtCore.QDateTime.fromString(operatore.get_datanascita(),"yyyy-mm-dd"))
        self.stato_combo.setIndex(operatore.get_stato())
