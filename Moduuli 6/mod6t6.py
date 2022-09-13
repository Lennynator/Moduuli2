import math

def yksikkohinta(halkaisija, hinta):
    pinta_ala=math.pi*(halkaisija/100/2)**2
    return  hinta/pinta_ala

pizzahalkaisja1=float(input("Anna 1. pizzan halkaisija: "))
pizzahinta1=float(input("Anna 1. pizzan hinta: "))
pizzahalkaisja2=float(input("Anna 2. pizzan halkaisija: "))
pizzahinta2=float(input("Anna 2. pizzan hinta: "))

yksilohinta1= yksikkohinta(pizzahalkaisja1, pizzahinta1)
yksilohinta2= yksikkohinta(pizzahalkaisja2, pizzahinta2)

print(f"1. pizzan yksikköhinta on {yksilohinta1:.2f}€/m2")
print(f"2. pizzan yksikköhinta on {yksilohinta2:.2f}€/m2")

pizza1=["1. pizza", yksilohinta1]
pizza2=["2. pizza", yksilohinta2]
pizzat=[pizza1, pizza2]

edullisempi=pizzat[0][0]
yksikkohinta=pizzat[0][1]
for pitsa in pizzat:
    if pitsa[1] < yksikkohinta:
        edullisempi=pitsa[0]
    yksilohinta2=pitsa[1]

print(f"{edullisempi} on edullisempi")
