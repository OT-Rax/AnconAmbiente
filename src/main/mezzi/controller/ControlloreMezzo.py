from src.main.mezzi.model.Mezzo import Mezzo
class ControlloreMezzo:
    def __init__(self):
        self.model = Mezzo()

    def get_id_mezzo(self):
        return self.model.get_id_mezzo()

    def get_targa_mezzo(self):
        return self.model.get_targa_mezzo()

    def get_tipo_mezzo(self):
        return self.model.get_tipo_mezzo()

    def get_funzione_mezzo(self):
        return self.model.get_funzione_mezzo()

    def get_iscrizione_mezzo(self):
        return self.model.get_iscrizione_mezzo()

    def get_stato_mezzo(self):
        return self.model.get_stato_mezzo()

    def set_targa_mezzo(self, targa):
        self.model.set_targa_mezzo(targa)

    def set_tipo_mezzo(self, tipo):
        self.model.set_tipo_mezzo(tipo)

    def set_iscrizione_mezzo(self, iscrizione):
        self.model.set_iscrizione_mezzo(iscrizione)

    def set_stato_mezzo(self, stato):
        self.model.set_stato(stato)