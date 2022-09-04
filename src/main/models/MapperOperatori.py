import os
import sqlite3

from models.Operatore import Operatore

class MapperOperatori:
    def __init__(self):
        dirname = os.path.dirname(__file__)
        db_file = os.path.join(dirname, '../db/AAdb')
        self.db_directory = db_file

    #Metodo che restituisce tutti gli operatori presenti nel DataBase
    def get_operatori(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        operatori  = []
        for row in cur.execute("SELECT * FROM Operatori"):
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
            operatori.append(operatore)
        con.close()
        return operatori

    #Metodo che restituisce tutti gli operatori che sono disponibili tra le date e gli orari dati in input
    # :param inizio_turno: oggetto contenente data ed ora dell'inizio del turno
    # :param fine_turno: oggetto contenente data ed ora della fine del turno
    def get_operatori_disponibili(self, inizio_turno, fine_turno):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        operatori  = []
        for row in cur.execute("SELECT * FROM Operatori AS O \
                                WHERE O.stato=0 \
                                EXCEPT \
                                SELECT O.* FROM (OPERATORI AS O JOIN IMPIEGHI AS I ON O.id=I.id_operatore) JOIN TURNI AS T ON I.id_turno = T.id \
                                WHERE (T.data_inizio > ? AND T.data_inizio < ?)\
                                OR (T.data_fine > ? AND T.data_fine < ?)\
                                OR (T.data_inizio < ? AND T.data_fine > ?)", (inizio_turno, fine_turno, inizio_turno, fine_turno, inizio_turno, fine_turno)):
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
            operatori.append(operatore)
        con.close()
        return operatori


    def get_operatori_disponibili_modifica(self, inizio_turno, fine_turno, id_turno):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        operatori  = []
        for row in cur.execute("SELECT * FROM Operatori AS O \
                                WHERE O.stato=0 \
                                EXCEPT \
                                SELECT O.* FROM (OPERATORI AS O JOIN IMPIEGHI AS I ON O.id=I.id_operatore) JOIN TURNI AS T ON I.id_turno = T.id \
                                WHERE T.id!=? AND ((T.data_inizio > ? AND T.data_inizio < ?)\
                                OR (T.data_fine > ? AND T.data_fine < ?)\
                                OR (T.data_inizio < ? AND T.data_fine > ?))", (id_turno, inizio_turno, fine_turno, inizio_turno, fine_turno, inizio_turno, fine_turno)):
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
            operatori.append(operatore)
        con.close()
        return operatori

    #Metodo che restituisce un operatore attraverso l'id dato in input
    # :param id: oggetto contenente l'id dell'operatore da prelevare
    def get_operatore(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        operatore=None
        for row in cur.execute("SELECT * FROM Operatori WHERE id="+str(id)):
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
        con.close()
        return operatore
    
    #Metodo che restituisce un oggetto popolato dagli operatori che hanno in comune l'id o il nome o il cognome dato in input
    # :param text: oggetto contenente la stringa di caratteri per la ricerca di determinati operatori
    def ricerca_operatori(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        operatori  = []
        for row in cur.execute('SELECT * FROM Operatori WHERE id LIKE ? OR nome LIKE ? OR cognome LIKE ?', ("%"+text+"%", "%"+text+"%","%"+text+"%")):
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
            operatori.append(operatore)
        con.close()
        return operatori

    #Metodo che inserisce un Operatore nel DataBase
    # :param nome: nome dell'operatore
    # :param cognome: cognome dell'operatore
    # :param datanascita: data di nascita dell'operatore
    # :param cf: codice fiscale dell'operatore
    # :param patenti: patenti possedute dall'operatore 
    # :param data_fine_contratto: data di fine contratto dell'operatore
    # :param stato: stato che indica se l'operatore è disponibile, in malattia o in ferie
    def insert_operatore(self, nome, cognome, data_nascita, cf, patenti, data_fine_contratto, stato):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Operatori (nome, cognome, data_nascita, cf, data_fine_contratto, stato) VALUES (?, ?, ?, ?, ?, ?)", (nome, cognome, data_nascita, cf, data_fine_contratto, stato))
        con.commit()
        con.close()

    #Metodo che va ad aggiornare i dati modificati di un operatore
    # :param id: id dell'operatore da modificare
    # :param operatore: oggetto contenete i dati aggiornati delloperatore da inserire nel DataBase 
    def update_operatore(self, id, operatore):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("UPDATE Operatori SET nome=?, cognome=?, data_nascita=?, cf=?, data_fine_contratto=?, stato=? WHERE id=?",
                (operatore.get_nome(), operatore.get_cognome(), operatore.get_datanascita(), operatore.get_cf(), operatore.get_datacontratto(), operatore.get_stato(), id))
        con.commit()
        con.close()

    #Metodo per l'eliminazione degli operatori dal DataBase
    # :param operatori: oggetto contenente gli operatori che si vogliono eliminare dal DataBase
    def elimina_operatori(self, operatori):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for operatore in operatori:
            cur.execute("DELETE FROM Operatori WHERE id="+str(operatore.get_id()))
        con.commit()
        con.close()
