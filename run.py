from src.diario import Diario
from src.indizi import Indizi
indizio1=Indizi("lettera", "la lettera di jack lo squartatore")
indizio2=Indizi("impronta","Impronta scena del crimine")

diario = Diario()
diario.registra_indizio(indizio1)
diario.registra_indizio(indizio2)
print("Giocatore si avvicina allo sprite dell'NPC")
print("Giocatore interagisce col NPC")
print("NPC rivela indizio al giocatore")
indizio3=Indizi("Dichiarazione","Dichiarazione rilasciata dal NPC")
diario.registra_indizio(indizio3)
print("Indizi presenti nel Diario")
print(diario.indizi[0])
print(diario.indizi[1])
print(diario.indizi[2])