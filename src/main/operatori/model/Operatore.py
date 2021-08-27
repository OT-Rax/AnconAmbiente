class Operatore:
    def __init__(self, id, nome, cognome, cf, datanascita, stato, patenti):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.datanascita = datanascita
        self.stato = stato
        self.patenti = patenti

    #Metodi get

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_cf(self):
        return self.cf

    def get_datanascita(self):
        return self.datanascita

    def get_stato(self):
        return self.stato

    def get_patenti(self):
        return self.patenti

    #Metodi set

    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome

    def set_cognome(self, cognome):
        self.cognome = cognome

    def set_cf(self, cf):
        self.cf = cf

    def set_datanascita(self, datanascita):
        self.datanascita = datanascita

    def set_stato(self, stato):
        self.stato = stato

    def set_patenti(self, patenti):
        self.patenti = patenti