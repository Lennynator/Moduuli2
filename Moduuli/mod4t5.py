tunnus="python"
salasana="rules"
toistot=5
yritykset=0

while (tunnus=="python" and salasana=="rules") and yritykset<toistot:
    tunnus=("Annan käyttäjätunnus:")
    salasana=input("Anna salasana:")
    yritykset=yritykset+1

if (yritykset>=5):
    print("Pääsy evätty")

else:
    print("Tervetuloa")

