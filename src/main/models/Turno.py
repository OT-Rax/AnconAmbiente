class Turno:
    def __init__(self, id, servizio, data_inizio, data_fine, mezzi, operatori):
        self.id = id
        self.servizio = servizio
        self.data_inizio = data_inizio
        self.data_fine = data_fine
        self.mezzi = mezzi
        self.operatori = operatori

#metodi getter 

    def get_id(self):
        return self.id

    def get_servizio(self):
        return self.servizio

    def get_data_inizio(self):
        return self.data_inizio

    def get_data_fine(self):
        return self.data_fine

    def get_mezzi(self):
        return self.mezzi

    def get_operatori(self):
        return self.operatori

    #metodi setter

    def set_servizio(self, servizio):
        self.servizio = servizio

    def set_data_inizio(self, data_inizio):
        self.data_inizio = data_inizio

    def set_data_fine(self, data_fine):
        self.data_fine = data_fine

    def set_mezzi(self, mezzi):
        self.mezzi = mezzi

    def set_operatori(self, operatori):
        self.operatori = operatori


