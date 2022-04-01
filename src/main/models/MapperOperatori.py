import sqlite3

from models.Operatore import Operatore
from models.ListaOperatori import ListaOperatori

class MapperOperatori:
    db_directory=''

    def __init__(self):
        self.db_directory="./db/AAdb"

    def get_lista_operatori(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        lista_operatori = ListaOperatori()
        for row in cur.execute("SELECT * FROM Operatori"):
            operatore = Operatore(row[0], row[1], row[2], row[3], row[4], row[4], row[5])   
            lista_operatori.aggiungi_operatore(operatore)
        return lista_operatori

    def get_operatore(self, id):
        id=4

        
    def add_operatore(self, operatore):
        operatore = 'ciao'

    def modify_operatore(self, id, operatore):
        operatore=id
        
    

