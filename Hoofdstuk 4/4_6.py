# Libraries om met MySQL te verbinden.
from getpass import getpass
from mysql.connector import connect, Error

# Query aanmaken.
create_zangers_table_query = """
CREATE TABLE Zangers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    voornaam VARCHAR(100),
    achternaam VARCHAR(100)
);
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
            cursor.execute(create_zangers_table_query)
            connection.commit()

# Indien dit niet lukt, de foutmelding printen.
except Error as e:
    print(e)