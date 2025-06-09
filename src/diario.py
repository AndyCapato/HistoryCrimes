from src.indizi import Indizi
class Diario ():
    def __init__(self):
        self.indizi: list[Indizi] = []

    def registra_indizio(self, indizio):
        indizio.registrato = True
        self.indizi.append (indizio)
    


    