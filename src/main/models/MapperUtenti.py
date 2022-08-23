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
        con.close()
        if c.arraysize == 0:
            return False
        else:
            stored_pw = ""
            for row in c:
                stored_pw = row[0]
            parameters = stored_pw.split('$')
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
            utente = Utente(row[0], row[1], row[2], (row[3], row[4], row[5], row[6], row[7],row[8]))
            utenti.append(utente)
        con.close()
        return utenti

    def get_utente(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        utente=None
        #Non ho usato bindings perche rotti
        for row in cur.execute("SELECT * FROM Utenti WHERE id="+str(id)):
            utente = Utente(row[0], row[1], row[2], (row[3], row[4], row[5], row[6], row[7],row[8]))
        con.close()
        return utente 


    def get_utente_by_username(self, username):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        utente=None
        #Non ho usato bindings perche rotti
        for row in cur.execute("SELECT * FROM Utenti WHERE username=?", (username,)):
            utente = Utente(row[0], row[1], row[2], (row[3], row[4], row[5], row[6], row[7],row[8]))
        con.close()
        return utente 

    def ricerca_utenti(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        utenti = []
        for row in cur.execute('SELECT * FROM Utenti WHERE id LIKE ? OR username LIKE ?', ("%"+text+"%", "%"+text+"%")):
            utente = Utente(row[0], row[1], row[2], (row[3], row[4], row[5], row[6], row[7],row[8]))
            utenti.append(utente)
        con.close()
        return utenti 
    
    def insert_utente(self, utente):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        permessi = utente.get_permessi()
        cur.execute("INSERT INTO Utenti VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (utente.get_username(), self.encrypt_password(utente.get_password()), permessi[0], permessi[1], permessi[2], permessi[3], permessi[4], permessi[5]))
        con.commit()
        con.close()

    def encrypt_password(self, password):
        salt = os.urandom(10)
        hash = hashlib.scrypt(password.encode(), salt=salt, n=self.n, r=self.r, p=self.p, dklen=self.dklen)
        encrypted_password = f"{hash.hex()}${salt.hex()}${self.n}${self.r}${self.p}${self.dklen}"
        return encrypted_password


    def update_utente(self, id, utente):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        permessi = utente.get_permessi()
        cur.execute("UPDATE Utenti SET username=?, accesso_operatori=?, accesso_mezzi=?, accessi_servizi=?, accesso_turni=?, accesso_clienti=?, accesso_utenti=? WHERE id=?",
                (utente.get_username(), permessi[0], permessi[1], permessi[2], permessi[3], permessi[4], permessi[5]))
        con.commit()
        con.close()

    def elimina_utenti(self, utenti):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for utente in utenti:
            cur.execute("DELETE FROM Utenti WHERE id="+str(utente.get_id()))
        con.commit()
        con.close()
