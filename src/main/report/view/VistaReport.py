from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaReport(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaReport, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/report.ui', self)  # Load the .ui file
