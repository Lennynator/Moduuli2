from geopy import distance



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
         autocommit=True)
