class ListaOperatori:
    def __init__(self):
        self.lista_operatori = []

    def aggiungi_operatore(self, operatore):
        self.lista_operatori.append(operatore)

    def get_lista_operatori(self):
        return self.lista_operatori

    #Metodo che restituisce l'operatore in posizione "index"
    def get_operatore_by_id(self, index):
        return self.lista_operatori[index]