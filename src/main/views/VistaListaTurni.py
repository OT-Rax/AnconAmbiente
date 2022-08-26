from PyQt5 import QtWidgets, uic, QtCore 
import sys
import xz_rc

from views.VistaInserimentoTurno import VistaInserimentoTurno
from views.VistaModificaTurno import VistaModificaTurno
from views.VistaTurno import VistaTurno
from controllers.ControlloreTurni import ControlloreTurni

class VistaListaTurni(QtWidgets.QMainWindow):
    controller = ControlloreTurni()

    def __init__(self):
        super(VistaListaTurni, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/turni.ui', self)  # Load the .ui file
        self.inserisci_button.clicked.connect(self.go_inserisci)
        self.modifica_button.clicked.connect(self.go_modifica)
        self.visualizza_button.clicked.connect(self.go_visualizza)
        self.elimina_button.clicked.connect(self.go_elimina)
        self.indietro_button.clicked.connect(self.close)

    def go_inserisci(self):
        self.vista_inserimentoturno = VistaInserimentoTurno()
        self.vista_inserimentoturno.show()

    def go_modifica(self):
        self.vista_modificaturno = VistaModificaTurno()
        self.vista_modificaturno.show()

    def go_visualizza(self):
        turni = self.get_turni_selezionati()
        for turno in turni:   
            self.vista_turno = VistaTurno(self,turno)
            self.vista_turno.show()

    def go_elimina(self):
        turni=self.get_turni_selezionati()
        if len(turni) !=0:
            popup=QtWidgets.QDialog()
            uic.loadUi('gui/dialog_elimina.ui', popup)
            if len(turni) == 1:
                popup.label_3.setText("Vuoi davvero eliminare questo turno?")
            else:
                popup.label_3.setText("Vuoi davvero eliminare " + str(len(turni)) + " turni?")
            popup.buttonBox.accepted.connect(self.elimina)
            popup.exec()
            self.update()

    def get_turni_selezionati(self):
        caselle_selezionate=self.tabella_turni.selectedItems()
        turni=[]
        if len(caselle_selezionate) == 0:
            self.warning_label.setText("Seleziona almeno un turno.")
        else:
            self.warning_label.setText("")
            righe_selezionate=[]
            for casella in caselle_selezionate:
                righe_selezionate.append(casella.row())
            for riga in set(righe_selezionate):
                turno=self.controller.get_turno(int(self.tabella_turni.item(riga, 0).text()))
                turni.append(turno)
        return turni

    def inserisci_tabella(self, turni):
        row = self.tabella_turni.rowCount()
        for turno in turni:
            items = []
            items.append(QtWidgets.QTableWidgetItem(str(turno.get_id())))
            items.append(QtWidgets.QTableWidgetItem(turno.get_servizio()))
            items.append(QtWidgets.QTableWidgetItem(turno.get_data()))
            mezzo = turno.get_mezzo()
            items.append(QtWidgets.QTableWidgetItem(mezzo.get_id_mezzo))
            operatore = turno.get_operatore()
            items.append(QtWidgets.QTableWidgetItem(operatore.get_id()))
            self.tabella_operatori.insertRow(row)
            column=0
            for item in items:
                item.setFlags(item.flags() &~ QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tabella_turni.setItem(row, column, item) 
                column+=1
            row+=1
        self.ordina_tabella()

class DialogElimina(QtWidgets.QDialog):
    def __init__(self):
        super(DialogElimina, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/dialog_elimina.ui', self)  # Load the .ui file
