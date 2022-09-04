from models.MapperOperatori import MapperOperatori

class ControlloreOperatori:
    def __init__(self):
        self.mapper = MapperOperatori()
        
    #Metodi che si collegano ai metodi del mapper Operatori

    def get_operatore(self, id):
        return self.mapper.get_operatore(id)

    def get_operatori(self):
        return self.mapper.get_operatori()

    def get_operatori_disponibili(self, data_inizio, data_fine):
        return self.mapper.get_operatori_disponibili(data_inizio, data_fine)

    def insert_operatore(self, nome, cognome, cf, data_nascita, patenti, data_fine_contratto):
        return self.mapper.insert_operatore(nome, cognome, cf, data_nascita, patenti, data_fine_contratto, 0)

    def ricerca_operatori(self, text):
        return self.mapper.ricerca_operatori(text)

    def elimina_operatori(self, operatori):
        return self.mapper.elimina_operatori(operatori)

    def modifica_operatore(self, operatore):
        return self.mapper.update_operatore(operatore.get_id(), operatore)
