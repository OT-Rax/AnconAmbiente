from PyQt5 import QtWidgets, uic, QtCore, Qt
import os
import sys
import xz_rc

from controllers.ControlloreReport import ControlloreReport
class VistaReport(QtWidgets.QMainWindow):
    def __init__(self):
        # Costruttore 'VistaReport'
        super(VistaReport, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/report.ui', self)  # Load the .ui file
        self.entita_combo.currentIndexChanged.connect(self.prima)
        self.oggetto_combo.currentIndexChanged.connect(self.seconda)

        self.controller = ControlloreReport()

    def prima(self):
        # Metodo attivato dalla prima combobox
        if(self.entita_combo.currentText() == 'Mezzi'):
            self.oggetto_combo.clear()
            self.oggetto_combo.addItem('Tipo')
            self.oggetto_combo.addItem('Allestimento')
        if(self.entita_combo.currentText() == 'Servizi'):
            self.oggetto_combo.clear()
            self.oggetto_combo.addItem('Operatore')
            self.oggetto_combo.addItem('Mezzo')
        if (self.entita_combo.currentText() == 'Turni'):
            self.oggetto_combo.clear()
            self.oggetto_combo.addItem('Operatore')
            self.oggetto_combo.addItem('Mezzo')


    def seconda(self):
        # Metodo attivato dalla seconda combobox
        if (self.oggetto_combo.currentText() == 'Tipo'):
            righe = self.controller.mezzo_tipo()
            for row in righe:
                self.risultato_textedit.append(row)
        if (self.oggetto_combo.currentText() == 'Allestimento'):
            righe = self.controller.mezzo_all()
            for row in righe:
                self.risultato_textedit.append(row)

        if (self.oggetto_combo.currentText() == 'Operatore'):
            operatori = self.controller.get_Operatori()
            self.opzione_combo.clear()
            for row in operatori:
                self.opzione_combo.addItem(row)
        if (self.oggetto_combo.currentText() == 'Mezzo'):
            self.opzione_combo.clear()
            mezzi = self.controller.get_Operatori()
            for row in mezzi:
                self.opzione_combo.addItem(row)








