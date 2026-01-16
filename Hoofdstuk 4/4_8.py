# Libraries om met MySQL te verbinden.
from getpass import getpass
from mysql.connector import connect, Error

# Query aanmaken.
insert_zangers_query="""
INSERT INTO Zangers(voornaam, achternaam)
VALUES
    ("David", "Getta"),
    ("Rihanna", ""),
    ("Ed", "Sheeran"),
    ("Madonna", "");
"""
# Probeer een verbinding te maken met de database world.
try:
    with connect(
        host="localhost",
        user="root",
        password="#Str3amIT#",
        database="StreamIT",
    ) as connection:
        
        # Query uitvoeren.
        with connection.cursor() as cursor:
            cursor.execute(insert_zangers_query)
            connection.commit()

# Indien dit niet lukt, de foutmelding printen.
except Error as e:
    print(e)