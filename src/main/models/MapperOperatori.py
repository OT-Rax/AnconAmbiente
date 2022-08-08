import sqlite3

from models.Operatore import Operatore

class MapperOperatori:
    def __init__(self):
        self.db_directory="./db/AAdb"

    def get_operatori(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        operatori  = []
        for row in cur.execute("SELECT * FROM Operatori"):
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[4], row[5])   
            operatori.append(operatore)
        con.close()
        return operatori

    def get_operatore(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for row in cur.execute("SELECT * FROM Operatori WHERE id=?", (id)):
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[4], row[5])   
            return operatore
        con.close()
        return None
    
    def ricerca_operatori(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        operatori  = []
        for row in cur.execute('SELECT * FROM Operatori WHERE id LIKE ? OR nome LIKE ? OR cognome LIKE ?', ("%"+text+"%", "%"+text+"%","%"+text+"%")):
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[4], row[5])   
            operatori.append(operatore)
        con.close()
        return operatori

    def insert_operatore(self, nome, cognome, cf, data_nascita, patenti, data_fine_contratto):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Operatori VALUES(?, ?, ?, ?, ?, ?)", ("ciaopa", nome, cognome, "datadinascitaformattata", cf, 0))
        con.commit()
        con.close()


    def update_operatore(self, id, operatore):
        operatore=id
