# Libraries om met MySQL te verbinden.
from getpass import getpass
from mysql.connector import connect, Error

# Query aanmaken.
create_database_query = """
CREATE DATABASE StreamIT;
"""
# Probeer een verbinding te maken met de database world.
try:
    with connect(
        host="localhost",
        user="root",
        password="#Str3amIT#",
    ) as connection:
        # Query uitvoeren.
        with connection.cursor() as cursor:
            cursor.execute(create_database_query)
            # Feedback printen.
            print("Database StreamIT succesvol aangemaakt.")

# Indien dit niet lukt, de foutmelding printen.
except Error as e:
    print(e)