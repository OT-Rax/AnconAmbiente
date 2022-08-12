import sqlite3
from faker import Faker

if __name__ == '__main__':
    fake = Faker('it_IT')
    con=sqlite3.connect('AAdb')
    cur=con.cursor()
    # cur.execute('''
    #     INSERT INTO Operatori (nome, cognome, data_nascita, cf, data_fine_contratto, stato)
    #                    VALUES ('Mario', 'Rossi', '1980-10-14', 'MARIOROSSI123456', NULL, 0),
    #                           ('Franco', 'Battiato', '1984-09-23', 'FRANCOMACFROIRFR', NULL, 1),
    #                           ('Gordon', 'Sbordon', '2022-11-11', '0123456789123456', NULL, 0)
    # ''')
    for i in range(10):
        row = [fake.first_name(), fake.last_name(), fake.date_of_birth(),
               fake.ssn(), fake.future_date(), fake.random_int(min=0, max=1)]
        cur.execute(' \
                INSERT INTO Operatori (nome, cognome, data_nascita, cf, data_fine_contratto, stato) \
                VALUES ("%s", "%s", "%s", %s, "%s", "%s", "%i"); \
                ' % (row[0], row[1], row[2], row[3], row[4], row[5]))

    con.commit()
    con.close()


