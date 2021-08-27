class ListaMezzi:
    def __init__(self):
        self.lista_mezzi = []

    def inserisci_mezzo(self, mezzo):
        self.lista_mezzi.append(mezzo)

    def get_mezzo_by_id(self, index):
        return self.lista_mezzi[index]

    def get_lista_mezzi(self):
        return self.lista_mezzi