from src.main.mezzi.model.ListaMezzi import ListaMezzi
class ControlloreListaMezzi:
    def __init__(self):
        self.model = ListaMezzi()

    def inserisci_mezzo(self, mezzo): #Metodo che aggiunge un mezzo alla lista dei mezzi
        self.model.lista_mezzi.append(mezzo)

    def get_lista_mezzi(self):
        return self.model.get_lista_mezzi()

    def get_mezzo_by_id(self, index):
        return self.model.get_mezzo_by_id(index)
