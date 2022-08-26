import sqlite3

from models.Turno import Turno

class MapperTurno:
    def __init__(self):
        self.db_directory="./db/AAdb"

    def get_Turni(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turni = []
        for row in cur.execute("SELECT * FROM Turni"):
            turno = Turno(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            turni.append(turno)
        con.close()
        return turni

    def get_turno(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turno=None
        for row in cur.execute("SELECT * FROM Turni WHERE id="+str(id)):
            turno = Turno(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) 
        con.close()
        return turno
    
    #per la ricerca turni viene selezionata solo la data
    def ricerca_turni(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turni  = []
        for row in cur.execute('SELECT * FROM Turni WHERE data LIKE ?', ("%"+text+"%")):
            turno = Turno(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
            turni.append(turno)
        con.close()
        return turni

    def insert_turno(self, servizio, data, ora_inizio, ora_fine, mezzo, operatore):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Turni (servizio, data, ora_inizio, ora_fine, mezzo, operatore) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (servizio, data, ora_inizio, ora_fine, mezzo, operatore))
        con.commit()
        con.close()

    def update_turno(self, id, turno):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("UPDATE Turni SET servizio=?, data=?, ora_inizio=?, ora_fine=?, mezzo=?, operatore=? WHERE id=?", (turno.get_servizio, turno.get_data, turno.get_ora_inizio, turno.get_ora_fine, turno.get_mezzo, turno.get_operatore, id))
        con.commit()
        con.close()

    def elimina_turni(self, turni):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for turno in turni:
            cur.execute("DELETE FROM Turni WHERE id="+str(turno.get_id()))
        con.commit()
        con.close()