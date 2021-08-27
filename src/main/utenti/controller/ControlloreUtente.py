class ControlloreUtente:
    def __init__(self, utente):
        self.model = utente

    def get_nome_utente_utente(self):
        return self.model.nome

    def get_password_utente(self):
        return self.model.password

    def get_permessi_utente(self):
        return self.model.permessi

    def set_nome_utente(self, nome):
        self.model.nome = nome

    def set_password_utente(self, password):
        self.model.password = password

    def set_permessi_utente(self, permessi):
        self.model.permessi = permessi
