import sqlite3

class ControlloreReport:

    def __init__(self):
        # Costruttore
        self.db_directory="./db/AAdb"

    def mezzo_tipo(self):
        # Metodo per ottenere numero di mezzi per tipologia
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        righe = []
        for row in cur.execute("SELECT tipo, COUNT(id) FROM Mezzi GROUP BY tipo"):
            righe.append(row[0] +' '+ row[1])
        con.close()
        return righe

    def mezzo_all(self):
        # Metodo per ottenere numero di mezzi per allestimento
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        righe = []
        for row in cur.execute("SELECT allestimento, COUNT(id) FROM Mezzi GROUP BY tipo"):
            righe.append(row[0] +' '+ row[1])
        con.close()
        return righe

    def get_Operatori(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        id = []
        for row in cur.execute("SELECT id FROM Operatori"):
            id.append(row)
        con.close()
        return id

    def get_Mezzi(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        id = []
        for row in cur.execute("SELECT id FROM Mezzi"):
            id.append(row)
        con.close()
        return id

