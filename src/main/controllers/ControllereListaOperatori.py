from src.main.operatori.model.ListaOperatori import ListaOperatori
class ControlloreListaOperatori:
    def __init__(self):
        self.model = ListaOperatori()

    def get_lista_operatori(self):
        return  self.model.get_lista_operatori()

    #Metodo che restituisce l'operatore in posizione "index"
    def get_operatore_by_id(self, index):
        return self.model.get_operatore_by_id(index)

    def add_operatore(self, Operatore):
        self.model.aggiungi_operatore(Operatore)
