from models.MapperClienti import MapperClienti

class ControlloreClienti:
    def __init__(self):
        self.mapper = MapperClienti()

    #Metodi che si collegano ai metodi del mapper Clienti

    def get_cliente(self, id):
        return self.mapper.get_cliente(id)

    def get_clienti(self):
        return self.mapper.get_clienti()

    def get_idclienti(self):
        return self.mapper.get_idclienti()

    #id, nome, cognome, datanascita, cf, partitaiva, indirizzo, email, telefono):
    def insert_cliente(self, nome, cognome, datanascita, cf, partitaiva, indirizzo, email, telefono):
        return self.mapper.insert_cliente(nome, cognome, datanascita, cf, partitaiva, indirizzo, email, telefono)

    def ricerca_clienti(self, text):
        return self.mapper.ricerca_clienti(text)

    def elimina_clienti(self, clienti):
        return self.mapper.elimina_clienti(clienti)

    def modifica_cliente(self, cliente):
        return self.mapper.update_cliente(cliente.get_id(), cliente)
