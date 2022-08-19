from models.MapperMezzi import MapperMezzi
from models.Mezzo import Mezzo
from models.MapperMezzi import MapperMezzi

class ControlloreMezzo:
    def __init__(self):
        self.mapper = MapperMezzi()

    def get_mezzo(self, id):
        return self.mapper.get_mezzo(id)
    
    def get_mezzi(self):
        return self.mapper.get_mezzi()
    
    def insert_mezzo(self, targa, tipo, allestimento, iscrizione_albo, patente, stato):
        return self.mapper.insert_operatore(targa, patente, tipo, allestimento, iscrizione_albo, stato)