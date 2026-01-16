# Libraries om met MySQL te verbinden.
from getpass import getpass
from mysql.connector import connect, Error

# SQL-query aanamken.
show_table_Query = """DESCRIBE country;"""

# Probeer een verbinding te maken met de database world.
try:
    with connect(
        host="localhost",
        user="root",
        password="#Str3amIT#",
        database="world",
    ) as connection:
        
        # SQL-query uitvoeren in huidige verbinding.
        with connection.cursor() as cursor:
            cursor.execute(show_table_Query)
            result = cursor.fetchall()
            # Resultaten rij per rij printen.
            for row in result:
                print(row)

# Indien dit niet lukt, de foutmelding printen.
except Error as e:
    print(e)