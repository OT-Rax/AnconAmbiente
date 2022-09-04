import sqlite3

from models.Turno import Turno
from models.Mezzo import Mezzo
from models.Operatore import Operatore
from models.Servizio import Servizio

class MapperTurno:
    def __init__(self):
        self.db_directory="./db/AAdb"

    def get_turni(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turni = []
        operatori=[]
        mezzi=[]
        #ID, SERVIZIO, INIZIO, FINE, MEZZI, OPERATORI
        for turno in cur.execute("SELECT * FROM Turni"):
            for row in cur.execute("SELECT S.* FROM Servizi AS S JOIN Lavori AS L ON S.id=L.id_servizio"):
                servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            for row in cur.execute("SELECT O.* FROM Operatori AS O JOIN Impieghi AS I ON O.id=I.id_operatore"):
                operatori.append(Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            for row in cur.execute("SELECT M.* FROM Mezzi as M JOIN Assegnamenti AS A ON M.id=A.id_mezzo"):
                mezzi.append(Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))  
            turno = Turno(turno[0], servizio, turno[1], turno[2], mezzi, operatori)
            turni.append(turno)
        con.close()
        return turni

    def get_turno(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turno=None
        operatori=[]
        mezzi=[]
        for riga in cur.execute("SELECT * FROM Turni WHERE id="+str(id)):
            for row in cur.execute("SELECT S.* FROM Servizi AS S JOIN Lavori AS L ON S.id=L.id_servizio"):
                servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            for row in cur.execute("SELECT O.* FROM Operatori AS O JOIN Impieghi AS I ON O.id=I.id_operatore"):
                operatori.append(Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            for row in cur.execute("SELECT M.* FROM Mezzi as M JOIN Assegnamenti AS A ON M.id=A.id_mezzo"):
                mezzi.append(Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))  
            turno = Turno(riga[0], servizio, riga[1], riga[2], mezzi, operatori)
        con.close()
        return turno
    
    #per la ricerca turni viene selezionata solo la data
    def ricerca_turni(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turni  = []
        operatori=[]
        mezzi=[]
        for turno in cur.execute('SELECT * FROM Turni WHERE data LIKE ?', ("%"+text+"%")):
            for row in cur.execute("SELECT S.* FROM Servizi AS S JOIN Lavori AS L ON S.id=L.id_servizio"):
                servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            for row in cur.execute("SELECT O.* FROM Operatori AS O JOIN Impieghi AS I ON O.id=I.id_operatore"):
                operatori.append(Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            for row in cur.execute("SELECT M.* FROM Mezzi as M JOIN Assegnamenti AS A ON M.id=A.id_mezzo"):
                mezzi.append(Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))  
            turno = Turno(turno[0], servizio, turno[1], turno[2], mezzi, operatori)
            turni.append(turno)
        con.close()
        return turni

    def insert_turno(self, servizio, data_inizio, data_fine, mezzi, operatori):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Turni (data_inizio, data_fine) VALUES (?, ?)", (data_inizio, data_fine))
        id_turno=self.get_ultimo_id()
        cur.execute("INSERT INTO Lavori (id_servizio, id_turno) VALUES (?,?)", (servizio.get_id(), id_turno))
        for mezzo in mezzi:
            cur.execute("INSERT INTO Assegnamenti (id_mezzo, id_turno) VALUES (?,?)", (mezzo.get_id(), id_turno))
        for operatore in operatori:
            cur.execute("INSERT INTO Impieghi (id_operatore, id_turno) VALUES (?,?)", (operatore.get_id(), id_turno))
        con.commit()
        con.close()

    def update_turno(self, id, turno):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("UPDATE Turni SET servizio=?, data=?, ora_inizio=?, ora_fine=?, mezzo=?, operatore=? WHERE id=?", 
                (turno.get_servizio, turno.get_data, turno.get_ora_inizio, turno.get_ora_fine, turno.get_mezzo, turno.get_operatore, id))
        con.commit()
        con.close()

    def elimina_turni(self, turni):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for turno in turni:
            cur.execute("DELETE FROM Turni WHERE id="+str(turno.get_id()))
        con.commit()
        con.close()

    def get_ultimo_id(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for riga in cur.execute("SELECT MAX(id) FROM Turni"):
            id=riga[0]
        con.close()
        return id
