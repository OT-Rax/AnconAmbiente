import sqlite3

from models.Servizio import Servizio

class MapperServizi:
    def __init__(self):
        self.db_directory="./db/AAdb"

    def get_servizi(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        servizi  = []
        for row in cur.execute("SELECT * FROM Servizi"):
            servizio = Servizio(row[0], row[1], row[2], row[3], row[4])
            servizi.append(servizio)
        con.close()
        return servizi

    def get_servizio(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        servizio = None
        #Non ho usato bindings perche rotti
        for row in cur.execute("SELECT * FROM Servizi WHERE id="+str(id)):
            servizio = Servizio(row[0], row[1], row[2], row[3], row[4])
        con.close()
        return servizio

    def ricerca_servizi(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        servizi  = []
        for row in cur.execute('SELECT * FROM Servizi WHERE id LIKE ? OR tipo LIKE ? OR peridiocita LIKE ? OR id_cliente LIKE ?', ("%"+text+"%", "%"+text+"%","%"+text+"%", "%"+text+"%")):
            servizio = Servizio(row[0], row[1], row[2], row[3], row[4])
            servizi.append(servizio)
        con.close()
        return servizi

    def insert_servizio(self, id_cliente, tipo, luogo, periodicita):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Servizi (id_cliente, tipo, luogo, periodicita) VALUES (?, ?, ?);", (id_cliente, tipo, luogo, periodicita))
        con.commit()
        con.close()

    def update_servizio(self, id, servizio):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("UPDATE Servizi SET id_cliente=?, tipo=?, luogo=?, peridiocita=? WHERE id=?",
                (servizio.get_id_cliente(), servizio.get_tipo(), servizio.get_luogo(), servizio.get_periodicita(), id))
        con.commit()
        con.close()

    def elimina_servizi(self, servizi):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for servizio in servizi:
            print(str(servizio.get_id()))
            cur.execute("DELETE FROM Servizi WHERE id="+str(servizio.get_id()))
        con.commit()
        con.close()
