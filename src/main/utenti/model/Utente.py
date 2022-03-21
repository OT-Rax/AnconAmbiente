class Utente:
    def __init__(self, nome, password, permessi):
        super(Utente, self).__init__()
        self.nome = nome
        self.password = password
        self.permessi = permessi

    def get_nome(self):
        return self.nome

    def get_password(self):
        return self.password

    def get_permessi(self):
        return self.permessi

    def set_nome(self, nome):
        self.nome = nome

    def set_password(self, password):
        self.password = password

    def set_permessi(self, permessi):
        self.permessi = permessi
