class ListaClienti:
    def __init__(self):
        super(ListaClienti, self).__init__()
        self.lista_clienti = []

    def aggiungi_clienti(self, cliente):
        self.lista_clienti.append(cliente)

    def get_cliente_by_index(self, index):
        return self.lista_clienti[index]

    def get_lista_clienti(self):
        return self.lista_clienti
