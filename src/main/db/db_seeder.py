import sqlite3
import random
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

    # Popolazione Operatori
    for i in range(10):
        operatore = [fake.first_name(), fake.last_name(), fake.date_of_birth(),
               fake.ssn(), fake.future_date(), fake.random_int(min=0, max=2)]
        cur.execute(' \
                INSERT INTO Operatori (nome, cognome, data_nascita, cf, data_fine_contratto, stato) \
                VALUES (?, ?, ?, ?, ?, ?); \
                ', operatore)

    # Popolazione Mezzi
    for i in range(10):
        patenti = ["B", "B1", "C"]
        tipo = ["Auto", "Autoarticolato", "Camion", "Camioncino"]
        mezzo = [fake.license_plate(), random.choice(patenti), random.choice(tipo),
                 fake.past_date(), fake.random_int(min=0, max=2)]
        cur.execute(' \
                    INSERT INTO Mezzi (targa, livello_richiesto, tipo, iscrizione_albo, stato) \
                    VALUES (?, ?, ?, ?, ?); \
                    ', mezzo)
    # Popolazione turni
    for i in range(10):
        turno = [fake.past_date(), fake.past_date()]
        cur.execute(' \
                            INSERT INTO Turni (inizio_turno, fine_turno) \
                            VALUES (?, ?); \
                            ', turno)

    # Popolazione Clienti
    for i in range(10):
        cliente = [fake.first_name(), fake.last_name(), fake.date_of_birth(), fake.ssn(),
                   fake.company_vat(), fake.address(), fake.ascii_email(), fake.phone_number()]
        cur.execute(' \
                                    INSERT INTO Clienti (nome, cognome, data_nascita, cf, partita_iva, indirizzo, email, telefono) \
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?); \
                                    ', cliente)

    # Popolazione Assegnamenti
    # id_turni = cur.execute(' \
    #                         SELECT id FROM Turni \
    #                         ')
    # id_mezzi = cur.execute(' \
    #                             SELECT id FROM Mezzi \
    #                             ')
    # for i in range(10):
    #     cur.execute(' \
    #                                         INSERT INTO Assegnamenti (id_turno, id_mezzo) \
    #                                         VALUES (?, ?); \
    #                                         ', id_turni, id_mezzi)

    # Popolazione Impieghi
    # id_operatori = cur.execute(' \
    #                             SELECT id FROM Operatori \
    #                             ')
    # for i in range(10):
    #     cur.execute(' \
    #                                         INSERT INTO Impieghi (id_turno, id_operatore) \
    #                                         VALUES (?, ?); \
    #                                         ', id_turni, id_mezzi)

    con.commit()
    con.close()


