from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from operatori.view.VistaListaOperatori import  VistaListaOperatori

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/home.ui', self)  # Load the .ui file
        self.show()  # Show the GUI
        self.operatori_button.clicked.connect(self.go_lista_operatori())

    def go_lista_operatori(self):
        self.vista_lista_operatori = VistaListaOperatori()
        self.vista_lista_operatori.show()

app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
window = Ui()  # Create an instance of our class
app.exec_()  # Start the application