from models.Operatore import Operatore
from models.MapperOperatori import MapperOperatori

class ControlloreOperatori:
    def __init__(self):
        self.mapper = MapperOperatori()

    def get_operatori(self):
        operatori = []
        for operatore in self.mapper.get_operatori():
            operatori.append(operatore)
        return operatori
            
    def ricerca_operatori(self, text):
        operatori = []
        for operatore in self.mapper.ricerca_operatori(text):
            operatori.append(operatore)
        return operatori
