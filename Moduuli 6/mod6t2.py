import random


def heitaNoppaa(lkm):
    return random.randint(1, lkm)

lkm=int(input("Syötä tahkojen lukumäärä: "))
noppa = 0
while noppa != lkm:
        noppa=heitaNoppaa(lkm)
        print(noppa)
