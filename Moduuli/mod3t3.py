sukupuoli=input("Anna sukupuoli: ")
hemo=int(input("Anna hemoglobiiniarvo"))
if sukupuoli=="nainen"and hemo<117:
    print("Hemoglobiiniarvo alhainen")
elif sukupuoli=="nainen" and hemo>175 :
    print("Hemoglobiiniarvo korkea")
elif sukupuoli == "nainen" and 117<= hemo <= 175:
    print("Hemoglobiiniarvo normaali")
elif sukupuoli=="mies" and hemo<134:
    print("Hemoglobiiniarvo alhainen")
elif sukupuoli == "mies" and hemo>195:
    print("Hemoglobiiniarvo korkea")
elif sukupuoli == "mies" and 134<=hemo<=195:
     print("Hemoglobiiniarvo normaali")