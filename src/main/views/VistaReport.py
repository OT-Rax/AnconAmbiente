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
        self.opzione_combo.currentIndexChanged.connect(self.terza)

        self.controller = ControlloreReport()

    def prima(self):
        # Metodo attivato dalla prima combobox
        if(self.entita_combo.currentText() == 'Mezzi'):
            self.oggetto_combo.clear()
            self.oggetto_combo.addItem('Tipo')
            self.oggetto_combo.addItem('Allestimento')
        if(self.entita_combo.currentText() == 'Servizi'):
            self.oggetto_combo.clear()
            self.oggetto_combo.addItem('Per cliente')
            self.oggetto_combo.addItem('Numero di volte')
        if (self.entita_combo.currentText() == 'Turni'):
            self.oggetto_combo.clear()
            self.oggetto_combo.addItem('Operatore')
            self.oggetto_combo.addItem('Mezzo')


    def seconda(self):
        # Metodo attivato dalla seconda combobox
        if (self.oggetto_combo.currentText() == 'Tipo'):
            self.opzione_combo.clear()
            righe = self.controller.mezzo_tipo()
            for row in righe:
                self.risultato_textedit.append(row)
        if (self.oggetto_combo.currentText() == 'Allestimento'):
            self.opzione_combo.clear()
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

        if (self.oggetto_combo.currentText() == 'Per cliente'):
            self.opzione_combo.clear()
            operatori = self.controller.get_Clienti()
            self.opzione_combo.clear()
            for row in operatori:
                self.opzione_combo.addItem(row)

        if (self.oggetto_combo.currentText() == 'Numero di volte'):
            self.opzione_combo.clear()
            data1 = self.da_datepicker.date().toString("yyyy-MM-dd")
            data2 = self.a_datepicker.date().toString("yyyy-MM-dd")
            righe = self.controller.s_ser(data1, data2)
            for row in righe:
                self.risultato_textedit.append(row)

    def terza(self):
        if(self.entita_combo.currentText() == 'Servizi'):
            if (self.oggetto_combo.currentText() == 'Per cliente'):
                data1 = self.da_datepicker.date().toString("yyyy-MM-dd")
                data2 = self.a_datepicker.date().toString("yyyy-MM-dd")
                id = self.opzione_combo.currentText()
                righe = self.controller.s_cli(id, data1, data2)
                for row in righe:
                    self.risultato_textedit.append(row)

        if (self.entita_combo.currentText() == 'Turni'):
            if (self.oggetto_combo.currentText() == 'Operatori'):
                data1 = self.da_datepicker.date().toString("yyyy-MM-dd")
                data2 = self.a_datepicker.date().toString("yyyy-MM-dd")
                id = self.opzione_combo.currentText()
                righe = self.controller.s_cli(id, data1, data2)
                for row in righe:
                    self.risultato_textedit.append(row)
            if (self.oggetto_combo.currentText() == 'Mezzi'):
                data1 = self.da_datepicker.date().toString("yyyy-MM-dd")
                data2 = self.a_datepicker.date().toString("yyyy-MM-dd")
                id = self.opzione_combo.currentText()
                righe = self.controller.s_cli(id, data1, data2)
                for row in righe:
                    self.risultato_textedit.append(row)








