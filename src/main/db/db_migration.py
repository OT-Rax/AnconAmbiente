import sqlite3

if __name__ == '__main__':
    con=sqlite3.connect('AAdb')
    cur=con.cursor()
    cur.execute('''
        DROP TABLE IF EXISTS Patenti;
    ''')
    cur.execute('''
        CREATE TABLE Patenti(
        livello TEXT PRIMARY KEY,
        descrizione TEXT
        );
    ''')

    cur.execute('''
        DROP TABLE IF EXISTS Operatori;
    ''')
    cur.execute('''
        CREATE TABLE Operatori(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cognome TEXT NOT NULL,
        data_nascita TEXT NOT NULL,
        cf TEXT NOT NULL,
        data_fine_contratto TEXT,
        stato INT NOT NULL CHECK(stato>=0 & stato<=2)
        );
    ''')

    cur.execute('''
        DROP TABLE IF EXISTS Abilitazioni;
    ''')
    cur.execute('''
        CREATE TABLE Abilitazioni(
        livello_patente TEXT, 
        id_operatore INTEGER,
        FOREIGN KEY(livello_patente) REFERENCES Patenti(livello),
        FOREIGN KEY(id_operatore) REFERENCES Operatori(id),
        PRIMARY KEY(livello_patente, id_operatore)
        );
    ''')

    cur.execute('''
        DROP TABLE IF EXISTS Mezzi;
    ''')
    cur.execute('''
        CREATE TABLE Mezzi(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        targa TEXT NOT NULL,
        tipo TEXT NOT NULL,
        allestimento TEXT NOT NULL,
        iscrizione_albo TEXT,
        patente TEXT NOT NULL,
        stato INT NOT NULL CHECK(stato>=0 & stato<=2)
        );
    ''')

    cur.execute('''
        DROP TABLE IF EXISTS Turni;
    ''')

    cur.execute('''
        CREATE TABLE Turni(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_inizio TEXT NOT NULL,
        data_fine TEXT NOT NULL
        );
    ''')

    cur.execute('''
        DROP TABLE IF EXISTS Impieghi;
    ''')
    cur.execute('''
        CREATE TABLE Impieghi(
        id_turno INTEGER,
        id_operatore INTEGER,
        FOREIGN KEY(id_turno) REFERENCES Turni(id),
        FOREIGN KEY(id_operatore) REFERENCES Operatori(id),
        PRIMARY KEY(id_turno, id_operatore)
        );
    ''')

    cur.execute('''
        DROP TABLE IF EXISTS Assegnamenti;
    ''')
    cur.execute('''
        CREATE TABLE Assegnamenti(
        id_turno INTEGER,
        id_mezzo INTEGER,
        FOREIGN KEY(id_turno) REFERENCES Turni(id),
        FOREIGN KEY(id_mezzo) REFERENCES Mezzi(id),
        PRIMARY KEY(id_turno, id_mezzo));
    ''')

    cur.execute('''
        DROP TABLE IF EXISTS Clienti;
    ''')
    cur.execute('''
        CREATE TABLE Clienti(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cognome TEXT NOT NULL,
        data_nascita TEXT,
        cf TEXT NOT NULL,
        partita_iva TEXT NOT NULL,
        indirizzo TEXT,
        email TEXT,
        telefono TEXT
        );
    ''')

    cur.execute('''
        DROP TABLE IF EXISTS Servizi;
    ''')
    cur.execute('''
        CREATE TABLE Servizi(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER NOT NULL,
        tipo TEXT NOT NULL,
        luogo TEXT NOT NULL,
        data_inizio TEXT NOT NULL,
        data_fine TEXT NOT NULL,
        ripetizione INTEGER,
        periodicita TEXT,
        FOREIGN KEY(id_cliente) REFERENCES Clienti(id)
        );
    ''')

    cur.execute('''
        DROP TABLE IF EXISTS Lavori;
    ''')
    cur.execute('''
        CREATE TABLE Lavori(
        id_turno INTEGER NOT NULL,
        id_servizio INTEGER NOT NULL,
        FOREIGN KEY(id_turno) REFERENCES Turni(id),
        FOREIGN KEY(id_servizio) REFERENCES Servizi(id),
        PRIMARY KEY(id_turno, id_servizio)
        );
    ''')

    cur.execute('''
        DROP TABLE IF EXISTS Utenti;
    ''')
    cur.execute('''
        CREATE TABLE Utenti(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        accesso_operatori INT NOT NULL CHECK(accesso_operatori>=0 & accesso_operatori<=2),
        accesso_mezzi INT NOT NULL CHECK(accesso_mezzi>=0 & accesso_mezzi<=2),
        accesso_servizi INT NOT NULL CHECK(accesso_servizi>=0 & accesso_servizi<=2),
        accesso_turni INT NOT NULL CHECK(accesso_turni>=0 & accesso_turni<=2),
        accesso_clienti INT NOT NULL CHECK(accesso_clienti>=0 & accesso_clienti<=2),
        accesso_utenti INT NOT NULL CHECK(accesso_utenti>=0 & accesso_utenti<=2)
        );
    ''')
    con.commit()
    con.close()
