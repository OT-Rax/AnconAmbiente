from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from views.VistaModificaServizio import VistaModificaServizio
from controllers.ControlloreClienti import ControlloreClienti


class VistaServizio(QtWidgets.QMainWindow):
    def __init__(self, parent, servizio):
        # Costruttore 'VistaServizio'
        # :param parent: Vista che ha richiesto l'utilizzo di questa vista, posso utilizzare i metodi di parent
        # :param Servizio: Servizio dal quale visualizzare le informazioni
        super(VistaServizio, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/visualizza_servizio.ui', self)  # Load the .ui file
        self.controller_clienti = ControlloreClienti()
        self.servizio = servizio
        self.parent = parent
        self.id_label.setText(str(servizio.get_id()))
        self.tipo_label.setText(servizio.get_tipo())
        self.cliente_label.setText(self.controller_clienti.get_cliente(servizio.get_id_cliente()).get_nome()+" "+self.controller_clienti.get_cliente(servizio.get_id_cliente()).get_cognome())
        self.luogo_label.setText(str(servizio.get_luogo()))
        self.data_inizio_label.setText(str(servizio.get_datainizio()))
        self.data_fine_label.setText(str(servizio.get_datafine()))
        ripetizione=servizio.get_ripetizione()
        if servizio.get_periodicita() is None:
            periodicita="Non periodico"
        elif servizio.get_periodicita() == "Giornaliero":
            periodicita=str(ripetizione)+" volte al giorno"
        elif servizio.get_periodicita() == "Settimanale":
            periodicita=str(ripetizione)+" volte a settimana"
        elif servizio.get_periodicita() == "Mensile":
            periodicita=str(ripetizione)+" volte al mese"
        elif servizio.get_periodicita() == "Annuale":
            periodicita=str(ripetizione)+" volte all'anno"
        self.periodicita_label.setText(periodicita)
        self.indietro_button.clicked.connect(self.close)
        self.modifica_button.clicked.connect(self.go_modifica)

    def go_modifica(self):
        # Metodo per passare alla vista di modifica
        self.vista_modificaservizio = VistaModificaServizio(self.servizio)
        self.vista_modificaservizio.show()
        self.close()
    
