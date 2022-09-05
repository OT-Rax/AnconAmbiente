import os

from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from models.Operatore import Operatore
from views.VistaModificaOperatore import VistaModificaOperatore

class VistaOperatore(QtWidgets.QMainWindow):
    def __init__(self, parent, operatore):
        # Costruttore 'VistaOperatore'
        # :param parent: Vista che ha richiesto l'utilizzo di questa vista, posso utilizzare i metodi di parent
        # :param operatore: Operatore dal quale visualizzare le informazioni
        super(VistaOperatore, self).__init__(parent)  # Call the inherited classes __init__ method
        dirname = os.path.dirname(__file__)
        gui_file = os.path.join(dirname, '../gui/visualizza_operatore.ui')
        uic.loadUi(gui_file, self)  # Load the .ui file
        self.operatore=operatore
        self.parent=parent
        self.id_label.setText(str(operatore.get_id()))
        self.nome_label.setText(operatore.get_nome())
        self.cognome_label.setText(operatore.get_cognome())
        self.datanascita_label.setText(operatore.get_datanascita())
        self.cf_label.setText(operatore.get_cf())
        datacontratto=operatore.get_datacontratto()
        if datacontratto is None:
            datacontratto="Indeterminato"
        self.datacontratto_label.setText(datacontratto)
        stato=operatore.get_stato()
        if stato == 0:
            stato = "Disponibile"
        elif stato == 1:
            stato = "In Malattia"
        else:
            stato = "In Ferie"
        self.stato_label.setText(stato)
        self.indietro_button.clicked.connect(self.close)
        self.modifica_button.clicked.connect(self.go_modifica)

    def go_modifica(self):
        # Metodo per passare alla vista di modifica
        self.vista_modificaoperatore = VistaModificaOperatore(self.parent, self.operatore)
        self.vista_modificaoperatore.show()
        self.close()
