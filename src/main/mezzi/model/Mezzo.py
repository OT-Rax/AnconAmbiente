class Mezzo:
    def __init__(self, id, targa, tipo, funzione, iscrizione_albo, stato):
        self.id = id
        self.targa = targa
        self.tipo = tipo
        self.funzione = funzione
        self.iscrizione_albo = iscrizione_albo
        self.stato = stato

    # Metodi getters and setters

    def get_id_mezzo(self):
        return self.id

    def get_targa_mezzo(self):
        return self.targa

    def get_tipo_mezzo(self):
        return self.tipo

    def get_funzione_mezzo(self):
        return self.funzione

    def get_iscrizione_mezzo(self):
        return self.iscrizione_albo

    def get_stato_mezzo(self):
        return self.stato

    def set_id_mezzo(self, id):
        self.id = id

    def set_targa_mezzo(self, targa):
        self.targa = targa

    def set_tipo_mezzo(self, tipo):
        self.tipo = tipo

    def set_funzione_mezzo(self, funzione):
        self.funzione = funzione

    def set_iscrizione_mezzo(self, iscrizione_albo):
        self.iscrizione_albo = iscrizione_albo

    def set_stato(self, stato):
        self.stato = stato