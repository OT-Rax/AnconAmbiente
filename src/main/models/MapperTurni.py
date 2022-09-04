import os
import sqlite3

from models.Turno import Turno
from models.Mezzo import Mezzo
from models.Operatore import Operatore
from models.Servizio import Servizio

class MapperTurni:
    def __init__(self):
        dirname = os.path.dirname(__file__)
        db_file = os.path.join(dirname, '../db/AAdb')
        self.db_directory = db_file

    def get_turni(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turni = []
        #ID, SERVIZIO, INIZIO, FINE, MEZZI, OPERATORI
        for riga in cur.execute("SELECT * FROM Turni").fetchall():
            servizio=None
            operatori = []
            mezzi= []
            for row in cur.execute("SELECT S.* FROM Servizi AS S JOIN Lavori AS L ON S.id=L.id_servizio WHERE L.id_turno="+str(riga[0])):
                servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            for row in cur.execute("SELECT O.* FROM Operatori AS O JOIN Impieghi AS I ON O.id=I.id_operatore WHERE I.id_turno="+str(riga[0])):
                operatori.append(Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            for row in cur.execute("SELECT M.* FROM Mezzi as M JOIN Assegnamenti AS A ON M.id=A.id_mezzo WHERE A.id_turno="+str(riga[0])):
                mezzi.append(Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))  
            turni.append(Turno(riga[0], servizio, riga[1], riga[2], mezzi, operatori))
        con.close()
        return turni

    
    def get_turni_operatore(self, id_operatore, data_inizio, data_fine):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turni = []
        #ID, SERVIZIO, INIZIO, FINE, MEZZI, OPERATORI
        for riga in cur.execute("SELECT * FROM Turni AS T INNER JOIN Impieghi AS I on T.id=I.id_turno WHERE I.id_operatore=? AND T.data_fine BETWEEN ? AND ?", (id_operatore,data_inizio,data_fine)).fetchall():
            servizio=None
            operatori = []
            mezzi= []
            for row in cur.execute("SELECT S.* FROM Servizi AS S JOIN Lavori AS L ON S.id=L.id_servizio WHERE L.id_turno="+str(riga[0])):
                servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            for row in cur.execute("SELECT O.* FROM Operatori AS O JOIN Impieghi AS I ON O.id=I.id_operatore WHERE I.id_turno="+str(riga[0])):
                operatori.append(Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            for row in cur.execute("SELECT M.* FROM Mezzi as M JOIN Assegnamenti AS A ON M.id=A.id_mezzo WHERE A.id_turno="+str(riga[0])):
                mezzi.append(Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))  
            turni.append(Turno(riga[0], servizio, riga[1], riga[2], mezzi, operatori))
        con.close()
        return turni
    def get_turni_mezzo(self, id_mezzo, data_inizio, data_fine):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turni = []
        #ID, SERVIZIO, INIZIO, FINE, MEZZI, OPERATORI
        for riga in cur.execute("SELECT * FROM Turni AS T INNER JOIN Assegnamenti AS A on T.id=A.id_turno WHERE A.id_mezzo=? AND T.data_fine BETWEEN ? AND ?", (id_mezzo,data_inizio,data_fine)).fetchall():
            servizio=None
            operatori = []
            mezzi= []
            for row in cur.execute("SELECT S.* FROM Servizi AS S JOIN Lavori AS L ON S.id=L.id_servizio WHERE L.id_turno="+str(riga[0])):
                servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            for row in cur.execute("SELECT O.* FROM Operatori AS O JOIN Impieghi AS I ON O.id=I.id_operatore WHERE I.id_turno="+str(riga[0])):
                operatori.append(Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            for row in cur.execute("SELECT M.* FROM Mezzi as M JOIN Assegnamenti AS A ON M.id=A.id_mezzo WHERE A.id_turno="+str(riga[0])):
                mezzi.append(Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))  
            turni.append(Turno(riga[0], servizio, riga[1], riga[2], mezzi, operatori))
        con.close()
        return turni

    def get_turni_servizio(self, id_servizio, data_inizio, data_fine):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turni = []
        #ID, SERVIZIO, INIZIO, FINE, MEZZI, OPERATORI
        for riga in cur.execute("SELECT * FROM Turni AS T INNER JOIN Lavori AS L on T.id=L.id_turno WHERE L.id_servizio=? AND T.data_fine BETWEEN ? AND ?", (id_servizio,data_inizio,data_fine)).fetchall():
            servizio=None
            operatori = []
            servizi= []
            for row in cur.execute("SELECT S.* FROM Servizi AS S JOIN Lavori AS L ON S.id=L.id_servizio WHERE L.id_turno="+str(riga[0])):
                servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            for row in cur.execute("SELECT O.* FROM Operatori AS O JOIN Impieghi AS I ON O.id=I.id_operatore WHERE I.id_turno="+str(riga[0])):
                operatori.append(Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            for row in cur.execute("SELECT M.* FROM Mezzi as M JOIN Assegnamenti AS A ON M.id=A.id_mezzo WHERE A.id_turno="+str(riga[0])):
                servizi.append(Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))  
            turni.append(Turno(riga[0], servizio, riga[1], riga[2], servizi, operatori))
        con.close()
        return turni


    def get_turni_cliente(self, id_cliente, data_inizio, data_fine):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turni = []
        #ID, SERVIZIO, INIZIO, FINE, MEZZI, OPERATORI
        for riga in cur.execute("SELECT * FROM (Turni AS T INNER JOIN Lavori AS L on T.id=L.id_turno) INNER JOIN Servizi AS S ON L.id_servizio=S.id \
                WHERE S.id_cliente=? AND T.data_fine BETWEEN ? AND ?", (id_cliente,data_inizio,data_fine)).fetchall():
            servizio=None
            operatori = []
            servizi= []
            for row in cur.execute("SELECT S.* FROM Servizi AS S JOIN Lavori AS L ON S.id=L.id_servizio WHERE L.id_turno="+str(riga[0])):
                servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            for row in cur.execute("SELECT O.* FROM Operatori AS O JOIN Impieghi AS I ON O.id=I.id_operatore WHERE I.id_turno="+str(riga[0])):
                operatori.append(Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            for row in cur.execute("SELECT M.* FROM Mezzi as M JOIN Assegnamenti AS A ON M.id=A.id_mezzo WHERE A.id_turno="+str(riga[0])):
                servizi.append(Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))  
            turni.append(Turno(riga[0], servizio, riga[1], riga[2], servizi, operatori))
        con.close()
        return turni

    def get_turno(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turno=None
        operatori=[]
        mezzi=[]
        for riga in cur.execute("SELECT * FROM Turni WHERE id="+str(id)):
            for row in cur.execute("SELECT S.* FROM Servizi AS S JOIN Lavori AS L ON S.id=L.id_servizio WHERE L.id_turno="+str(riga[0])):
                servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            for row in cur.execute("SELECT O.* FROM Operatori AS O JOIN Impieghi AS I ON O.id=I.id_operatore WHERE I.id_turno="+str(riga[0])):
                operatori.append(Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            for row in cur.execute("SELECT M.* FROM Mezzi as M JOIN Assegnamenti AS A ON M.id=A.id_mezzo WHERE A.id_turno="+str(riga[0])):
                mezzi.append(Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))  
            turno = Turno(riga[0], servizio, riga[1], riga[2], mezzi, operatori)
        con.close()
        return turno
    
    #per la ricerca turni viene selezionata solo la data
    def filtra_turni(self, da_data, a_data):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turni = []
        #ID, SERVIZIO, INIZIO, FINE, MEZZI, OPERATORI
        for riga in cur.execute("SELECT * FROM Turni WHERE data_inizio BETWEEN ? AND ? OR data_fine BETWEEN ? AND ?", (da_data, a_data, da_data, a_data)).fetchall():
            servizio=None
            operatori = []
            mezzi= []
            for row in cur.execute("SELECT S.* FROM Servizi AS S JOIN Lavori AS L ON S.id=L.id_servizio WHERE L.id_turno="+str(riga[0])):
                servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            for row in cur.execute("SELECT O.* FROM Operatori AS O JOIN Impieghi AS I ON O.id=I.id_operatore WHERE I.id_turno="+str(riga[0])):
                operatori.append(Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            for row in cur.execute("SELECT M.* FROM Mezzi as M JOIN Assegnamenti AS A ON M.id=A.id_mezzo WHERE A.id_turno="+str(riga[0])):
                mezzi.append(Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))  
            turni.append(Turno(riga[0], servizio, riga[1], riga[2], mezzi, operatori))
        con.close()
        return turni

    def insert_turno(self, id_servizio, data_inizio, data_fine, id_mezzi, id_operatori):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Turni (data_inizio, data_fine) VALUES (?, ?)", (data_inizio, data_fine))
        con.commit()
        id_turno=self.get_ultimo_id()
        cur.execute("INSERT INTO Lavori (id_servizio, id_turno) VALUES (?,?)", (id_servizio, id_turno))
        for id_mezzo in id_mezzi:
            cur.execute("INSERT INTO Assegnamenti (id_mezzo, id_turno) VALUES (?,?)", (id_mezzo, id_turno))
        for id_operatore in id_operatori:
            cur.execute("INSERT INTO Impieghi (id_operatore, id_turno) VALUES (?,?)", (id_operatore, id_turno))
        con.commit()
        con.close()

    def update_turno(self, id, turno):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        turno_old = self.get_turno(id)
        for operatore in turno_old.get_operatori():
            cur.execute("DELETE FROM Impieghi WHERE id_turno="+str(id)+" AND id_operatore="+str(operatore.get_id()))
        for mezzo in turno_old.get_mezzi():
            cur.execute("DELETE FROM Assegnamenti WHERE id_turno="+str(id)+" AND id_mezzo="+str(mezzo.get_id_mezzo()))
        cur.execute("DELETE FROM Lavori WHERE id_turno="+str(id)+" AND id_servizio="+str(turno_old.get_servizio().get_id()))
        cur.execute("UPDATE Turni SET data_inizio=?, data_fine=? WHERE id=?", 
                (turno.get_data_inizio(), turno.get_data_fine(), id))
        for mezzo in turno.get_mezzi():
            cur.execute("INSERT INTO Assegnamenti (id_mezzo, id_turno) VALUES (?,?)", (mezzo.get_id_mezzo(), id))
        for operatore in turno.get_operatori():
            cur.execute("INSERT INTO Impieghi (id_operatore, id_turno) VALUES (?,?)", (operatore.get_id(), id))
        cur.execute("INSERT INTO Lavori (id_servizio, id_turno) VALUES (?,?)", (turno.get_servizio().get_id(), id))
        con.commit()
        con.close()

    def elimina_turni(self, turni):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for turno in turni:
            cur.execute("DELETE FROM Turni WHERE id="+str(turno.get_id()))
            cur.execute("DELETE FROM Assegnamenti WHERE id_turno="+str(turno.get_id()))
            cur.execute("DELETE FROM Impieghi WHERE id_turno="+str(turno.get_id()))
            cur.execute("DELETE FROM Lavori WHERE id_turno="+str(turno.get_id()))
        con.commit()
        con.close()

    def get_ultimo_id(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for riga in cur.execute("SELECT MAX(id) FROM Turni"):
            id=riga[0]
        con.close()
        return id
