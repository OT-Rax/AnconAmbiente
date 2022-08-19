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

    def get_mezzo(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        mezzo=None
        #Non ho usato bindings perche rotti
        for row in cur.execute("SELECT * FROM Mezzi WHERE id="+str(id)):
            mezzo = Mezzo(row[0], row[1], row[2], row[3], row[4], row[5], row[6])   
        con.close()
        return mezzo

    def insert_operatore(self, targa, patente, tipo, allestimento, iscrizione_albo, stato):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Mezzi (targa, patente, tipo, allestimento, iscrizione_albo, stato) VALUES (?, ?, ?, ?, ?, ?)", (targa, patente, tipo, allestimento, iscrizione_albo, stato))
        con.commit()
        con.close()

