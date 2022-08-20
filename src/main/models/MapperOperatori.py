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
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
            operatori.append(operatore)
        con.close()
        return operatori

    def get_operatore(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        operatore=None
        #Non ho usato bindings perche rotti
        for row in cur.execute("SELECT * FROM Operatori WHERE id="+str(id)):
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
        con.close()
        return operatore
    
    def ricerca_operatori(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        operatori  = []
        for row in cur.execute('SELECT * FROM Operatori WHERE id LIKE ? OR nome LIKE ? OR cognome LIKE ?', ("%"+text+"%", "%"+text+"%","%"+text+"%")):
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
            operatori.append(operatore)
        con.close()
        return operatori

    def insert_operatore(self, nome, cognome, data_nascita, cf, patenti, data_fine_contratto, stato):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Operatori (nome, cognome, data_nascita, cf, data_fine_contratto, stato) VALUES (?, ?, ?, ?, ?, ?)", (nome, cognome, data_nascita, cf, data_fine_contratto, stato))
        con.commit()
        con.close()


    def update_operatore(self, id, operatore):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("UPDATE Operatori SET nome=?, cognome=?, data_nascita=?, cf=?, data_fine_contratto=?, stato=? WHERE id=?",
                (operatore.get_nome(), operatore.get_cognome(), operatore.get_datanascita(), operatore.get_cf(), operatore.get_datacontratto(), operatore.get_stato(), id))
        con.commit()
        con.close()

    def elimina_operatori(self, operatori):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for operatore in operatori:
            print(str(operatore.get_id()))
            cur.execute("DELETE FROM Operatori WHERE id="+str(operatore.get_id()))
        con.commit()
        con.close()
