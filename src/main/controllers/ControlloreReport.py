import sqlite3

class ControlloreReport:

    def __init__(self):
        # Costruttore
        self.db_directory="./db/AAdb"

    def mezzo_tipo(self):
        # Metodo per ottenere numero di mezzi per tipologia
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        righe = []
        for row in cur.execute("SELECT tipo, COUNT(id) FROM Mezzi GROUP BY tipo"):
            righe.append(row[0] +' '+ str(row[1]))
        con.close()
        return righe

    def mezzo_all(self):
        # Metodo per ottenere numero di mezzi per allestimento
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        righe = []
        for row in cur.execute("SELECT allestimento, COUNT(id) FROM Mezzi GROUP BY tipo"):
            righe.append(row[0] +' '+ str(row[1]))
        con.close()
        return righe

    def get_Operatori(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        id = []
        for row in cur.execute("SELECT id FROM Operatori"):
            id.append(str(row[0]))
        con.close()
        return id

    def get_Mezzi(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        id = []
        for row in cur.execute("SELECT id FROM Mezzi"):
            id.append(str(row[0]))
        con.close()
        return id

    def get_Clienti(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        id = []
        for row in cur.execute("SELECT id FROM Clienti"):
            id.append(str(row[0]))
        con.close()
        return id

    def s_cli(self,id, data1, data2):
        #
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        righe = []
        for row in cur.execute("SELECT COUNT(*) FROM Servizi AS S WHERE S.id_cliente=? AND S.data_fine BETWEEN ? AND ?", (id, data1, data2)):
            righe.append(str(row[0]))
        con.close()
        return righe

    def s_ser(self, data1, data2):
        #
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        righe = []
        for row in cur.execute("SELECT Servizi.id, COUNT(ALL) FROM (Servizi JOIN Lavori ON Servizi.id = Lavori.id_servizio) JOIN Turni ON Lavori.id_turno=Turni.id WHERE Turni.data_fine BETWEEN ? AND ? GROUP BY Servizi.id", (data1, data2)):
            righe.append(str(row[0]) + ' ' + str(row[1]))
        con.close()
        return righe


    def turni_operatore(self, id, d1, d2):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        righe = []
        for row in cur.execute(
                "SELECT Turni.id FROM Turni JOIN Impieghi ON Turni.id = Impieghi.id_turno WHERE Impieghi.id_operatore=? AND Turni.data_fine BETWEEN ? AND ?", (id, d1, d2)):
            righe.append(str(row[0]))
        con.close()
        return righe
    def turni_mezzo(self, id, d1, d2):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        righe = []
        for row in cur.execute(
                "SELECT Turni.id FROM Turni JOIN Assegnamenti ON Turni.id = Assegnamenti.id_turno WHERE Assegnamenti.id_mezzo=? AND T.data_fine BETWEEN ? AND ?",
                (id, d1, d2)):
            righe.append(str(row[0]))
        con.close()
        return righe
