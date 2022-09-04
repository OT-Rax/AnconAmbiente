import sys
import sqlite3
import os
from PyQt5.QtWidgets import QApplication

from views.VistaLogin import VistaLogin

if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    db_file = os.path.join(dirname, 'db/AAdb')
    con=sqlite3.connect(db_file)
    #cur = con.execute("query")
    con.commit()
    app = QApplication(sys.argv)
    vista_login = VistaLogin()
    vista_login.show()
    con.close()
    sys.exit(app.exec_())
