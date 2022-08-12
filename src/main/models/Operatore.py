class Operatore:
    def __init__(self, id, nome, cognome, datanascita, cf, datacontratto, stato):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.datanascita = datanascita
        self.cf = cf
        self.datacontratto = datacontratto
        self.stato = stato

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

    def get_datacontratto(self):
        return self.datacontratto

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

    def set_datacontratto(self, datacontratto):
        self.datacontratto = datacontratto
