from models.MapperServizi import MapperServizi
class ControlloreServizio:
    def __init__(self):
        self.mapper = MapperServizi()

    def elimina_servizi(self, servizi):
        return self.mapper.elimina_servizi(servizi)

    def get_servizi(self):
        return self.mapper.get_servizi()

    def get_servizio(self, id):
        return self.mapper.get_servizio(id)

    def ricerca_servizi(self, text):
        return self.mapper.ricerca_servizi(text)

    def get_stato_servizio(self):
        return self.mapper.stato

    def get_periodicita_servizio(self):
        return self.mapper.periodicita

    def get_id_servizio(self):
        return self.mapper.id

    def get_cliente_servizio(self):
        return self.mapper.cliente

    def get_tipo_servizio(self):
        return self.mapper

    def set_stato_servizio(self, stato):
        self.mapper.stato = stato

    def set_periodicita_servizio(self, periodicita):
        self.mapper.periodicita = periodicita

    def set_id_servizio(self, id):
        self.mapper.id = id

    def set_cliente_servizio(self, cliente):
        self.mapper.cliente = cliente

    def set_tipo_servizio(self, tipo):
        self.mapper.tipo = tipo

    def insert_cliente(self, id_cliente,):
        return self.mapper.insert_mezzo()
