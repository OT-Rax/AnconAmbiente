from models.MapperUtenti import MapperUtenti

class ControlloreUtenti:
    def __init__(self):
        self.mapper = MapperUtenti()
    
    #Metodi che si collegano ai metodi del mapper Utenti

    def check_password(self, username, password):
        return self.mapper.check_password(username, password)

    def get_utente(self, id):
        return self.mapper.get_utente(id)

    def get_utente_by_username(self, username):
        return self.mapper.get_utente_by_username(username)
    
    def get_utenti(self):
        return self.mapper.get_utenti()

    def insert_utente(self, utente):
        return self.mapper.insert_utente(utente)

    def ricerca_utenti(self, text):
        return self.mapper.ricerca_utenti(text)

    def elimina_utenti(self, utenti):
        return self.mapper.elimina_utenti(utenti)

    def modifica_utente(self, utente):
        return self.mapper.update_utente(utente.get_id(), utente)
