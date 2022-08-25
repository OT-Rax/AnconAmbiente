class Servizio:
    def __init__(self, id, id_cliente, tipo, periodicita):
        self.id = id
        self.id_cliente = id_cliente
        self.tipo = tipo
        self.periodicita = periodicita

    # Metodi getters and setters

    def get_id_cliente(self):
        return self.id_cliente

    def get_tipo(self):
        return self.tipo

    def get_periodicita(self):
        return self.periodicita

    def set_stato(self, stato):
        self.stato = stato


    def set_periodicita(self, periodicita):
        self.periodicita = periodicita


    def set_id(self, id):
        self.id = id


    def set_id_cliente(self, cliente):
        self.id_cliente = cliente


    def set_tipo(self, tipo):
        self.tipo = tipo
