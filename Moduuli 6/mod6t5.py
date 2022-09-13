import random

def funktio(luvut):
    for i in luvut:
        if i%2!=0: luvut.remove(i)
    return luvut
testiluvut=[]
for i in range (10):
    testiluvut.append(random.randint(0, 100))
print(f"Alkuperäinen lista on {testiluvut}\nf Listan parilliset luvut ovat: {funktio(testiluvut)}")