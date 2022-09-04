import sqlite3

from PyQt5 import QtCore
from models.Servizio import Servizio

class MapperServizi:
    def __init__(self):
        self.db_directory="./db/AAdb"

    #Metodo che restituisce tutti i servizi presenti nel DataBase
    def get_servizi(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        servizi  = []
        for row in cur.execute("SELECT * FROM Servizi"):
            servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            servizi.append(servizio)
        con.close()
        return servizi

    #Metodo che restituisce i servizi la cui data è maggiore uguale della data data in input
    # :param data: oggetto contenente la data con cui si vogliono filtrare i servizi
    def get_servizi_inseribili(self, data):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        servizi  = []
        for row in cur.execute("SELECT * FROM Servizi WHERE data_fine>=?", (data.date().toString("yyyy-MM-dd"),)):
            servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            servizi.append(servizio)
        con.close()
        return servizi

    #Metodo che restituisce unoggetto contenente tutti i servizi da eseguire nella data inserita in input a seconda delle ripetizioni e periodicià dei servizi
    # :param data: oggetto contenente la data con cui si vogliono filtrare i servizi
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

    #Metodo che restituisce un servizio con id corrispondente a quello dato in input
    # :param id: id del servizio che si vuole ottenere
    def get_servizio(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        servizio = None
        for row in cur.execute("SELECT * FROM Servizi WHERE id="+str(id)):
            servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        con.close()
        return servizio

    #Metodo che restituisce un oggetto popolato dai servizi che hanno in comune l'id o il tipo o il luogo o la periodicità o l'id del cliente dato in input
    # :param text: oggetto contenente la stringa di caratteri per la ricerca di determinati servizi
    def ricerca_servizi(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        servizi  = []
        for row in cur.execute('SELECT * FROM Servizi WHERE id LIKE ? OR tipo LIKE ? OR luogo LIKE? OR periodicita LIKE ? OR id_cliente LIKE ?', ("%"+text+"%", "%"+text+"%", "%"+text+"%","%"+text+"%", "%"+text+"%")):
            servizio = Servizio(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            servizi.append(servizio)
        con.close()
        return servizi

    #Metodo che inserisce un Servizio nel DataBase
    # :param id_cliente: id del cliente associato al servizio
    # :param tipo: tipo di servizio da svolgere
    # :param luogo: luogo in cui effettuare il servizio
    # :param data_inizio: data di inizio del contratto del servizio
    # :param data_fine: data di fine del contratto del servizio
    # :param ripetizione: numero di volte con cui ripetere il servizio
    # :param periodicita: con quale periodicità viene effettuato il servizio (giornaliera, settimanale, mensile, annuale)
    def insert_servizio(self, id_cliente, tipo, luogo, data_inizo, data_fine, ripetizione, periodicita):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Servizi (id_cliente, tipo, luogo, data_inizio, data_fine, ripetizione, periodicita) VALUES (?, ?, ?, ?, ?, ?, ?);", (id_cliente, tipo, luogo, data_inizo, data_fine, ripetizione, periodicita))
        con.commit()
        con.close()

    #Metodo che va ad aggiornare i dati modificati di un servizio
    # :param id: id del servizio da modificare
    # :param servizio: oggetto contenete i dati aggiornati del servizio da inserire nel DataBase 
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

    #Metodo per l'eliminazione dei servizi dal DataBase
    # :param servizi: oggetto contenente i servizi che si vogliono eliminare dal DataBase
    def elimina_servizi(self, servizi):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for servizio in servizi:
            cur.execute("DELETE FROM Servizi WHERE id="+str(servizio.get_id()))
        con.commit()
        con.close()
