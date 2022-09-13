def gallonat(maara):
    litrat=maara*3.785
    return litrat

luku1 = float(input("Anna gallonat: "))
while luku1>=0:
    tulos = gallonat(luku1)
    print(f"{luku1} galloonaa on litroina {tulos}.")
    luku1=float(input("Anna gallonat: "))
    if luku1<=0:
        break




