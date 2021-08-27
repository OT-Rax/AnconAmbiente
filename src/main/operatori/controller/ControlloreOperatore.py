from src.main.operatori.model.Operatore import Operatore
class ControlloreOperatore:
    def __init__(self):
        self.model = Operatore()

    #Metodi get

    def get_id(self):
        return self.model.get_id()

    def get_nome(self):
        return self.model.get_nome()

    def get_cognome(self):
        return self.model.get_cognome()

    def get_cf(self):
        return self.model.get_cf()

    def get_datanascita(self):
        return self.model.get_datanascita()

    def get_stato(self):
        return self.model.get_stato()

    def get_patenti(self):
        return self.model.get_patenti()

    #Metodi set

    def set_id(self, id):
        self.model.id = id

    def set_nome(self, nome):
        self.model.nome = nome

    def set_cognome(self, cognome):
        self.model.cognome = cognome

    def set_cf(self, cf):
        self.model.cf = cf

    def set_datanascita(self, datanascita):
        self.model.datanascita = datanascita

    def set_stato(self, stato):
        self.model.stato = stato

    def set_patenti(self, patenti):
        self.model.patenti = patenti
