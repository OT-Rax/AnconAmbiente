from models.MapperTurni import MapperTurno

class ControlloreTurni:
    def __init__(self):
        self.mapper = MapperTurno()
        
    def get_turno(self, id):
        return self.mapper.get_turno(id)

    def get_turni(self):
        return self.mapper.get_turni()

    def insert_turno(self, servizio, data, ora_inizio, ora_fine, mezzo, operatore):
        return self.mapper.insert_turno(servizio, data, ora_inizio, ora_fine, mezzo, operatore)

    def ricerca_turni(self, text):
        return self.mapper.ricerca_turni(text)

    def elimina_turni(self, turni):
        return self.mapper.elimina_turni(turni)

    def modifica_turno(self, turno):
        return self.mapper.update_turno(turno.get_id(), turno)