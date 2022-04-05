from models.Operatore import Operatore
from models.MapperOperatori import MapperOperatori

class ControlloreOperatori:
    def __init__(self):
        self.mapper = MapperOperatori()

    def get_operatori(self):
        return self.mapper.get_operatori()
            
    def ricerca_operatori(self, text):
        return self.mapper.ricerca_operatori(text)
