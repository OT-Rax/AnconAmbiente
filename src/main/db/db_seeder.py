import sqlite3
from faker import Faker

if __name__ == '__main__':
    con=sqlite3.connect('AAdb')
    cur=con.cursor()
    cur.execute('''
        INSERT INTO Operatori (nome, cognome, data_nascita, cf, data_fine_contratto, stato)
                       VALUES ('Mario', 'Rossi', '1980-10-14', 'MARIOROSSI123456', NULL, 0),
                              ('Franco', 'Battiato', '1984-09-23', 'FRANCOMACFROIRFR', NULL, 1),
                              ('Gordon', 'Sbordon', '2022-11-11', '0123456789123456', NULL, 0)
    ''')
    con.commit()
    con.close()
