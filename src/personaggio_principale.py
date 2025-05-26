from src.character import Character
class PersonaggioPrincipale(Character):
    def __init__(self, livello, nome, cognome):
        super().__init__(nome, cognome)
        self.livello=livello

   



