import unittest
import sqlite3
from faker import Faker
import os
import sys
sys.path.append(os.path.dirname(__file__) + "../")
from models.MapperUtenti import MapperUtenti
from models.MapperOperatori import MapperOperatori
from models.Utente import Utente
from models.Operatore import Operatore

class TestAAERP (unittest.TestCase):
    dirname = os.path.dirname(__file__)
    db_file = os.path.join(dirname, '../db/AAdb')
    fake = Faker('it_IT')
    
    #Unit test per verificare che la verifica tramite hash della password funzioni
    def test_login(self):
        mapper_utenti = MapperUtenti()
        random_username = self.fake.user_name()
        random_password = self.fake.password()
        utente_test = Utente(0, random_username, random_password, [0,0,0,0,0,0])
        mapper_utenti.insert_utente(utente_test)
        self.assertTrue(mapper_utenti.check_password(random_username, random_password))

    #Unit test per verificare che l'inserimento vada a buon fine    
    def test_inserimento_operatore(self):
        mapper_operatori = MapperOperatori()
        nome_random = self.fake.first_name()
        cognome_random = self.fake.last_name()
        data_nascita_random = str(self.fake.date_of_birth())
        cf_random = self.fake.ssn()
        data_contratto_random = str(self.fake.future_date())
        stato_random = self.fake.random_int(min=0, max=2)
        mapper_operatori.insert_operatore(nome_random, cognome_random, data_nascita_random, cf_random, data_contratto_random, stato_random)
        operatore = mapper_operatori.get_ultimo_operatore()
        self.assertEqual(nome_random, operatore.get_nome())
        self.assertEqual(cognome_random, operatore.get_cognome())
        self.assertEqual(data_nascita_random, operatore.get_datanascita())
        self.assertEqual(cf_random, operatore.get_cf())
        self.assertEqual(data_contratto_random, operatore.get_datacontratto())
        self.assertEqual(stato_random, operatore.get_stato())

    #test che assicura che tutti e 3 i campi per la ricerca funzionino
    def test_ricerca_operatore(self):
        mapper_operatori = MapperOperatori()
        mapper_operatori.insert_operatore("Mario", "Rossi", "1900-10-31", "NTNBRC80M14E255O", "2022-12-16", 0)
        operatore_test = mapper_operatori.get_ultimo_operatore()
        operatori_test_nome = mapper_operatori.ricerca_operatori("Mario")
        operatori_test_cognome = mapper_operatori.ricerca_operatori("Rossi")
        presenza_ricerca_nome = False
        presenza_ricerca_cognome = False
        for operatore in operatori_test_nome:
            if operatore.get_id() == operatore_test.get_id():
                presenza_ricerca_nome = True
        for operatore in operatori_test_cognome:
            if operatore.get_id() == operatore_test.get_id():
                presenza_ricerca_cognome = True
        self.assertTrue(presenza_ricerca_nome)
        self.assertTrue(presenza_ricerca_cognome)

    def test_elimina_operatore(self):
        mapper_operatori = MapperOperatori()
        nome_random = self.fake.first_name()
        cognome_random = self.fake.last_name()
        data_nascita_random = self.fake.date_of_birth()
        cf_random = self.fake.ssn()
        data_contratto_random = self.fake.future_date()
        stato_random = self.fake.random_int(min=0, max=2)
        mapper_operatori.insert_operatore(nome_random, cognome_random, data_nascita_random, cf_random, data_contratto_random, stato_random)
        operatore = mapper_operatori.get_ultimo_operatore()
        mapper_operatori.elimina_operatori((operatore,))
        self.assertIsNone(mapper_operatori.get_operatore(operatore.get_id()))
    
    def test_update_operatore(self):
        mapper_operatori = MapperOperatori()
        nome_random = self.fake.first_name()
        cognome_random = self.fake.last_name()
        data_nascita_random = self.fake.date_of_birth()
        cf_random = self.fake.ssn()
        data_contratto_random = self.fake.future_date()
        stato_random = self.fake.random_int(min=0, max=2)
        mapper_operatori.insert_operatore(nome_random, cognome_random, data_nascita_random, cf_random, data_contratto_random, stato_random)
        operatore = mapper_operatori.get_ultimo_operatore()
        nome_test = self.fake.first_name()
        operatore.set_nome = nome_test
        mapper_operatori.update_operatore(operatore.get_id(), operatore)
        self.assertEqual(operatore.get_nome(), mapper_operatori.get_ultimo_operatore().get_nome()) 

if __name__ == '__main__':
    unittest.main()
