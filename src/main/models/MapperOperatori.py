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
        return operatori

    def get_operatore(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for row in cur.execute("SELECT * FROM Operatori WHERE id=" + id):
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[4], row[5])   
            return operatore
        return None
    
    def ricerca_operatori(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        operatori  = []
        for row in cur.execute("SELECT * FROM Operatori WHERE id LIKE '%" + text + "%' OR nome LIKE '%" + text +  "%' OR cognome LIKE '%" + text + "%'"):
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[4], row[5])   
            operatori.append(operatore)
        return operatori



    def insert_operatore(self, operatore):
        operatore = 'ciao'

    def update_operatore(self, id, operatore):
        operatore=id
