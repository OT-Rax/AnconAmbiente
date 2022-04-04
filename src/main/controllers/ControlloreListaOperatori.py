from models.ListaOperatori import ListaOperatori
from models.MapperOperatori import MapperOperatori
class ControlloreListaOperatori:
    def __init__(self):
        self.model = ListaOperatori()
        self.mapper = MapperOperatori()

    def get_operatori(self):
        return  self.mapper.get_operatori()

    #Metodo che restituisce l'operatore in posizione "index"
    def get_operatore_by_id(self, index):
        return self.model.get_operatore_by_id(index)

    def add_operatore(self, Operatore):
        self.model.aggiungi_operatore(Operatore)
