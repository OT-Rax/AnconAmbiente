class Servizio:
    def __init__(self, id, id_cliente, tipo, luogo, data_inizio, data_fine, periodicita):
        self.id = id
        self.id_cliente = id_cliente
        self.tipo = tipo
        self.luogo = luogo
        self.data_inizio = data_inizio
        self.data_fine = data_fine
        self.periodicita = periodicita

    # Metodi getters and setters

    def get_id(self):
        return self.id

    def get_id_cliente(self):
        return self.id_cliente

    def get_tipo(self):
        return self.tipo

    def get_periodicita(self):
        return self.periodicita

    def get_luogo(self):
        return self.luogo
    
    def get_datainizio(self):
        return self.data_inizio

    def get_datafine(self):
        return self.data_fine

    def set_periodicita(self, periodicita):
        self.periodicita = periodicita

    def set_id(self, id):
        self.id = id

    def set_id_cliente(self, cliente):
        self.id_cliente = cliente

    def set_luogo_(self,luogo):
        self.get_luogo = luogo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_datainizio(self, data_inizio):
        self.data_inizio = data_inizio

    def set_datafine(self, data_fine):
        self.data_fine = data_fine
