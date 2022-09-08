import random
numero=random.randint(1,6)
arvaus=""
while not arvaus==numero:
    arvaus=int(input("Arvaa numero: "))
    if arvaus>numero:
        print("Liian suuri arvaus")
    elif arvaus<numero:
        print("Liian pieni arvaus")
else:
    print("Oikea arvaus")



