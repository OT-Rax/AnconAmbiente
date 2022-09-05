import os
import sqlite3

from models.Cliente import Cliente


class MapperClienti:
    def __init__(self):
        dirname = os.path.dirname(__file__)
        db_file = os.path.join(dirname, '../db/AAdb')
        self.db_directory=db_file

    #Metodo che restituisce tutti i clienti presenti nel Database
    def get_clienti(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        clienti = []
        for row in cur.execute("SELECT * FROM Clienti"):
            #Cliente(id, nome, cognome, datanascita, cf, partitaiva, indirizzo, email, telefono):
            cliente = Cliente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            clienti.append(cliente)
        con.close()
        return clienti

    #Metodo che restituisce tutti gli id dei clienti presenti nel DataBase
    def get_idclienti(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        id = []
        for row in cur.execute("SELECT id FROM Clienti"):
            #Cliente(id, nome, cognome, datanascita, cf, partitaiva, indirizzo, email, telefono):
            id.append(row[0])
        con.close()
        return id

    #Metodo che restituisce un cliente presente nel DataBase attraverso il suo id
    # :param id: Oggetto contenente l'id del cliente che si vuole ottenere
    def get_cliente(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cliente=None
        for row in cur.execute("SELECT * FROM Clienti WHERE id="+str(id)):
            cliente = Cliente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]) 
        con.close()
        return cliente
    
    #Metodo che restituisce un oggetto di clienti che hanno l'id o il nome  o il congnome dato in input
    # :param text: oggetto contenente l'id o il nome o il cognome dei clienti che si vogliono ottenere in output 
    def ricerca_clienti(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        clienti  = []
        for row in cur.execute('SELECT * FROM Clienti WHERE id LIKE ? OR nome LIKE ? OR cognome LIKE ?', ("%"+text+"%", "%"+text+"%","%"+text+"%")):
            cliente = Cliente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])   
            clienti.append(cliente)
        con.close()
        return clienti

    #metodo per l'inserimento del cliente nel DB
    # :param nome: nome del cliente
    # :param cognome: cognome del cliente
    # :param datanascita: data di nascita del cliente
    # :param cf: codice fiscale del cliente
    # :param partitaiva: partita iva del cliente
    # :param indirizzo: indirizzo del cliente
    # :param email: indirizzo email del cliente
    # :param telefono: numero di telefono/cellulare del cliente
    def insert_cliente(self, nome, cognome, datanascita, cf, partitaiva, indirizzo, email, telefono):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Clienti (nome, cognome, data_nascita, cf, partita_iva, indirizzo, email, telefono) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (nome, cognome, datanascita, cf, partitaiva, indirizzo, email, telefono))
        con.commit()
        con.close()

    #Metodo che va ad aggiornare i dati modificati di un cliente
    # :param id: id del cliente da modificare
    # :param cliente: oggetto contenete i dati aggiornati del cliente da inserire nel DB 
    def update_cliente(self, id, cliente):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("UPDATE Clienti SET nome=?, cognome=?, data_nascita=?, cf=?, partita_iva=?, indirizzo=?, email=?, telefono=? WHERE id=?", (cliente.get_nome(), cliente.get_cognome(), cliente.get_datanascita(), cliente.get_cf(), cliente.get_partitaiva(), cliente.get_indirizzo(), cliente.get_email(), cliente.get_telefono(), id))
        con.commit()
        con.close()

    #Metodo per l'eliminazione di un cliente dal DataBase
    # :param clienti: oggetto contenente il cliente che si vuole eliminare dal DataBase
    def elimina_clienti(self, clienti):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for cliente in clienti:
            cur.execute("DELETE FROM Clienti WHERE id="+str(cliente.get_id()))
        con.commit()
        con.close()
