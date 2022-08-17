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
    patenti = ["B", "B1", "C"]
    for i in range(10):
        print("Inserimento mezzo numero", i)
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
            print("Assegnamento numero ",i," gia presente")
    print("-------------------------")

    # Popolazione Impieghi
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

    # Popolazione Patenti
    print("Popolazione Patenti")
    for i in range(10):
        try:
            print("Inserimento patente numero", i)
            patente = [random.choice(patenti), 'Patente']
            cur.execute(' \
                                                    INSERT INTO Patenti (livello, descrizione) \
                                                    VALUES (?, ?); \
                                                    ', (turno_random, operatore_random))
        except:
            print("Patente numero ", i, " gia presente")

    print("-------------------------")

    # Popolazione Servizi
    print("Popolazione Servizi")
    id_clienti = cur.execute(' \
                                SELECT id FROM Clienti \
                                ').fetchall()  # Prendo tutti i clienti
    for i in range(10):
        try:
            cliente_random = id_clienti[fake.random_int(min=0, max=len(id_clienti) - 1)][0]
            tipo = ['Pulizia strada', 'Raccolta rifiuti', 'Pulizia straordinaria', 'Raccolta a domicilio']
            periodicita = ['Giornaliero', 'Mensile', 'Annuale', 'Bimestrale', 'Trimestrale', 'Settimanale']
            print("Inserimento servizio numero", i)
            servizio = [cliente_random, tipo, periodicita]
            cur.execute(' \
                                                        INSERT INTO Servizi (id_cliente, tipo, periodicita) \
                                                        VALUES (?, ?, ?); \
                                                        ', servizio)
        except:
            print("Servizio numero ", i, " gia presente")

    print("-------------------------")

    con.commit()
    con.close()


