class ListaUtenti:
    def __init__(self):
        super(ListaUtenti, self).__init__()
        self.lista_utenti = []

    def aggiungi_utente(self, cliente):
        self.lista_utenti.append(cliente)

    def elimina_utente_by_index(self, index):
        self.lista_utenti.pop(index)

    def get_utente_by_index(self, index):
        return self.lista_utenti[index]

    def get_lista_utenti(self):
        return self.lista_utenti
