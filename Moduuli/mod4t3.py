numero=(input ("Anna numero: "))
lista=[]
while numero!=(""):
    numero=(input("Anna numero: "))
    lista.append(numero)
    if numero==(""):
        print("Suurin annettu numeron on:"+max(lista))
        print("Pienin annettu numero on"+min(lista))



