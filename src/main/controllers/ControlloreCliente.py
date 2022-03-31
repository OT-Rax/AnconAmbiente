class ControlloreCliente:
    def __init__(self, cliente):
        self.model = cliente
    def get_id_cliente(self):
        return self.model.id

    def get_nome_cliente(self):
        return self.model.nome

    def get_cognome_cliente(self):
        return self.model.cognome

    def get_cf_cliente(self):
        return self.model.cf

    def get_indirizzo_cliente(self):
        return self.model.indirizzo

    def get_email_cliente(self):
        return self.model.email

    def get_telefono_cliente(self):
        return self.model.telefono

    def get_datanascita(self):
        return self.model.datanascita

    def set_id_cliente(self, id):
        self.model.id = id

    def set_nome_cliente(self, nome):
        self.model.nome = nome

    def set_cognome_cliente(self, cognome):
        self.model.cognome = cognome

    def set_cf_cliente(self, cf):
        self.model.cf = cf

    def set_indirizzo_cliente(self, indirizzo):
        self.model.indirizzo = indirizzo

    def set_email_cliente(self, email):
        self.model.email = email

    def set_telefono_cliente(self, telefono):
        self.model.telefono = telefono

    def set_datanascita_cliente(self, datanascita):
        self.model.datanascita = datanascita
