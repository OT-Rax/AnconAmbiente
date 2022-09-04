import os
import sqlite3

from models.Mezzo import Mezzo

class MapperMezzi:
    def __init__(self):
        dirname = os.path.dirname(__file__)
        db_file = os.path.join(dirname, '../db/AAdb')
        self.db_directory = db_file

    #Metodo che restituisce tutti i mezzi presenti nel DB
    def get_mezzi(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        mezzi  = []
        for row in cur.execute("SELECT * FROM Mezzi"):
            mezzo = Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
            mezzi.append(mezzo)
        con.close()
        return mezzi

    #Metodo che restituisce tutti i mezzi che sono disponibili tra le date e gli orari dati in input
    # :param inizio_turno: oggetto contenente data ed ora dell'inizio del turno
    # :param fine_turno: oggetto contenente data ed ora della fine del turno
    def get_mezzi_disponibili(self, inizio_turno, fine_turno):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        mezzi  = []
        for row in cur.execute("SELECT * FROM Mezzi AS M WHERE M.stato=0 \
                                EXCEPT \
                                SELECT M.* FROM (MEZZI AS M JOIN ASSEGNAMENTI AS A ON M.id=A.id_mezzo) JOIN TURNI AS T ON A.id_turno = T.id \
                                WHERE (T.data_inizio > ? AND T.data_inizio < ?)\
                                OR (T.data_fine > ? AND T.data_fine < ?)\
                                OR (T.data_inizio < ? AND T.data_fine > ?)", (inizio_turno, fine_turno, inizio_turno, fine_turno, inizio_turno, fine_turno)):
            mezzo = Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
            mezzi.append(mezzo)
        con.close()
        return mezzi


    def get_mezzi_disponibili_modifica(self, inizio_turno, fine_turno, id_turno):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        mezzi  = []
        for row in cur.execute("SELECT * FROM Mezzi AS M WHERE M.stato=0 \
                                EXCEPT \
                                SELECT M.* FROM (MEZZI AS M JOIN ASSEGNAMENTI AS A ON M.id=A.id_mezzo) JOIN TURNI AS T ON A.id_turno = T.id \
                                WHERE T.id!=? AND ((T.data_inizio > ? AND T.data_inizio < ?)\
                                OR (T.data_fine > ? AND T.data_fine < ?)\
                                OR (T.data_inizio < ? AND T.data_fine > ?))", (id_turno, inizio_turno, fine_turno, inizio_turno, fine_turno, inizio_turno, fine_turno)):
            mezzo = Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
            mezzi.append(mezzo)
        con.close()
        return mezzi


    #Metodo che restituisce un mezzo attraverso l'id dato in input
    # :param id: oggetto contenente l'id del mezzo da prelevare
    def get_mezzo(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        mezzo=None
        for row in cur.execute("SELECT * FROM Mezzi WHERE id="+str(id)):
            mezzo = Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
        con.close()
        return mezzo

    #Metodo che restituisce un oggetto popolato dai mezzi che hanno in comune l'id o il tipo o l'allestimento dato in input
    # :param text: oggetto contenente la stringa di caratteri per la ricerca di determinati mezzi
    def ricerca_mezzi(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        mezzi  = []
        for row in cur.execute('SELECT * FROM Mezzi WHERE id LIKE ? OR tipo LIKE ? OR allestimento LIKE ?', ("%"+text+"%", "%"+text+"%","%"+text+"%")):
            mezzo = Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
            mezzi.append(mezzo)
        con.close()
        return mezzi

    #Metodo che inserisce un Mezzo nel DB
    # :param targa: targa del Mezzo
    # :param tipo: che tipo di mezzo e' (es. auto, camion,...)
    # :param allestimento: allestimento del mezzo
    # :param iscrizione_albo: oggetto contenente la data di iscrizione all'albo del mezzo
    # :param patente: patente necessaria per guidare il mezzo
    # :param stato: stato di disponibilita' del mezzo
    def insert_mezzo(self, targa, tipo, allestimento, iscrizione_albo, patente, stato):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Mezzi (targa, tipo, allestimento, iscrizione_albo, patente, stato) VALUES (?, ?, ?, ?, ?, ?)", (targa, tipo, allestimento, iscrizione_albo, patente, stato))
        con.commit()
        con.close()

    #Metodo per l'aggiornamento di un mezzo nel DB a seguito di una modifica
    # :param id: id del mezzo da modificare
    # :param mezzo: Oggetto Mezzo contenente i nuovi dati da inserire nel DB 
    def update_mezzo(self, id, mezzo):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("UPDATE Mezzi SET targa=?, tipo=?, allestimento=?, iscrizione_albo=?, patente=?, stato=? WHERE id=?",
                (mezzo.get_targa_mezzo(), mezzo.get_tipo_mezzo(), mezzo.get_allestimento_mezzo(), mezzo.get_iscrizione_mezzo(), mezzo.get_patente_mezzo(), mezzo.get_stato_mezzo(), id))
        con.commit()
        con.close()

    #Metodo che elimina i mezzi, passati in input, dal DB
    # :param mezzi: Oggetto popolato dai mezzi da eliminare dal DB
    def elimina_mezzi(self, mezzi):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for mezzo in mezzi:
            print(str(mezzo.get_id_mezzo()))
            cur.execute("DELETE FROM Mezzi WHERE id="+str(mezzo.get_id_mezzo()))
        con.commit()
        con.close()
