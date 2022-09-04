from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from models.Utente import Utente
from views.VistaModificaUtente import VistaModificaUtente

class VistaUtente(QtWidgets.QMainWindow):
    def __init__(self, parent, utente):
        # Costruttore 'VistaUtente'
        # :param parent: Vista che ha richiesto l'utilizzo di questa vista, posso utilizzare i metodi di parent
        # :param utente: Utente dal quale visualizzare le informazioni
        super(VistaUtente, self).__init__(parent)  # Call the inherited classes __init__ method
        uic.loadUi('gui/visualizza_utente.ui', self)  # Load the .ui file
        self.utente=utente
        self.parent=parent
        self.id_label.setText(str(utente.get_id()))
        self.username_label.setText(utente.get_username())
        permessi=utente.get_permessi()
        self.operatori_check.setChecked(True if permessi[0]==1 else False)
        self.mezzi_check.setChecked(True if permessi[1]==1 else False)
        self.servizi_check.setChecked(True if permessi[2]==1 else False)
        self.turni_check.setChecked(True if permessi[3]==1 else False)
        self.clienti_check.setChecked(True if permessi[4]==1 else False)
        self.utenti_check.setChecked(True if permessi[5]==1 else False)
        self.indietro_button.clicked.connect(self.close)
        self.modifica_button.clicked.connect(self.go_modifica)

    def go_modifica(self):
        # Metodo per passare alla vista di modifica
        self.vista_modificautente = VistaModificaUtente(self.parent, self.utente)
        self.vista_modificautente.show()
        self.close()
