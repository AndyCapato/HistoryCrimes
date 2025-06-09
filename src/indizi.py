
class Indizi():
    def __init__(self, tipo, descrizione):
        self.tipo=tipo
        self.descrizione=descrizione
        self.registrato= False
    
    def __str__(self):
        return self.descrizione
        