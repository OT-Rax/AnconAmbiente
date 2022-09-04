from models.MapperTurni import MapperTurni

class ControlloreTurni:
    def __init__(self):
        self.mapper = MapperTurni()
        
    def get_turno(self, id):
        return self.mapper.get_turno(id)

    def get_turni(self):
        return self.mapper.get_turni()

    def get_turni_operatore(self, id_operatore, data_inizio, data_fine):
        return self.mapper.get_turni_operatore(id_operatore, data_inizio, data_fine)

    def get_turni_mezzo(self, id_mezzo, data_inizio, data_fine):
        return self.mapper.get_turni_mezzo(id_mezzo,data_inizio, data_fine)

    def get_turni_servizio(self, id_servizio, data_inizio, data_fine):
        return self.mapper.get_turni_servizio(id_servizio,data_inizio, data_fine)

    def get_turni_cliente(self, id_cliente, data_inizio, data_fine):
        return self.mapper.get_turni_cliente(id_cliente,data_inizio, data_fine)

    def insert_turno(self, id_servizio, data_inizio, data_fine, id_mezzi, id_operatori):
        return self.mapper.insert_turno(id_servizio, data_inizio, data_fine, id_mezzi, id_operatori)

    def filtra_turni(self, da_data, a_data):
        return self.mapper.filtra_turni(da_data, a_data)

    def elimina_turni(self, turni):
        return self.mapper.elimina_turni(turni)

    def modifica_turno(self, turno):
        return self.mapper.update_turno(turno.get_id(), turno)
