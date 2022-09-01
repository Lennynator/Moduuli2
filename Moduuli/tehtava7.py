hinta=float(input("Anna ravintolalounaan hinta:"))

if hinta>=20:
    print("Erittäin kallis")
elif hinta>=12:
    print("Melko kallis")
elif hinta>=8:
    print("Melko edullinen")
else:
    print("Edullinen")
