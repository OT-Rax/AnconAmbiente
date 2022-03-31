import sys
import sqlite3
from PyQt5.QtWidgets import QApplication

from views.VistaLogin import VistaLogin

if __name__ == '__main__':
    con=sqlite3.connect('db/AAdb')
    #cur = con.execute("query")
    con.commit()
    app = QApplication(sys.argv)
    vista_login = VistaLogin()
    vista_login.show()
    con.close()
    sys.exit(app.exec_())
