import mysql.connector
def haelentokentta(icao):
    tuple=(icao,)
    sql='''SELECT name, municipality FROM airport 
    WHERE ident= %s'''
    kursori= yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos=kursori.fetchone()
    return tulos;


yhteys =mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Torstai22#',
         autocommit=True
         )
kentta=input("Anna ICAO koodi: ")
if kentta is not None:
    print(f'Nimi: {kentta[0]}, kunta:  {kentta[1]}')
else:print("Ei ICAO koodi")