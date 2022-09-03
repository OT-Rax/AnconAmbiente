import sqlite3
import random
import os
import hashlib
from faker import Faker

if __name__ == '__main__':
    fake = Faker('it_IT')
    con=sqlite3.connect('AAdb')
    cur=con.cursor()
    # Inserimento Utenti default
    print("-----Inserimento Utenti-----")
    n=2
    r=16
    p=1
    dklen=64
    salt = os.urandom(10)
    hash = hashlib.scrypt("admin".encode(), salt=salt, n=n, r=r, p=p, dklen=dklen)
    encrypted_password = f"{hash.hex()}${salt.hex()}${n}${r}${p}${dklen}"
    try:
        cur.execute(' \
                INSERT INTO Utenti (username, password_hash, accesso_operatori, accesso_mezzi, accesso_servizi, accesso_turni, accesso_clienti, accesso_utenti) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?); \
                ', ("admin", encrypted_password , 1, 1, 1, 1, 1, 1))
    except sqlite3.IntegrityError:
        print("Utente admin già presente")
    except Exception as e:
        print(e)
    print("-------------------------")

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
        allestimento = ["Spazzamento", "Raccoglimento", "Trasporto"]
        mezzo = [fake.license_plate(), random.choice(tipo),
                 random.choice(allestimento), fake.past_date(), random.choice(patenti), fake.random_int(min=0, max=2)]
        cur.execute(' \
                    INSERT INTO Mezzi (targa, tipo, allestimento, iscrizione_albo, patente, stato) \
                    VALUES (?, ?, ?, ?, ?, ?); \
                    ', mezzo)
    print("-------------------------")

    # # Popolazione Turni
    # print("Popolazione Turni")
    # for i in range(10):
    #     print("Inserimento turno numero", i)
    #     turno = [fake.past_date(), fake.past_date()]
    #     cur.execute(' \
    #                         INSERT INTO Turni (inizio_turno, fine_turno) \
    #                         VALUES (?, ?); \
    #                         ', turno)
    # print("-------------------------")

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
        except sqlite3.IntegrityError:
            print("Assegnamento numero ",i," gia presente")
        except Exception as e:
            print(e)

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
        except sqlite3.IntegrityError:
            print("Impiego numero ",i," gia presente")
        except Exception as e:
            print(e)

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
                                                    ', patente)
        except sqlite3.IntegrityError:
            print("Patente numero ", i, " gia presente")
        except Exception as e:
            print(e)

    print("-------------------------")

    # Popolazione Servizi
    print("Popolazione Servizi")
    id_clienti = cur.execute(' \
                                SELECT id FROM Clienti \
                                ').fetchall()  # Prendo tutti i clienti
    tipo = ['Pulizia strada', 'Raccolta rifiuti', 'Pulizia straordinaria', 'Raccolta a domicilio']
    periodicita = [None, 'Giornaliero', 'Settimanale', 'Mensile', 'Annuale']
    for i in range(10):
        try:
            cliente_random = id_clienti[fake.random_int(min=0, max=len(id_clienti) - 1)][0]
            tipo_random = tipo[fake.random_int(min=0, max=len(tipo) - 1)]
            luogo_random = fake.address()
            data_inizio_random = fake.past_date()
            data_fine_random = fake.future_date()
            ripetizione_random = fake.random_int(min=1, max=5)
            periodicita_random=periodicita[fake.random_int(min=0, max=len(periodicita) - 1)]
            print("Inserimento servizio numero", i)
            servizio = [cliente_random, tipo_random, luogo_random, data_inizio_random, data_fine_random, ripetizione_random, periodicita_random]
            cur.execute(' \
                                                        INSERT INTO Servizi (id_cliente, tipo, luogo, data_inizio, data_fine, ripetizione, periodicita) \
                                                        VALUES (?, ?, ?, ?, ?, ?, ?); \
                                                        ', servizio)
        except sqlite3.IntegrityError:
            print("Servizio numero ", i, " gia presente")
        except Exception as e:
            print(e)

    print("-------------------------")

    # Popolazione Lavori
    print("Popolazione Lavori")

    for i in range(10):
        id_turni = cur.execute(' \
                                SELECT id FROM Turni \
                                ').fetchall() #Prendo tutti i turni
        id_servizi = cur.execute(' \
                                        SELECT id FROM Servizi \
                                        ').fetchall()  # Prendo tutti i clienti
        try:
            print("Inserimento lavoro numero", i)
            turno_random = id_turni[fake.random_int(min=0, max=len(id_turni) - 1)][0]
            servizio_random = id_servizi[fake.random_int(min=0, max=len(id_servizi) - 1)][0]
            cur.execute(' \
                                                           INSERT INTO Lavori (id_turno, id_servizio) \
                                                           VALUES (?, ?); \
                                                           ', (turno_random, servizio_random))
        except sqlite3.IntegrityError:
            print("Lavoro numero ", i, " gia presente")
        except Exception as e:
            print(e)

    print("-------------------------")

    # Popolazione Abilitazioni
    print("Popolazione Abilitazioni")

    for i in range(10):

        try:
            print("Inserimento abilitazione numero", i)
            patente_random = random.choice(patenti)
            operatore_random = id_operatori[fake.random_int(min=0, max=len(id_operatori) - 1)][0]
            cur.execute(' \
                                                              INSERT INTO Abilitazioni (livello_patente, id_operatore) \
                                                              VALUES (?, ?); \
                                                              ', (patente_random, operatore_random))
        except sqlite3.IntegrityError:
            print("Abilitazione numero ", i, " gia presente")
        except Exception as e:
            print(e)

    print("-------------------------")

    con.commit()
    con.close()

    
