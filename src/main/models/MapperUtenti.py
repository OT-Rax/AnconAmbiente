import sqlite3
import hashlib

from models.Utente import Utente

class MapperUtenti:
    def __init__(self):
        self.db_directory="./db/AAdb"
        #self.n=
        
    def check_password(self, username, login_pw):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        c = cur.execute("SELECT password_hash FROM Utenti WHERE username = ?", (username,))
        if c.rowcount == 0:
            return False
        else:
            stored_pw = ""
            for row in c:
                stored_pw = row[0]
            parameters = stored_pw.split('$')
            hashed_passw = hashlib.scrypt(login_pw, salt=parameters[1], n=parameters[2], r=parameters[3], p=parameters[4], dklen=parameters[5]) 
            if hashed_passw == parameters[0]:
                return True
            else:
                return False
