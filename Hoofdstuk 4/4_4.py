# Libraries om met MySQL te verbinden.
from getpass import getpass
from mysql.connector import connect, Error

# Queries aanmaken.
select_Belgium_Query = """
SELECT * FROM country WHERE name = "Belgium";
"""
select_Europe_Query = """
SELECT Name, Population FROM country WHERE Continent = "Europe"; 
"""
# Probeer een verbinding te maken met de database world.
try:
    with connect(
        host="localhost",
        user="root",
        password="#Str3amIT#",
        database="world",
    ) as connection:
        # Queries uitvoeren.
        with connection.cursor() as cursor:
            cursor.execute(select_Belgium_Query)
            result_Belgium = cursor.fetchall()

            cursor.execute(select_Europe_Query)
            result_Europe = cursor.fetchall()

            # Resultaten printen.
            print("Gegevens België:")
            print(result_Belgium)
            
            print("Gegevens Europese landen:")
            for row in result_Europe:
                print(row)

# Indien dit niet lukt, de foutmelding printen.
except Error as e:
    print(e)
