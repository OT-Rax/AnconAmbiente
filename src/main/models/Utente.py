class Utente:
    def __init__(self, id, username, password, permessi):
        super(Utente, self).__init__()
        self.id = id
        self.username = username
        self.password = password
        self.permessi = permessi

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password

    def get_permessi(self):
        return self.permessi

    def set_id(self, id):
        self.id = id

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_permessi(self, permessi):
        self.permessi = permessi
