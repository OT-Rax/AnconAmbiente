import sqlite3

from models.Cliente import Cliente

class MapperClienti:
    def __init__(self):
        self.db_directory="./db/AAdb"

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

    def get_idclienti(self):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        id = []
        for row in cur.execute("SELECT id FROM Clienti"):
            #Cliente(id, nome, cognome, datanascita, cf, partitaiva, indirizzo, email, telefono):
            id.append(row[0])
        con.close()
        return id

    def get_cliente(self, id):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cliente=None
        #Non ho usato bindings perche rotti
        for row in cur.execute("SELECT * FROM Clienti WHERE id="+str(id)):
            cliente = Cliente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]) 
        con.close()
        return cliente
    
    def ricerca_clienti(self, text):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        clienti  = []
        for row in cur.execute('SELECT * FROM Clienti WHERE id LIKE ? OR nome LIKE ? OR cognome LIKE ?', ("%"+text+"%", "%"+text+"%","%"+text+"%")):
            cliente = Cliente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])   
            clienti.append(cliente)
        con.close()
        return clienti

    def insert_cliente(self, nome, cognome, datanascita, cf, partitaiva, indirizzo, email, telefono):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("INSERT INTO Clienti (nome, cognome, data_nascita, cf, partita_iva, indirizzo, email, telefono) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (nome, cognome, datanascita, cf, partitaiva, indirizzo, email, telefono))
        con.commit()
        con.close()


    def update_cliente(self, id, cliente):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        cur.execute("UPDATE Clienti SET nome=?, cognome=?, data_nascita=?, cf=?, partita_iva=?, indirizzo=?, email=?, telefono=? WHERE id=?", (cliente.get_nome(), cliente.get_cognome(), cliente.get_datanascita(), cliente.get_cf(), cliente.get_partitaiva(), cliente.get_indirizzo(), cliente.get_email(), cliente.get_telefono(), id))
        con.commit()
        con.close()

    def elimina_clienti(self, clienti):
        con = sqlite3.connect(self.db_directory)
        cur = con.cursor()
        for cliente in clienti:
            cur.execute("DELETE FROM Clienti WHERE id="+str(cliente.get_id()))
        con.commit()
        con.close()
