import sqlite3

from models.Mezzo import Mezzo

class MapperMezzi:
    def __init__(self):
        self.db_directory="./db/AAdb"

    def get_mezzi(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        mezzi  = []
        for row in cur.execute("SELECT * FROM Mezzi"):
            mezzo = Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
            mezzi.append(mezzo)
        con.close()
        return mezzi

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

    def get_mezzo(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        mezzo=None
        for row in cur.execute("SELECT * FROM Mezzi WHERE id="+str(id)):
            mezzo = Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
        con.close()
        return mezzo

    def ricerca_mezzi(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        mezzi  = []
        for row in cur.execute('SELECT * FROM Mezzi WHERE id LIKE ? OR tipo LIKE ? OR allestimento LIKE ?', ("%"+text+"%", "%"+text+"%","%"+text+"%")):
            mezzo = Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
            mezzi.append(mezzo)
        con.close()
        return mezzi

    def insert_operatore(self, targa, tipo, allestimento, iscrizione_albo, patente, stato):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Mezzi (targa, tipo, allestimento, iscrizione_albo, patente, stato) VALUES (?, ?, ?, ?, ?, ?)", (targa, tipo, allestimento, iscrizione_albo, patente, stato))
        con.commit()
        con.close()

    def update_mezzo(self, id, mezzo):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("UPDATE Mezzi SET targa=?, tipo=?, allestimento=?, iscrizione_albo=?, patente=?, stato=? WHERE id=?",
                (mezzo.get_targa_mezzo(), mezzo.get_tipo_mezzo(), mezzo.get_allestimento_mezzo(), mezzo.get_iscrizione_mezzo(), mezzo.get_patente_mezzo(), mezzo.get_stato_mezzo(), id))
        con.commit()
        con.close()

    def elimina_mezzi(self, mezzi):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for mezzo in mezzi:
            print(str(mezzo.get_id_mezzo()))
            cur.execute("DELETE FROM Mezzi WHERE id="+str(mezzo.get_id_mezzo()))
        con.commit()
        con.close()
