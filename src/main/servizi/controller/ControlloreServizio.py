class ControlloreServizio:
    def __init__(self, servizio):
        self.model = servizio

    def get_stato_servizio(self):
        return self.model.stato

    def get_periodicita_servizio(self):
        return self.model.periodicita

    def get_id_servizio(self):
        return self.model.id

    def get_cliente_servizio(self):
        return self.model.cliente

    def get_tipo_servizio(self):
        return self.model.tipo

    def set_stato_servizio(self, stato):
        self.model.stato = stato

    def set_periodicita_servizio(self, periodicita):
        self.model.periodicita = periodicita

    def set_id_servizio(self, id):
        self.model.id = id

    def set_cliente_servizio(self, cliente):
        self.model.cliente = cliente

    def set_tipo_servizio(self, tipo):
        self.model.tipo = tipo
