from models.Operatore import Operatore
from models.MapperOperatori import MapperOperatori

class ControlloreOperatori:
    def __init__(self):
        self.mapper = MapperOperatori()

    def get_operatori(self):
        return self.mapper.get_operatori()

    def insert_operatore(self, nome, cognome, cf, data_nascita, patenti, data_fine_contratto):
        return self.mapper.insert_operatore(nome, cognome, cf, data_nascita, patenti, data_fine_contratto)

    def ricerca_operatori(self, text):
        return self.mapper.ricerca_operatori(text)
