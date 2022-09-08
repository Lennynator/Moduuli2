import random
maara=int(input("Anna noppien määrä: "))
nopat=0
lista=[]
for nopa in range(maara):
    nopat=random.randint(1,6)
    lista.append(nopat)

print(f"Noppien summa on {sum(lista)}")
