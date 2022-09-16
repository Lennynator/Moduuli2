nimet =set()

nimi = input("Anna nimi: ")
if nimi !="":
    print("Uusi nimi")
while nimi!="":
    nimet.add(nimi)
    nimi = input("Anna seuraava nimi: ")
    if nimi in nimet:
        print("Aiemmin syötetty nimi!")
    else:print("Uusi nimi")



for i in nimet:
    print(i)

