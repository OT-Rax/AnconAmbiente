from models.MapperServizi import MapperServizi

class ControlloreServizi:
    def __init__(self):
        self.mapper = MapperServizi()

    def elimina_servizi(self, servizi):
        return self.mapper.elimina_servizi(servizi)

    def get_servizi(self):
        return self.mapper.get_servizi()

    def get_servizio(self, id):
        return self.mapper.get_servizio(id)

    def update_servizio(self, servizio):
        return self.mapper.update_servizio(servizio.get_id(), servizio)

    def ricerca_servizi(self, text):
        return self.mapper.ricerca_servizi(text)

    def insert_servizio(self, id_cliente, tipo, luogo, data_inizio, data_fine, ripetizione, periodicita):
        return self.mapper.insert_servizio(id_cliente, tipo, luogo, data_inizio, data_fine, ripetizione, periodicita)
