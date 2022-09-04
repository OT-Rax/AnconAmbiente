import sqlite3

from PyQt5 import QtCore
from models.Servizio import Servizio

class MapperServizi:
    def __init__(self):
        self.db_directory="./db/AAdb"

    def get_servizi(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        servizi  = []
        for row in cur.execute("SELECT * FROM Servizi"):
            servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            servizi.append(servizio)
        con.close()
        return servizi

    def get_servizi_inseribili(self, data):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        servizi  = []
        for row in cur.execute("SELECT * FROM Servizi WHERE data_fine>=?", (data.date().toString("yyyy-MM-dd"),)):
            servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            servizi.append(servizio)
        con.close()
        return servizi

    def get_servizi_da_inserire(self, data):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        servizi  = []
        print(data.date().toString("yyyy-MM-dd"))
        for row in cur.execute("SELECT S.id, S.id_cliente, S.tipo, S.luogo, S.data_inizio, S.data_fine, S.ripetizione, S.periodicita, COUNT(ALL) \
                                FROM (Servizi AS S LEFT JOIN Lavori AS L ON S.id = L.id_servizio) LEFT JOIN Turni as T ON L.id_turno=T.id\
                                WHERE S.data_fine>=? AND ((periodicita IS NULL) \
                                OR (periodicita='Giornaliero' AND ((T.data_inizio > ? AND T.data_inizio < ?) OR (T.data_fine > ? AND T.data_fine < ?) OR (T.data_inizio < ? AND T.data_fine > ?) \
                                OR (T.data_inizio IS NULL AND T.data_fine IS NULL))) \
                                OR (periodicita='Settimanale' AND ((T.data_inizio > ? AND T.data_inizio < ?) OR (T.data_fine > ? AND T.data_fine < ?) OR (T.data_inizio < ? AND T.data_fine > ?) \
                                OR (T.data_inizio IS NULL AND T.data_fine IS NULL))) \
                                OR (periodicita='Mensile' AND ((T.data_inizio > ? AND T.data_inizio < ?) OR (T.data_fine > ? AND T.data_fine < ?) OR (T.data_inizio < ? AND T.data_fine > ?) \
                                OR (T.data_inizio IS NULL AND T.data_fine IS NULL))) \
                                OR (periodicita='Annuale' AND ((T.data_inizio > ? AND T.data_inizio < ?) OR (T.data_fine > ? AND T.data_fine < ?) OR (T.data_inizio < ? AND T.data_fine > ?) \
                                OR (T.data_inizio IS NULL AND T.data_fine IS NULL)))) \
                                GROUP BY S.id, S.id_cliente, S.tipo, S.luogo, S.data_inizio, S.data_fine, S.ripetizione, S.periodicita \
                                HAVING COUNT(*)<S.ripetizione"\
                                ,
                                (data.date().toString("yyyy-MM-dd"), \
                                data.date().toString("yyyy-MM-dd"), data.date().addDays(1).toString("yyyy-MM-dd"), \
                                data.date().toString("yyyy-MM-dd"), data.date().addDays(1).toString("yyyy-MM-dd"), \
                                data.date().toString("yyyy-MM-dd"), data.date().addDays(1).toString("yyyy-MM-dd"), \
                                data.date().addDays(-3).toString("yyyy-MM-dd"), data.date().addDays(4).toString("yyyy-MM-dd hh:mm"), \
                                data.date().addDays(-3).toString("yyyy-MM-dd"), data.date().addDays(4).toString("yyyy-MM-dd hh:mm"), \
                                data.date().addDays(-3).toString("yyyy-MM-dd"), data.date().addDays(4).toString("yyyy-MM-dd hh:mm"), \
                                data.date().toString("yyyy-MM"), data.date().addMonths(1).toString("yyyy-MM"), \
                                data.date().toString("yyyy-MM"), data.date().addMonths(1).toString("yyyy-MM"), \
                                data.date().toString("yyyy-MM"), data.date().addMonths(1).toString("yyyy-MM"), \
                                data.date().toString("yyyy"), data.date().addYears(1).toString("yyyy"), \
                                data.date().toString("yyyy"), data.date().addYears(1).toString("yyyy"), \
                                data.date().toString("yyyy"), data.date().addYears(1).toString("yyyy"), \
                                )):
            servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            servizi.append(servizio)
        con.close()
        return servizi

    def get_servizio(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        servizio = None
        #Non ho usato bindings perche rotti
        for row in cur.execute("SELECT * FROM Servizi WHERE id="+str(id)):
            servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        con.close()
        return servizio

    def ricerca_servizi(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        servizi  = []
        for row in cur.execute('SELECT * FROM Servizi WHERE id LIKE ? OR tipo LIKE ? OR luogo LIKE? OR periodicita LIKE ? OR id_cliente LIKE ?', ("%"+text+"%", "%"+text+"%", "%"+text+"%","%"+text+"%", "%"+text+"%")):
            servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            servizi.append(servizio)
        con.close()
        return servizi

    def insert_servizio(self, id_cliente, tipo, luogo, data_inizo, data_fine, ripetizione, periodicita):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Servizi (id_cliente, tipo, luogo, data_inizio, data_fine, ripetizione, periodicita) VALUES (?, ?, ?, ?, ?, ?, ?);", (id_cliente, tipo, luogo, data_inizo, data_fine, ripetizione, periodicita))
        con.commit()
        con.close()

    def update_servizio(self, id, servizio):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("UPDATE Servizi SET id_cliente=?, tipo=?, luogo=?, data_inizio=?, data_fine=?, ripetizione=?, periodicita=? WHERE id=?",
            (servizio.get_id_cliente(),
            servizio.get_tipo(),
            servizio.get_luogo(),
            servizio.get_datainizio(),
            servizio.get_datafine(),
            servizio.get_ripetizione(),
            servizio.get_periodicita(),
            id))
        con.commit()
        con.close()

    def elimina_servizi(self, servizi):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for servizio in servizi:
            cur.execute("DELETE FROM Servizi WHERE id="+str(servizio.get_id()))
        con.commit()
        con.close()
