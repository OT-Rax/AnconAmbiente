import sqlite3
import os
import hashlib

from models.Utente import Utente

class MapperUtenti:
    def __init__(self):
        dirname = os.path.dirname(__file__)
        db_file = os.path.join(dirname, '../db/AAdb')
        self.db_directory = db_file
        self.n=2
        self.r=16
        self.p=1
        self.dklen=64
    
    #Metodo che verifica che l'username e la password inserite nel login siano corrette
    # :param username: username dell'utente
    # :param login_pw: password dell'utente
    def check_password(self, username, login_pw):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        c = cur.execute("SELECT password_hash FROM Utenti WHERE username = ?", (username,)).fetchall()
        if len(c)==0:
            return False
        else:
            stored_pw = ""
            for row in c:
                stored_pw = row[0]
            parameters = stored_pw.split('$')
            hashed_passw = hashlib.scrypt(login_pw.encode(), salt=bytes.fromhex(parameters[1]), n=int(parameters[2]), r=int(parameters[3]), p=int(parameters[4]), dklen=int(parameters[5])) 
            if hashed_passw.hex() == parameters[0]:
                con.close()
                return True
            else:
                con.close()
                return False

    #Metodo che restituisce tutti gli utenti presenti nel DataBase
    def get_utenti(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        utenti = []
        for row in cur.execute("SELECT * FROM Utenti"):
            utente = Utente(row[0], row[1], row[2], (row[3], row[4], row[5], row[6], row[7],row[8]))
            utenti.append(utente)
        con.close()
        return utenti

    #Metodo che restituisce un utente attraverso l'id dato in input
    # :param id: id dell'utente
    def get_utente(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        utente=None
        for row in cur.execute("SELECT * FROM Utenti WHERE id="+str(id)):
            utente = Utente(row[0], row[1], row[2], (row[3], row[4], row[5], row[6], row[7],row[8]))
        con.close()
        return utente 

    #Metodo che restituisce un utente attraverso l'username dato in input
    # :param username: username dell'utente
    def get_utente_by_username(self, username):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        utente=None
        #Non ho usato bindings perche rotti
        for row in cur.execute("SELECT * FROM Utenti WHERE username=?", (username,)):
            utente = Utente(row[0], row[1], row[2], (row[3], row[4], row[5], row[6], row[7],row[8]))
        con.close()
        return utente 

    #Metodo che restituisce un oggetto popolato dagli utenti che hanno in comune l'id o l'username dato in input
    # :param text: oggetto contenente la stringa di caratteri per la ricerca di determinati utenti
    def ricerca_utenti(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        utenti = []
        for row in cur.execute('SELECT * FROM Utenti WHERE id LIKE ? OR username LIKE ?', ("%"+text+"%", "%"+text+"%")):
            utente = Utente(row[0], row[1], row[2], (row[3], row[4], row[5], row[6], row[7],row[8]))
            utenti.append(utente)
        con.close()
        return utenti 
    
    #Metodo che inserisce un Utente nel DataBase
    # :param utente: oggetto utente da inserire nel DataBase
    def insert_utente(self, utente):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        permessi = utente.get_permessi()
        cur.execute("INSERT INTO Utenti (username, password_hash, accesso_operatori, accesso_mezzi, accesso_servizi, accesso_turni, accesso_clienti, accesso_utenti) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (utente.get_username(), self.encrypt_password(utente.get_password()), permessi[0], permessi[1], permessi[2], permessi[3], permessi[4], permessi[5]))
        con.commit()
        con.close()


    def encrypt_password(self, password):
        salt = os.urandom(10)
        hash = hashlib.scrypt(password.encode(), salt=salt, n=self.n, r=self.r, p=self.p, dklen=self.dklen)
        encrypted_password = f"{hash.hex()}${salt.hex()}${self.n}${self.r}${self.p}${self.dklen}"
        return encrypted_password

    #Metodo che va ad aggiornare i dati modificati di un Utente
    # :param id: id dell'utente da modificare
    # :param utente: oggetto contenete i dati aggiornati dell'utente da inserire nel DataBase 
    def update_utente(self, id, utente):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        permessi = utente.get_permessi()
        cur.execute("UPDATE Utenti SET username=?, accesso_operatori=?, accesso_mezzi=?, accesso_servizi=?, accesso_turni=?, accesso_clienti=?, accesso_utenti=? WHERE id=?",
                (utente.get_username(), permessi[0], permessi[1], permessi[2], permessi[3], permessi[4], permessi[5], id))
        con.commit()
        con.close()

    #Metodo per l'eliminazione degli utenti dal DataBase
    # :param utenti: oggetto contenente gli utenti che si vogliono eliminare dal DataBase
    def elimina_utenti(self, utenti):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for utente in utenti:
            cur.execute("DELETE FROM Utenti WHERE id="+str(utente.get_id()))
        con.commit()
        con.close()
