import sqlite3
import os
import hashlib

from models.Utente import Utente

class MapperUtenti:
    def __init__(self):
        self.db_directory="./db/AAdb"
        self.n=2
        self.r=16
        self.p=1
        self.dklen=64
        
    def check_password(self, username, login_pw):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        c = cur.execute("SELECT password_hash FROM Utenti WHERE username = ?", (username,))
        print(c.arraysize)
        if c.arraysize == 0:
            return False
        else:
            stored_pw = ""
            for row in c:
                stored_pw = row[0]
            parameters = stored_pw.split('$')
            print(parameters[1])
            hashed_passw = hashlib.scrypt(login_pw.encode(), salt=bytes.fromhex(parameters[1]), n=int(parameters[2]), r=int(parameters[3]), p=int(parameters[4]), dklen=int(parameters[5])) 
            if hashed_passw.hex() == parameters[0]:
                return True
            else:
                return False

    def get_utenti(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        utenti = []
        for row in cur.execute("SELECT * FROM Utenti"):
            utenti.append(Utente(row[0], row[1], row[2], (row[3], row[4], row[5], row[6], row[7],row[8])))
        return utenti


    def insert_utente(self, utente):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        permessi = utente.get_permessi()
        #cur.execute("INSERT INTO Utenti VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (utente.get_id(), utente.get_username(), self.encrypt_password(utente.get_password()))
        con.commit()

    def encrypt_password(self, password):
        salt = os.urandom(10)
        hash = hashlib.scrypt(password.encode(), salt=salt, n=self.n, r=self.r, p=self.p, dklen=self.dklen)
        encrypted_password = f"{hash.hex()}${salt.hex()}${self.n}${self.r}${self.p}${self.dklen}"
        return encrypted_password
