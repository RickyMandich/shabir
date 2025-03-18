# Esercizio
# Si depositano 10 000€ in un conto bancario, remunerato con un interesse annuo del 5%. Quanti anni occorrono perchè il saldo del conto diventi il doppio dell'investimento iniziale?
#
# Scrivi un programma che legge da tastiera l'investimento iniziale e stampi il numero di anni necessari


saldo = float(input("inserisci l'investimento iniziale\n\t"))
anni = 0
obbiettivo = saldo*2
while(saldo<obbiettivo):
    # incremento gli anni
    anni+=1
    # aggiungo gli interessi
    saldo = saldo + (saldo/20)
print("hai maturato",int(saldo),"€ in",anni,"anni")


# obbiettivo = 20 000
# saldo >= 20 000