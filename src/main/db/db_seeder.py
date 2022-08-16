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
    print("-----Popolazione Operatori-----")
    for i in range(10):
        print("Inserimento operatore numero", i) 
        operatore = [fake.first_name(), fake.last_name(), fake.date_of_birth(),
               fake.ssn(), fake.future_date(), fake.random_int(min=0, max=2)]
        cur.execute(' \
                INSERT INTO Operatori (nome, cognome, data_nascita, cf, data_fine_contratto, stato) \
                VALUES (?, ?, ?, ?, ?, ?); \
                ', operatore)
    print("-------------------------")

    # Popolazione Mezzi
    print("Popolazione Mezzi")
    for i in range(10):
        print("Inserimento mezzo numero", i) 
        patenti = ["B", "B1", "C"]
        tipo = ["Auto", "Autoarticolato", "Camion", "Camioncino"]
        mezzo = [fake.license_plate(), random.choice(patenti), random.choice(tipo),
                 fake.past_date(), fake.random_int(min=0, max=2)]
        cur.execute(' \
                    INSERT INTO Mezzi (targa, livello_richiesto, tipo, iscrizione_albo, stato) \
                    VALUES (?, ?, ?, ?, ?); \
                    ', mezzo)
    print("-------------------------")

    # Popolazione turni
    print("Popolazione Turni")
    for i in range(10):
        print("Inserimento turno numero", i) 
        turno = [fake.past_date(), fake.past_date()]
        cur.execute(' \
                            INSERT INTO Turni (inizio_turno, fine_turno) \
                            VALUES (?, ?); \
                            ', turno)
    print("-------------------------")

    # Popolazione Clienti
    print("Popolazione Clenti")
    for i in range(10):
        print("Inserimento cliente numero", i) 
        cliente = [fake.first_name(), fake.last_name(), fake.date_of_birth(), fake.ssn(),
                   fake.company_vat(), fake.address(), fake.ascii_email(), fake.phone_number()]
        cur.execute(' \
                                    INSERT INTO Clienti (nome, cognome, data_nascita, cf, partita_iva, indirizzo, email, telefono) \
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?); \
                                    ', cliente)
    print("-------------------------")

    # Popolazione Assegnamenti
    print("Popolazione Assegnamenti")
    id_turni = cur.execute(' \
                            SELECT id FROM Turni \
                            ').fetchall() #Prendo tutti i turni
    id_mezzi = cur.execute(' \
                                SELECT id FROM Mezzi \
                                ').fetchall() #Prendo tutti i mezzi
    for i in range(10):
        try:
            print("Inserimento assegnamento numero", i) 
            #prendo un turno ed un mezzo randomici
            turno_random=id_turni[fake.random_int(min=0, max=len(id_turni)-1)][0]
            mezzo_random=id_mezzi[fake.random_int(min=0, max=len(id_mezzi)-1)][0]
            cur.execute(' \
                                                INSERT INTO Assegnamenti (id_turno, id_mezzo) \
                                                VALUES (?, ?); \
                                                ', (turno_random, mezzo_random))
        except:
            print("Impiego numero ",i," gia presente")
    print("-------------------------")

    #Popolazione Impieghi
    print("Popolazione Impieghi")
    id_operatori = cur.execute(' \
                                SELECT id FROM Operatori \
                                ').fetchall() # Prendo tutti gli operatori
    for i in range(10):
        try:
            print("Inserimento impiego numero", i) 
            turno_random=id_turni[fake.random_int(min=0, max=len(id_turni)-1)][0]
            operatore_random=id_operatori[fake.random_int(min=0, max=len(id_operatori)-1)][0]
            cur.execute(' \
                                                INSERT INTO Impieghi (id_turno, id_operatore) \
                                                VALUES (?, ?); \
                                                ', (turno_random, operatore_random))
        except:
            print("Impiego numero ",i," gia presente")

    print("-------------------------")

    con.commit()
    con.close()


