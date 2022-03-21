class Cliente:
    def __init__(self, id, nome, cognome, cf, indirizzo, email, telefono, datanascita ):
        super(Cliente, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.indirizzo = indirizzo
        self.email = email
        self.telefono = telefono
        self. datanascita = datanascita

    # Metodi get / set

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_cf(self):
        return self.cf

    def get_indirizzo(self):
        return self.indirizzo

    def get_email(self):
        return self.email

    def get_telefono(self):
        return self.telefono

    def get_datanascita(self):
        return self.datanascita

    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome

    def set_cognome(self, cognome):
        self.cognome = cognome

    def set_cf(self, cf):
        self.cf = cf

    def set_indirizzo(self, indirizzo):
        self.indirizzo = indirizzo

    def set_email(self, email):
        self.email = email

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_datanascita(self, datanascita):
        self.datanascita = datanascita