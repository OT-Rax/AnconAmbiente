from models.MapperUtenti import MapperUtenti

class ControlloreUtenti:
    def __init__(self):
        self.mapper = MapperUtenti()
    
    def check_password(self, username, password):
        return self.mapper.check_password(username, password)
